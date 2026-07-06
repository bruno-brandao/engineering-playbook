#!/usr/bin/env pwsh
# Wrapper DCP — bootstrap (se necessário) + scan.py

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$PythonPathFile = Join-Path $ScriptDir ".python-path"
$VenvPython = Join-Path $ScriptDir ".venv\Scripts\python.exe"

function Get-DcpPython {
    if (Test-Path $PythonPathFile) {
        $p = Get-Content $PythonPathFile -Raw
        if ($p -and (Test-Path $p.Trim())) { return $p.Trim() }
    }
    if (Test-Path $VenvPython) { return $VenvPython }
    foreach ($cmd in @("python", "python3", "py -3")) {
        try {
            $exe = Invoke-Expression "$cmd -c `"import sys; print(sys.executable)`"" 2>$null
            if ($exe -and (Test-Path $exe)) { return $exe.Trim() }
        } catch { }
    }
    return $null
}

$python = Get-DcpPython
if (-not $python) {
    Write-Host "Bootstrap necessário..."
    & (Join-Path $ScriptDir "bootstrap.ps1")
    $python = Get-Content $PythonPathFile -Raw
    $python = $python.Trim()
}

if ($args.Count -eq 0) {
    & $python (Join-Path $ScriptDir "scan.py") --help
    exit $LASTEXITCODE
}

& $python (Join-Path $ScriptDir "scan.py") @args
exit $LASTEXITCODE
