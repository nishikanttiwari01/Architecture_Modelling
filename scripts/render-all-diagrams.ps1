param(
    [switch]$Required
)

$ErrorActionPreference = "Stop"

& "$PSScriptRoot/render-plantuml.ps1" -Required:$Required
& "$PSScriptRoot/render-mermaid.ps1" -Required:$Required

# Draw.io figures are rendered from their editable mxGraph source by a Python
# renderer (see DEC-021). Its exit code is not suppressed: a render failure must
# fail this script.
Write-Host "Rendering Draw.io diagrams: $PSScriptRoot/render-drawio-diagrams.py"
python "$PSScriptRoot/render-drawio-diagrams.py"
if ($LASTEXITCODE -ne 0) {
    throw "Draw.io renderer failed with exit code $LASTEXITCODE"
}

Write-Host "Diagram rendering pass complete."
