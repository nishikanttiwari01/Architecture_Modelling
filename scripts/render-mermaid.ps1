param(
    [string]$InputPath = "diagrams/source/mermaid",
    [string]$OutputPath = "diagrams/exported/svg",
    [switch]$Required
)

$ErrorActionPreference = "Stop"

$source = Resolve-Path -Path $InputPath -ErrorAction SilentlyContinue
if (-not $source) {
    if ($Required) { throw "Mermaid input path not found: $InputPath" }
    Write-Host "Mermaid input path not found, skipping: $InputPath"
    exit 0
}

$item = Get-Item -LiteralPath $source
if ($item.PSIsContainer) {
    $files = @(Get-ChildItem -LiteralPath $item.FullName -Recurse -Filter *.mmd)
} else {
    $files = @($item)
}

if ($files.Count -eq 0) {
    Write-Host "No Mermaid files found under $InputPath."
    exit 0
}

$mmdc = Get-Command mmdc -ErrorAction SilentlyContinue
$npx = Get-Command npx -ErrorAction SilentlyContinue
if (-not $mmdc -and -not $npx) {
    if ($Required) { throw "Mermaid renderer not found. Install @mermaid-js/mermaid-cli or provide mmdc on PATH." }
    Write-Host "Mermaid renderer not found, skipping render."
    exit 0
}

New-Item -ItemType Directory -Force -Path $OutputPath | Out-Null

foreach ($file in $files) {
    $outFile = Join-Path $OutputPath ($file.BaseName + ".svg")
    Write-Host "Rendering Mermaid: $($file.FullName)"
    if ($mmdc) {
        & $mmdc.Source -i $file.FullName -o $outFile
    } else {
        & $npx.Source mmdc -i $file.FullName -o $outFile
    }
    if ($LASTEXITCODE -ne 0) {
        throw "Mermaid render failed for $($file.FullName)"
    }
}

Write-Host "Mermaid rendering complete."
