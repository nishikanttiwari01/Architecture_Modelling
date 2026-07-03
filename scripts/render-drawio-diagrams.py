#!/usr/bin/env python3
"""Render the book's Draw.io teaching diagrams to SVG and PNG.

This renderer reads the editable Draw.io mxGraph model (geometry, styles and
text) and produces an SVG vector export and a PNG preview directly from that
source. It is deliberately small and supports only the subset of Draw.io shapes
used by the book's Chapter 13 teaching diagrams: rectangles (optionally
rounded), ellipses, plain text cells and straight or orthogonal connectors with
optional arrowheads and labels.

The Draw.io file remains the single editable source of truth. The SVG and PNG
are generated from it, not hand drawn or screenshotted. This mirrors the
BPMN render-from-source approach recorded in DEC-012 and is recorded for
Draw.io in DEC-021 (Proposed: the previews are reproducible teaching exports,
not verified native Draw.io exports).

Dependency: Pillow. Install it reproducibly with
    python -m pip install -r requirements-diagrams.txt
Font selection is deterministic and cross-platform: Arial is preferred (so the
Windows-rendered reference exports stay byte-stable) with DejaVu Sans as an
explicit fallback. The selected family is reported on stdout, and the renderer
fails with a clear message if no supported font is available.
"""

from __future__ import annotations

import html
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SVG_DIR = ROOT / "diagrams/exported/svg"
PNG_DIR = ROOT / "diagrams/exported/png"

MARGIN = 20
PNG_SCALE = 2  # supersample for a crisp preview

# Deterministic cross-platform font selection. Arial is preferred so that the
# reference exports rendered on Windows stay byte-stable; DejaVu Sans is the
# explicit fallback on Linux and other environments. The renderer reports which
# family it selected and fails loudly if none is available rather than silently
# switching to an unknown platform-dependent font.
FONT_FAMILIES: list[tuple[str, str, str, str]] = [
    (
        "Arial",
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/ariali.ttf",
    ),
    (
        "DejaVu Sans",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf",
    ),
    (
        "DejaVu Sans (Fedora/RHEL)",
        "/usr/share/fonts/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans-Oblique.ttf",
    ),
    (
        "DejaVu Sans (Arch)",
        "/usr/share/fonts/TTF/DejaVuSans.ttf",
        "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/TTF/DejaVuSans-Oblique.ttf",
    ),
    (
        "Arial (macOS)",
        "/Library/Fonts/Arial.ttf",
        "/Library/Fonts/Arial Bold.ttf",
        "/Library/Fonts/Arial Italic.ttf",
    ),
]

_FONT_CACHE: dict[tuple[str, int], ImageFont.FreeTypeFont] = {}
_RESOLVED_FONTS: dict[str, str] | None = None


def _loadable(path: str) -> bool:
    try:
        ImageFont.truetype(path, 12)
        return True
    except OSError:
        return False


def resolve_fonts() -> dict[str, str]:
    """Pick the first available font family and report the selection.

    Returns a mapping with 'regular', 'bold' and 'italic' TrueType paths. A
    missing bold or italic variant falls back to the family's regular file.
    Raises SystemExit with a clear message when no supported font is found.
    """
    for name, regular, bold, italic in FONT_FAMILIES:
        if regular and _loadable(regular):
            resolved = {
                "family": name,
                "regular": regular,
                "bold": bold if bold and _loadable(bold) else regular,
                "italic": italic if italic and _loadable(italic) else regular,
            }
            print(
                f"render-drawio-diagrams: using font family '{name}' "
                f"(regular={resolved['regular']})"
            )
            return resolved
    tried = ", ".join(family[0] for family in FONT_FAMILIES)
    raise SystemExit(
        "render-drawio-diagrams: no supported font was found. "
        f"Tried: {tried}. Install Arial or DejaVu Sans "
        "(for example the 'fonts-dejavu' package) and retry."
    )


def _fonts() -> dict[str, str]:
    global _RESOLVED_FONTS
    if _RESOLVED_FONTS is None:
        _RESOLVED_FONTS = resolve_fonts()
    return _RESOLVED_FONTS


