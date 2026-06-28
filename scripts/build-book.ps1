param(
    [string]$OutputDirectory = "build",
    [switch]$UsePandoc
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot
$PythonBuilder = Join-Path $PSScriptRoot "build-book.py"

python $PythonBuilder --output-directory $OutputDirectory
if ($LASTEXITCODE -ne 0) {
    throw "The Markdown build failed with exit code $LASTEXITCODE."
}

$BuildDir = if ([System.IO.Path]::IsPathRooted($OutputDirectory)) {
    $OutputDirectory
} else {
    Join-Path $RepoRoot $OutputDirectory
}
$Combined = Join-Path $BuildDir "architecture-modelling-handbook.md"

if ($UsePandoc) {
    if (-not (Get-Command pandoc -ErrorAction SilentlyContinue)) {
        throw "Pandoc was requested but is not installed or not on PATH."
    }
    $Docx = Join-Path $BuildDir "architecture-modelling-handbook.docx"
    pandoc $Combined -o $Docx --toc
    if ($LASTEXITCODE -ne 0) {
        throw "Pandoc failed with exit code $LASTEXITCODE."
    }
    Write-Host "DOCX created: $Docx"
}
