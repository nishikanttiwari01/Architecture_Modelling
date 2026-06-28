param(
    [switch]$Required
)

$ErrorActionPreference = "Stop"

& "$PSScriptRoot/render-plantuml.ps1" -Required:$Required
& "$PSScriptRoot/render-mermaid.ps1" -Required:$Required

Write-Host "Diagram rendering pass complete."
