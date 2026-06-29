#!/usr/bin/env python3
"""Render the book's simple BPMN DI examples to SVG.

This is intentionally small. It reads BPMN Diagram Interchange coordinates
from the XML source files and renders the subset of BPMN used by the book's
teaching examples.
"""

from __future__ import annotations

import html
import sys
import textwrap
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NS = {
    "bpmn": "http://www.omg.org/spec/BPMN/20100524/MODEL",
    "bpmndi": "http://www.omg.org/spec/BPMN/20100524/DI",
    "dc": "http://www.omg.org/spec/DD/20100524/DC",
    "di": "http://www.omg.org/spec/DD/20100524/DI",
}

TITLES = {
    "FIG-06-01-online-store-order-fulfilment-process": "FIG-06-01. Online Store Order Fulfilment BPMN Process",
    "FIG-06-02-horizon-bank-customer-onboarding-collaboration": "FIG-06-02. Horizon Bank Customer Onboarding BPMN Collaboration",
    "FIG-06-03-horizon-bank-payment-repair-exception-process": "FIG-06-03. Horizon Bank Payment Repair BPMN Exception Collaboration",
}

DESCRIPTIONS = {
    "FIG-06-01-online-store-order-fulfilment-process": "BPMN process showing order fulfilment inside the Online Store with a message start event.",
    "FIG-06-02-horizon-bank-customer-onboarding-collaboration": "BPMN collaboration showing black-box external participants and Horizon Bank onboarding flow.",
    "FIG-06-03-horizon-bank-payment-repair-exception-process": "BPMN collaboration showing payment repair, correction waiting and timeout handling.",
}


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def escape(value: str | None) -> str:
    return html.escape(value or "", quote=True)


def wrap_text(text: str, width: int) -> list[str]:
    if not text:
        return []
    return textwrap.wrap(text, width=width, break_long_words=False) or [text]


def text_block(
    x: float,
    y: float,
    text: str,
    *,
    anchor: str = "middle",
    css: str = "label",
    width: int = 18,
    line_height: int = 16,
) -> list[str]:
    lines = wrap_text(text, width)
    if not lines:
        return []
    start = y - ((len(lines) - 1) * line_height / 2)
    return [
        f'<text x="{x:.0f}" y="{start + i * line_height:.0f}" text-anchor="{anchor}" class="{css}">{escape(line)}</text>'
        for i, line in enumerate(lines)
    ]


def collect_model(root: ET.Element) -> tuple[dict[str, ET.Element], dict[str, str], set[str]]:
    elements: dict[str, ET.Element] = {}
    lanes: dict[str, str] = {}
    processes_with_lanes: set[str] = set()
    for element in root.iter():
        element_id = element.attrib.get("id")
        if element_id:
            elements[element_id] = element
        if local_name(element.tag) == "lane":
            for ref in element.findall("bpmn:flowNodeRef", NS):
                lanes[ref.text or ""] = element_id or ""
        if local_name(element.tag) == "process" and element.find("bpmn:laneSet", NS) is not None and element_id:
            processes_with_lanes.add(element_id)
    return elements, lanes, processes_with_lanes


def bounds(shape: ET.Element) -> tuple[float, float, float, float]:
    bound = shape.find("dc:Bounds", NS)
    if bound is None:
        raise ValueError(f"{shape.attrib.get('id')}: missing dc:Bounds")
    return tuple(float(bound.attrib[key]) for key in ("x", "y", "width", "height"))  # type: ignore[return-value]


def draw_event(x: float, y: float, w: float, h: float, kind: str, event_defs: list[str]) -> list[str]:
    cx, cy, r = x + w / 2, y + h / 2, min(w, h) / 2
    css = "end" if kind == "endEvent" else "event"
    lines = [f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r:.0f}" class="{css}"/>']
    if kind == "intermediateCatchEvent":
        lines.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{max(r - 5, 6):.0f}" class="innerEvent"/>')
    if "messageEventDefinition" in event_defs:
        ex, ey = cx - 10, cy - 7
        lines.append(f'<rect x="{ex:.0f}" y="{ey:.0f}" width="20" height="14" class="messageIcon"/>')
        lines.append(f'<path d="M{ex:.0f} {ey:.0f} L{cx:.0f} {ey + 8:.0f} L{ex + 20:.0f} {ey:.0f}" class="iconLine"/>')
    if "timerEventDefinition" in event_defs:
        lines.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{max(r - 7, 6):.0f}" class="timerIcon"/>')
        lines.append(f'<path d="M{cx:.0f} {cy:.0f} L{cx:.0f} {cy - 9:.0f} M{cx:.0f} {cy:.0f} L{cx + 8:.0f} {cy + 4:.0f}" class="timerHand"/>')
    return lines


