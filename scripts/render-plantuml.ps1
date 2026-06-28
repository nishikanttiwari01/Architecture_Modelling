param(
    [string]$InputPath = "diagrams/source/plantuml",
    [string]$OutputPath = "diagrams/exported/svg",
    [switch]$Required
)

$ErrorActionPreference = "Stop"

function Resolve-Renderer {
    $plantuml = Get-Command plantuml -ErrorAction SilentlyContinue
    if ($plantuml) {
        return @($plantuml.Source)
    }

    $jarCandidates = @(
        "tools/plantuml/plantuml.jar",
        "$env:USERPROFILE/.vscode/extensions/jebbs.plantuml*/plantuml.jar"
    )

    foreach ($candidate in $jarCandidates) {
        $matches = Get-ChildItem -Path $candidate -ErrorAction SilentlyContinue | Sort-Object FullName -Descending
        if ($matches) {
            $java = Get-Command java -ErrorAction SilentlyContinue
            if ($java) {
                return @($java.Source, "-jar", $matches[0].FullName)
            }
        }
    }

    return $null
}

$source = Resolve-Path -Path $InputPath -ErrorAction SilentlyContinue
if (-not $source) {
    if ($Required) { throw "PlantUML input path not found: $InputPath" }
    Write-Host "PlantUML input path not found, skipping: $InputPath"
    exit 0
}

$files = @()
$item = Get-Item -LiteralPath $source
if ($item.PSIsContainer) {
    $files = @(Get-ChildItem -LiteralPath $item.FullName -Recurse -Filter *.puml)
} else {
    $files = @($item)
}

if ($files.Count -eq 0) {
    Write-Host "No PlantUML files found under $InputPath."
    exit 0
}

$renderer = Resolve-Renderer
if (-not $renderer) {
    if ($Required) { throw "PlantUML renderer not found. Install PlantUML CLI or configure the VS Code PlantUML extension." }
    Write-Host "PlantUML renderer not found, skipping render."
    exit 0
}

New-Item -ItemType Directory -Force -Path $OutputPath | Out-Null

foreach ($file in $files) {
    Write-Host "Rendering PlantUML: $($file.FullName)"
    if ($renderer.Count -eq 1) {
        & $renderer[0] -tsvg -o (Resolve-Path $OutputPath).Path $file.FullName
    } else {
        & $renderer[0] $renderer[1] $renderer[2] -tsvg -o (Resolve-Path $OutputPath).Path $file.FullName
    }
    if ($LASTEXITCODE -ne 0) {
        throw "PlantUML render failed for $($file.FullName)"
    }
}

Write-Host "PlantUML rendering complete."