def get_font(bold: bool, italic: bool, size: int) -> ImageFont.FreeTypeFont:
    fonts = _fonts()
    if bold:
        path = fonts["bold"]
    elif italic:
        path = fonts["italic"]
    else:
        path = fonts["regular"]
    key = (path, size)
    if key not in _FONT_CACHE:
        _FONT_CACHE[key] = ImageFont.truetype(path, size)
    return _FONT_CACHE[key]


def parse_style(style: str | None) -> dict[str, str]:
    result: dict[str, str] = {}
    if not style:
        return result
    for part in style.split(";"):
        part = part.strip()
        if not part:
            continue
        if "=" in part:
            key, value = part.split("=", 1)
            result[key.strip()] = value.strip()
        else:
            result[part] = "1"  # flag such as "rounded" or "ellipse" or "text"
    return result


def clean_text(value: str | None) -> list[str]:
    """Turn an mxGraph label into a list of hard lines."""
    if not value:
        return []
    text = value
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"</div>", "\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)  # strip any remaining tags
    text = html.unescape(text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = text.split("\n")
    # drop a single trailing empty line created by a trailing break
    while len(lines) > 1 and lines[-1] == "":
        lines.pop()
    return lines


def wrap_lines(hard_lines: list[str], font: ImageFont.FreeTypeFont, max_width: float, wrap: bool) -> list[str]:
    if not wrap:
        return hard_lines
    wrapped: list[str] = []
    for line in hard_lines:
        if line == "":
            wrapped.append("")
            continue
        words = line.split(" ")
        current = ""
        for word in words:
            candidate = word if current == "" else current + " " + word
            if font.getlength(candidate) <= max_width or current == "":
                current = candidate
            else:
                wrapped.append(current)
                current = word
        wrapped.append(current)
    return wrapped


class Cell:
    def __init__(self, element: ET.Element):
        self.id = element.attrib.get("id", "")
        self.value = element.attrib.get("value", "")
        self.style = parse_style(element.attrib.get("style"))
        self.is_vertex = element.attrib.get("vertex") == "1"
        self.is_edge = element.attrib.get("edge") == "1"
        self.source = element.attrib.get("source")
        self.target = element.attrib.get("target")
        self.x = self.y = self.w = self.h = 0.0
        self.waypoints: list[tuple[float, float]] = []
        geometry = element.find("mxGeometry")
        if geometry is not None:
            self.x = float(geometry.attrib.get("x", 0) or 0)
            self.y = float(geometry.attrib.get("y", 0) or 0)
            self.w = float(geometry.attrib.get("width", 0) or 0)
            self.h = float(geometry.attrib.get("height", 0) or 0)
            for array in geometry.findall("Array"):
                if array.attrib.get("as") == "points":
                    for point in array.findall("mxPoint"):
                        self.waypoints.append(
                            (float(point.attrib.get("x", 0) or 0), float(point.attrib.get("y", 0) or 0))
                        )

    @property
    def cx(self) -> float:
        return self.x + self.w / 2

    @property
    def cy(self) -> float:
        return self.y + self.h / 2


def border_point(cell: Cell, toward: tuple[float, float]) -> tuple[float, float]:
    """Point on the rectangle border of ``cell`` in the direction of ``toward``."""
    cx, cy = cell.cx, cell.cy
    tx, ty = toward
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    half_w, half_h = cell.w / 2, cell.h / 2
    scale_x = half_w / abs(dx) if dx != 0 else float("inf")
    scale_y = half_h / abs(dy) if dy != 0 else float("inf")
    scale = min(scale_x, scale_y)
    return cx + dx * scale, cy + dy * scale


class Renderer:
    def __init__(self, cells: list[Cell]):
        self.cells = cells
        self.by_id = {c.id: c for c in cells if c.id}
        self.vertices = [c for c in cells if c.is_vertex and c.w > 0 and c.h > 0]
        self.edges = [c for c in cells if c.is_edge]
        max_x = max((c.x + c.w for c in self.vertices), default=100.0)
        max_y = max((c.y + c.h for c in self.vertices), default=100.0)
        for edge in self.edges:
            for wx, wy in edge.waypoints:
                max_x = max(max_x, wx)
                max_y = max(max_y, wy)
        self.width = int(max_x + MARGIN)
        self.height = int(max_y + MARGIN)

    # ---- geometry helpers -------------------------------------------------
    def edge_path(self, edge: Cell) -> list[tuple[float, float]]:
        src = self.by_id.get(edge.source) if edge.source else None
        tgt = self.by_id.get(edge.target) if edge.target else None
        points: list[tuple[float, float]] = list(edge.waypoints)
        if src is not None:
            first_ref = points[0] if points else (tgt.cx, tgt.cy) if tgt else (src.cx, src.cy)
            start = border_point(src, first_ref)
        else:
            start = points[0] if points else (0, 0)
            if points:
                points = points[1:]
        if tgt is not None:
            last_ref = points[-1] if points else start
            end = border_point(tgt, last_ref)
        else:
            end = points[-1] if points else start
            if points:
                points = points[:-1]
        return [start, *points, end]

    # ---- SVG --------------------------------------------------------------
    def to_svg(self, title: str, desc: str) -> str:
        out: list[str] = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}" '
            f'viewBox="0 0 {self.width} {self.height}" role="img" aria-labelledby="ttl dsc">',
            f'  <title id="ttl">{html.escape(title)}</title>',
            f'  <desc id="dsc">{html.escape(desc)}</desc>',
            f'  <rect x="0" y="0" width="{self.width}" height="{self.height}" fill="#FFFFFF"/>',
        ]
        for cell in self.vertices:
            out.extend(self._svg_vertex(cell))
        for edge in self.edges:
            out.extend(self._svg_edge(edge))
        out.append("</svg>")
        return "\n".join(out) + "\n"

    def _svg_vertex(self, cell: Cell) -> list[str]:
        s = cell.style
        if "text" in s and "fillColor" not in s and "rounded" not in s and "ellipse" not in s:
            fill = None
            stroke = None
        else:
            fill = s.get("fillColor", "#FFFFFF")
            stroke = s.get("strokeColor", "#333333")
        lines: list[str] = []
        stroke_width = s.get("strokeWidth", "1")
        dash = ' stroke-dasharray="6 4"' if s.get("dashed") == "1" else ""
        if "ellipse" in s:
            if fill is not None:
                lines.append(
                    f'  <ellipse cx="{cell.cx:.1f}" cy="{cell.cy:.1f}" rx="{cell.w/2:.1f}" ry="{cell.h/2:.1f}" '
                    f'fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"{dash}/>'
                )
        elif fill is not None:
            rx = 8 if s.get("rounded") == "1" else 0
            lines.append(
                f'  <rect x="{cell.x:.1f}" y="{cell.y:.1f}" width="{cell.w:.1f}" height="{cell.h:.1f}" '
                f'rx="{rx}" ry="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"{dash}/>'
            )
        lines.extend(self._svg_text(cell))
        return lines

    def _svg_text(self, cell: Cell) -> list[str]:
        s = cell.style
        hard = clean_text(cell.value)
        if not hard:
            return []
        size = int(s.get("fontSize", "12"))
        bold = (int(s.get("fontStyle", "0")) & 1) == 1
        italic = (int(s.get("fontStyle", "0")) & 2) == 2
        font = get_font(bold, italic, size)
        wrap = s.get("whiteSpace") == "wrap"
        pad = 6
        lines = wrap_lines(hard, font, max(cell.w - 2 * pad, 10), wrap)
        line_height = size * 1.3
        block_h = line_height * len(lines)
        valign = s.get("verticalAlign", "middle")
        if valign == "top":
            y0 = cell.y + pad + size
        elif valign == "bottom":
            y0 = cell.y + cell.h - block_h + size
        else:
            y0 = cell.cy - block_h / 2 + size
        align = s.get("align", "center")
        color = s.get("fontColor", "#111827")
        weight = ' font-weight="bold"' if bold else ""
        style_attr = ' font-style="italic"' if italic else ""
        if align == "left":
            anchor = "start"
            tx = cell.x + pad
        elif align == "right":
            anchor = "end"
            tx = cell.x + cell.w - pad
        else:
            anchor = "middle"
            tx = cell.cx
        result: list[str] = []
        for i, line in enumerate(lines):
            if line == "":
                continue
            y = y0 + i * line_height
            result.append(
                f'  <text x="{tx:.1f}" y="{y:.1f}" text-anchor="{anchor}" '
                f'font-family="Arial, sans-serif" font-size="{size}"{weight}{style_attr} '
                f'fill="{color}">{html.escape(line)}</text>'
            )
        return result

    def _svg_edge(self, edge: Cell) -> list[str]:
        s = edge.style
        path = self.edge_path(edge)
        if len(path) < 2:
            return []
        stroke = s.get("strokeColor", "#333333")
        stroke_width = s.get("strokeWidth", "1.5")
        dash = ' stroke-dasharray="6 4"' if s.get("dashed") == "1" else ""
        d = f'M{path[0][0]:.1f} {path[0][1]:.1f} ' + " ".join(f'L{x:.1f} {y:.1f}' for x, y in path[1:])
        lines = [f'  <path d="{d}" fill="none" stroke="{stroke}" stroke-width="{stroke_width}"{dash}/>']
        if s.get("endArrow", "classic") != "none":
            lines.extend(self._svg_arrow(path[-2], path[-1], stroke))
        if s.get("startArrow", "none") != "none":
            lines.extend(self._svg_arrow(path[1], path[0], stroke))
        label = clean_text(edge.value)
        if label:
            mx, my = self._label_anchor(edge, path)
            lines.extend(self._svg_edge_label(edge, label, mx, my))
        return lines

    @staticmethod
    def _label_anchor(edge: Cell, path: list[tuple[float, float]]) -> tuple[float, float]:
        if "lx" in edge.style and "ly" in edge.style:
            return float(edge.style["lx"]), float(edge.style["ly"])
        mid_index = len(path) // 2
        if len(path) % 2 == 0:
            mx = (path[mid_index - 1][0] + path[mid_index][0]) / 2
            my = (path[mid_index - 1][1] + path[mid_index][1]) / 2
        else:
            mx, my = path[mid_index]
        return mx, my

    def _svg_arrow(self, frm: tuple[float, float], to: tuple[float, float], color: str) -> list[str]:
        import math

        angle = math.atan2(to[1] - frm[1], to[0] - frm[0])
        size = 10
        p1 = (to[0] - size * math.cos(angle - math.pi / 7), to[1] - size * math.sin(angle - math.pi / 7))
        p2 = (to[0] - size * math.cos(angle + math.pi / 7), to[1] - size * math.sin(angle + math.pi / 7))
        return [
            f'  <polygon points="{to[0]:.1f},{to[1]:.1f} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" '
            f'fill="{color}"/>'
        ]

    def _svg_edge_label(self, edge: Cell, lines: list[str], mx: float, my: float) -> list[str]:
        size = int(edge.style.get("fontSize", "11"))
        font = get_font(False, False, size)
        width = max((font.getlength(line) for line in lines), default=0)
        line_height = size * 1.3
        box_w = width + 10
        box_h = line_height * len(lines) + 4
        out = [
            f'  <rect x="{mx - box_w/2:.1f}" y="{my - box_h/2:.1f}" width="{box_w:.1f}" height="{box_h:.1f}" '
            f'rx="3" ry="3" fill="#FFFFFF" stroke="#B0B7C3" stroke-width="0.8"/>'
        ]
        y0 = my - box_h / 2 + size + 1
        for i, line in enumerate(lines):
            out.append(
                f'  <text x="{mx:.1f}" y="{y0 + i*line_height:.1f}" text-anchor="middle" '
                f'font-family="Arial, sans-serif" font-size="{size}" fill="#1D2939">{html.escape(line)}</text>'
            )
        return out

    # ---- PNG --------------------------------------------------------------
    def to_png(self) -> Image.Image:
        scale = PNG_SCALE
        img = Image.new("RGB", (self.width * scale, self.height * scale), "#FFFFFF")
        draw = ImageDraw.Draw(img)
        for cell in self.vertices:
            self._png_vertex(draw, cell, scale)
        for edge in self.edges:
            self._png_edge(draw, edge, scale)
        return img

    def _png_vertex(self, draw: ImageDraw.ImageDraw, cell: Cell, scale: int) -> None:
        s = cell.style
        box = [cell.x * scale, cell.y * scale, (cell.x + cell.w) * scale, (cell.y + cell.h) * scale]
        is_plain_text = "text" in s and "fillColor" not in s and "rounded" not in s and "ellipse" not in s
        if not is_plain_text:
            fill = s.get("fillColor", "#FFFFFF")
            stroke = s.get("strokeColor", "#333333")
            sw = max(1, int(round(float(s.get("strokeWidth", "1")) * scale)))
            if "ellipse" in s:
                draw.ellipse(box, fill=fill, outline=stroke, width=sw)
            elif s.get("rounded") == "1":
                draw.rounded_rectangle(box, radius=8 * scale, fill=fill, outline=stroke, width=sw)
            else:
                draw.rectangle(box, fill=fill, outline=stroke, width=sw)
        self._png_text(draw, cell, scale)

    def _png_text(self, draw: ImageDraw.ImageDraw, cell: Cell, scale: int) -> None:
        s = cell.style
        hard = clean_text(cell.value)
        if not hard:
            return
        size = int(s.get("fontSize", "12"))
        bold = (int(s.get("fontStyle", "0")) & 1) == 1
        italic = (int(s.get("fontStyle", "0")) & 2) == 2
        font = get_font(bold, italic, size)
        font_scaled = get_font(bold, italic, size * scale)
        wrap = s.get("whiteSpace") == "wrap"
        pad = 6
        lines = wrap_lines(hard, font, max(cell.w - 2 * pad, 10), wrap)
        line_height = size * 1.3 * scale
        block_h = line_height * len(lines)
        valign = s.get("verticalAlign", "middle")
        if valign == "top":
            y = cell.y * scale + pad * scale
        elif valign == "bottom":
            y = (cell.y + cell.h) * scale - block_h
        else:
            y = cell.cy * scale - block_h / 2
        align = s.get("align", "center")
        color = s.get("fontColor", "#111827")
        for line in lines:
            if line == "":
                y += line_height
                continue
            if align == "left":
                x = cell.x * scale + pad * scale
                anchor = "la"
            elif align == "right":
                x = (cell.x + cell.w) * scale - pad * scale
                anchor = "ra"
            else:
                x = cell.cx * scale
                anchor = "ma"
            draw.text((x, y), line, font=font_scaled, fill=color, anchor=anchor)
            y += line_height

    def _png_edge(self, draw: ImageDraw.ImageDraw, edge: Cell, scale: int) -> None:
        s = edge.style
        path = self.edge_path(edge)
        if len(path) < 2:
            return
        stroke = s.get("strokeColor", "#333333")
        sw = max(1, int(round(float(s.get("strokeWidth", "1.5")) * scale)))
        pts = [(x * scale, y * scale) for x, y in path]
        if s.get("dashed") == "1":
            for i in range(len(pts) - 1):
                self._dashed_line(draw, pts[i], pts[i + 1], stroke, sw)
        else:
            draw.line(pts, fill=stroke, width=sw, joint="curve")
        if s.get("endArrow", "classic") != "none":
            self._png_arrow(draw, pts[-2], pts[-1], stroke, scale)
        if s.get("startArrow", "none") != "none":
            self._png_arrow(draw, pts[1], pts[0], stroke, scale)
        label = clean_text(edge.value)
        if label:
            if "lx" in s and "ly" in s:
                mx, my = float(s["lx"]) * scale, float(s["ly"]) * scale
            else:
                mid_index = len(pts) // 2
                if len(pts) % 2 == 0:
                    mx = (pts[mid_index - 1][0] + pts[mid_index][0]) / 2
                    my = (pts[mid_index - 1][1] + pts[mid_index][1]) / 2
                else:
                    mx, my = pts[mid_index]
            self._png_edge_label(draw, edge, label, mx, my, scale)

    def _dashed_line(self, draw, p0, p1, color, width) -> None:
        import math

        length = math.hypot(p1[0] - p0[0], p1[1] - p0[1])
        if length == 0:
            return
        dash, gap = 6 * PNG_SCALE, 4 * PNG_SCALE
        dx, dy = (p1[0] - p0[0]) / length, (p1[1] - p0[1]) / length
        pos = 0.0
        while pos < length:
            a = (p0[0] + dx * pos, p0[1] + dy * pos)
            end = min(pos + dash, length)
            b = (p0[0] + dx * end, p0[1] + dy * end)
            draw.line([a, b], fill=color, width=width)
            pos += dash + gap

    def _png_arrow(self, draw, frm, to, color, scale) -> None:
        import math

        angle = math.atan2(to[1] - frm[1], to[0] - frm[0])
        size = 10 * scale
        p1 = (to[0] - size * math.cos(angle - math.pi / 7), to[1] - size * math.sin(angle - math.pi / 7))
        p2 = (to[0] - size * math.cos(angle + math.pi / 7), to[1] - size * math.sin(angle + math.pi / 7))
        draw.polygon([to, p1, p2], fill=color)

    def _png_edge_label(self, draw, edge, lines, mx, my, scale) -> None:
        size = int(edge.style.get("fontSize", "11"))
        font = get_font(False, False, size * scale)
        widths = [draw.textlength(line, font=font) for line in lines]
        width = max(widths, default=0)
        line_height = size * 1.3 * scale
        box_w = width + 10 * scale
        box_h = line_height * len(lines) + 4 * scale
        draw.rounded_rectangle(
            [mx - box_w / 2, my - box_h / 2, mx + box_w / 2, my + box_h / 2],
            radius=3 * scale,
            fill="#FFFFFF",
            outline="#B0B7C3",
            width=max(1, scale),
        )
        y = my - box_h / 2 + 2 * scale
        for line in lines:
            draw.text((mx, y), line, font=font, fill="#1D2939", anchor="ma")
            y += line_height


