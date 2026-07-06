#!/usr/bin/env pwsh
# Dev Context Platform — bootstrap (Windows)
# Instala Python (winget), dependências pip e compila Roslyn indexer.

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$PlaybookRoot = Resolve-Path (Join-Path $ScriptDir "..\..")
$Requirements = Join-Path $ScriptDir "requirements.txt"
$RoslynProject = Join-Path $ScriptDir "indexers\roslyn\RoslynIndexer\RoslynIndexer.csproj"
$VenvDir = Join-Path $ScriptDir ".venv"

function Find-Python {
    $candidates = @(
        { & python -c "import sys; print(sys.executable)" 2>$null },
        { & python3 -c "import sys; print(sys.executable)" 2>$null },
        { & py -3 -c "import sys; print(sys.executable)" 2>$null }
    )
    foreach ($try in $candidates) {
        try {
            $path = & $try
            if ($path -and (Test-Path $path)) { return $path.Trim() }
        } catch { }
    }
    return $null
}

function Install-PythonWinget {
    Write-Host "Python não encontrado. Instalando via winget..."
    if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
        throw "winget não disponível. Instale Python 3.10+ manualmente: https://www.python.org/downloads/"
    }
    winget install Python.Python.3.12 --accept-package-agreements --accept-source-agreements --silent
    # Refresh PATH for current session
    $machinePath = [Environment]::GetEnvironmentVariable("Path", "Machine")
    $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
    $env:Path = "$machinePath;$userPath"
    Start-Sleep -Seconds 3
}

function Ensure-Venv {
    param([string]$PythonExe)
    if (-not (Test-Path $VenvDir)) {
        Write-Host "Criando venv em $VenvDir ..."
        & $PythonExe -m venv $VenvDir
    }
    if ($IsWindows -or $env:OS -match "Windows") {
        return Join-Path $VenvDir "Scripts\python.exe"
    }
    return Join-Path $VenvDir "bin\python"
}

Write-Host "=== DCP Bootstrap ===" -ForegroundColor Cyan

$python = Find-Python
if (-not $python) {
    Install-PythonWinget
    $python = Find-Python
}
if (-not $python) {
    throw "Python ainda não encontrado após instalação. Reinicie o terminal ou instale manualmente."
}

Write-Host "Python: $python" -ForegroundColor Green
$venvPython = Ensure-Venv -PythonExe $python

Write-Host "Instalando dependências pip..."
& $venvPython -m pip install --upgrade pip -q
& $venvPython -m pip install -r $Requirements -q

if (Get-Command dotnet -ErrorAction SilentlyContinue) {
    if (Test-Path $RoslynProject) {
        Write-Host "Compilando Roslyn indexer..."
        dotnet build $RoslynProject -v q --nologo
        if ($LASTEXITCODE -ne 0) { Write-Warning "Roslyn indexer falhou — scan C# usará fallback regex." }
    }
} else {
    Write-Warning "dotnet não encontrado — indexer Roslyn indisponível (scan leve OK)."
}

# Smoke test
Write-Host "Verificando scan CLI..."
& $venvPython (Join-Path $ScriptDir "scan.py") --help | Out-Null
if ($LASTEXITCODE -ne 0) { throw "scan.py --help falhou" }

Write-Host ""
Write-Host "Bootstrap concluído." -ForegroundColor Green
Write-Host "Use: .\project-context\scripts\dcp.ps1 status --project AtivosCompraMobilizacao"
Write-Host "Python do venv: $venvPython"

# Export path hint for parent scripts
Set-Content -Path (Join-Path $ScriptDir ".python-path") -Value $venvPython -NoNewline