def draw_gateway(x: float, y: float, w: float, h: float, kind: str) -> list[str]:
    cx, cy = x + w / 2, y + h / 2
    points = f"{cx:.0f},{y:.0f} {x + w:.0f},{cy:.0f} {cx:.0f},{y + h:.0f} {x:.0f},{cy:.0f}"
    lines = [f'<polygon points="{points}" class="gateway"/>']
    if kind == "exclusiveGateway":
        lines.append(f'<text x="{cx:.0f}" y="{cy + 5:.0f}" text-anchor="middle" class="gatewayMarker">X</text>')
    elif kind == "eventBasedGateway":
        pentagon = []
        for dx, dy in [(0, -16), (15, -5), (9, 13), (-9, 13), (-15, -5)]:
            pentagon.append(f"{cx + dx:.0f},{cy + dy:.0f}")
        lines.append(f'<polygon points="{" ".join(pentagon)}" class="eventMarker"/>')
        lines.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="9" class="eventMarkerCircle"/>')
    return lines


def render(source: Path, target: Path) -> None:
    tree = ET.parse(source)
    root = tree.getroot()
    elements, lane_membership, processes_with_lanes = collect_model(root)
    shapes = root.findall(".//bpmndi:BPMNShape", NS)
    edges = root.findall(".//bpmndi:BPMNEdge", NS)

    max_x = 0.0
    max_y = 0.0
    shape_bounds: dict[str, tuple[float, float, float, float]] = {}
    for shape in shapes:
        bpmn_id = shape.attrib["bpmnElement"]
        b = bounds(shape)
        shape_bounds[bpmn_id] = b
        max_x = max(max_x, b[0] + b[2])
        max_y = max(max_y, b[1] + b[3])
    for edge in edges:
        for waypoint in edge.findall("di:waypoint", NS):
            max_x = max(max_x, float(waypoint.attrib["x"]))
            max_y = max(max_y, float(waypoint.attrib["y"]))

    width = int(max_x + 40)
    height = int(max_y + 40)
    stem = source.stem
    title = TITLES.get(stem, stem)
    desc = DESCRIPTIONS.get(stem, title)

    out: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f'  <title id="title">{escape(title)}</title>',
        f'  <desc id="desc">{escape(desc)}</desc>',
        "  <defs>",
        '    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#222"/></marker>',
        '    <marker id="msgArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#ffffff" stroke="#6941c6" stroke-width="1.5"/></marker>',
        "    <style>",
        "      .pool { fill:#ffffff; stroke:#222; stroke-width:1.5; }",
        "      .lane { fill:#f7f8fa; stroke:#667085; stroke-width:1; }",
        "      .task { fill:#eef4ff; stroke:#175cd3; stroke-width:1.4; }",
        "      .event { fill:#ffffff; stroke:#222; stroke-width:2; }",
        "      .innerEvent { fill:none; stroke:#222; stroke-width:1.2; }",
        "      .end { fill:#ffffff; stroke:#222; stroke-width:4; }",
        "      .gateway { fill:#fff7e6; stroke:#b54708; stroke-width:1.5; }",
        "      .flow { stroke:#222; stroke-width:1.5; fill:none; marker-end:url(#arrow); }",
        "      .message { stroke:#6941c6; stroke-width:1.7; stroke-dasharray:7 5; fill:none; marker-end:url(#msgArrow); }",
        "      .label { font: 15px Arial, sans-serif; fill:#111827; }",
        "      .small { font: 13px Arial, sans-serif; fill:#344054; }",
        "      .title { font: bold 18px Arial, sans-serif; fill:#111827; }",
        "      .poolText { font: bold 14px Arial, sans-serif; fill:#111827; }",
        "      .labelBadge { fill:#ffffff; stroke:#667085; stroke-width:1; }",
        "      .gatewayMarker { font: 16px Arial, sans-serif; fill:#111827; }",
        "      .eventMarker, .eventMarkerCircle { fill:none; stroke:#111827; stroke-width:1.3; }",
        "      .messageIcon { fill:#ffffff; stroke:#111827; stroke-width:1.2; }",
        "      .iconLine, .timerHand, .timerIcon { fill:none; stroke:#111827; stroke-width:1.2; }",
        "    </style>",
        "  </defs>",
        f'  <text x="{width / 2:.0f}" y="26" text-anchor="middle" class="title">{escape(title)}</text>',
    ]

    participant_labels: list[tuple[float, float, float, float, str, bool]] = []
    for shape in shapes:
        bpmn_id = shape.attrib["bpmnElement"]
        element = elements.get(bpmn_id)
        if element is None:
            continue
        kind = local_name(element.tag)
        x, y, w, h = bounds(shape)
        name = element.attrib.get("name", "")
        if kind == "participant":
            out.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="4" class="pool"/>')
            participant_labels.append((x, y, w, h, name, element.attrib.get("processRef") in processes_with_lanes))
        elif kind == "lane":
            out.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" class="lane"/>')
            out.extend(text_block(x + 22, y + h / 2 - 7, name, anchor="start", css="poolText", width=12, line_height=17))
        elif kind == "task" or kind == "receiveTask":
            out.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="10" class="task"/>')
            out.extend(text_block(x + w / 2, y + h / 2 + 5, name, width=max(12, int(w / 7))))
        elif kind in {"startEvent", "intermediateCatchEvent", "endEvent"}:
            event_defs = [local_name(child.tag) for child in element]
            out.extend(draw_event(x, y, w, h, kind, event_defs))
            label = shape.find("bpmndi:BPMNLabel/dc:Bounds", NS)
            if label is not None and name:
                lx, ly, lw, lh = (float(label.attrib[k]) for k in ("x", "y", "width", "height"))
                out.extend(text_block(lx + lw / 2, ly + max(12, lh / 2), name, css="small", width=max(10, int(lw / 7))))
        elif kind in {"exclusiveGateway", "eventBasedGateway"}:
            out.extend(draw_gateway(x, y, w, h, kind))
            label = shape.find("bpmndi:BPMNLabel/dc:Bounds", NS)
            if label is not None and name:
                lx, ly, lw, lh = (float(label.attrib[k]) for k in ("x", "y", "width", "height"))
                out.extend(text_block(lx + lw / 2, ly + max(12, lh / 2), name, css="small", width=max(10, int(lw / 7))))

    for x, y, w, h, name, contains_lanes in participant_labels:
        if contains_lanes:
            out.append(f'<rect x="{x + 10:.0f}" y="{max(34, y - 24):.0f}" width="{max(92, len(name) * 8 + 20):.0f}" height="22" rx="3" class="labelBadge"/>')
            out.extend(text_block(x + 20, max(49, y - 8), name, anchor="start", css="poolText", width=24, line_height=17))
        else:
            out.extend(text_block(x + 22, y + h / 2 - 7, name, anchor="start", css="poolText", width=18, line_height=17))

    for edge in edges:
        bpmn_id = edge.attrib["bpmnElement"]
        element = elements.get(bpmn_id)
        if element is None:
            continue
        points = [(float(wp.attrib["x"]), float(wp.attrib["y"])) for wp in edge.findall("di:waypoint", NS)]
        if len(points) < 2:
            continue
        path = f"M{points[0][0]:.0f} {points[0][1]:.0f} " + " ".join(f"L{x:.0f} {y:.0f}" for x, y in points[1:])
        kind = local_name(element.tag)
        css = "message" if kind == "messageFlow" else "flow"
        out.append(f'<path d="{path}" class="{css}"/>')
        name = element.attrib.get("name", "")
        label = edge.find("bpmndi:BPMNLabel/dc:Bounds", NS)
        if label is not None and name:
            lx, ly, lw, lh = (float(label.attrib[k]) for k in ("x", "y", "width", "height"))
            out.extend(text_block(lx + lw / 2, ly + max(12, lh / 2), f"[{name}]" if kind == "sequenceFlow" else name, css="small", width=max(8, int(lw / 7))))

    out.append("</svg>")
    target.write_text("\n".join(out) + "\n", encoding="utf-8")


def main() -> int:
    sources = [Path(arg) for arg in sys.argv[1:]]
    if not sources:
        sources = sorted((ROOT / "diagrams/source/bpmn").glob("FIG-06-*.bpmn"))
    for source in sources:
        source = source if source.is_absolute() else ROOT / source
        target = ROOT / "diagrams/exported/svg" / f"{source.stem}.svg"
        render(source, target)
        print(f"Rendered {target.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