def load_cells(path: Path) -> list[Cell]:
    tree = ET.parse(path)
    root = tree.getroot()
    model = root.find(".//mxGraphModel")
    if model is None:
        raise ValueError(f"{path}: no mxGraphModel found")
    graph_root = model.find("root")
    if graph_root is None:
        raise ValueError(f"{path}: no <root> found")
    cells = [Cell(el) for el in graph_root.findall("mxCell")]
    return cells


def get_title_desc(path: Path, cells: list[Cell]) -> tuple[str, str]:
    for cell in cells:
        if "figtitle" in cell.style:
            title_lines = clean_text(cell.value)
            return (" ".join(title_lines), " ".join(title_lines))
    return (path.stem, path.stem)


def render(path: Path) -> tuple[Path, Path]:
    cells = load_cells(path)
    renderer = Renderer(cells)
    title, desc = get_title_desc(path, cells)
    svg_path = SVG_DIR / f"{path.stem}.svg"
    png_path = PNG_DIR / f"{path.stem}.png"
    svg_path.write_text(renderer.to_svg(title, desc), encoding="utf-8")
    renderer.to_png().save(png_path)
    return svg_path, png_path


def main() -> int:
    args = [Path(a) for a in sys.argv[1:]]
    if not args:
        args = sorted((ROOT / "diagrams/source/drawio").glob("FIG-*.drawio"))
    for arg in args:
        source = arg if arg.is_absolute() else ROOT / arg
        svg_path, png_path = render(source)
        print(f"Rendered {svg_path.relative_to(ROOT)} and {png_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
