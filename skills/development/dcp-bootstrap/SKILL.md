---
name: dcp-bootstrap
description: >-
  Instala dependências da Dev Context Platform (Python, pip, Roslyn) e executa
  o CLI scan. Use quando scan falhar por Python ausente, no primeiro uso da DCP,
  ou quando o usuário pedir setup/bootstrap da plataforma de contexto.
---

# DCP Bootstrap

## Objetivo

Garantir que a **Dev Context Platform** está pronta para rodar: Python 3.10+, venv, PyYAML, Roslyn indexer (.NET 8), e smoke test do `scan.py`.

Esta skill é invocada **antes** de [project-scanner](project-scanner/SKILL.md) ou [us-implementation-planner](us-implementation-planner/SKILL.md) quando o ambiente não está configurado.

## Quando usar

* `python` / `pip` não encontrados no PATH
* Primeiro uso da DCP no projeto ou máquina nova
* Usuário pede *"instalar o necessário e rodar o scan"*
* `scan verify` ou `scan sync` falhou por dependência

## Regra

**Não pedir ao usuário para instalar manualmente** — executar os scripts de bootstrap via Shell e reportar o resultado.

---

## Fluxo

### Etapa 1 — Detectar SO

| SO | Bootstrap | Wrapper |
| --- | --- | --- |
| Windows | `project-context/scripts/bootstrap.ps1` | `project-context/scripts/dcp.ps1` |
| macOS / Linux | `project-context/scripts/bootstrap.sh` | `project-context/scripts/dcp.sh` |

Executar a partir da raiz do engineering-playbook.

### Etapa 2 — Bootstrap

**Windows (PowerShell):**

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
.\project-context\scripts\bootstrap.ps1
```

Instala Python via **winget** se ausente, cria `.venv`, instala `requirements.txt`, compila Roslyn se `dotnet` disponível.

**Unix:**

```bash
chmod +x project-context/scripts/bootstrap.sh project-context/scripts/dcp.sh
./project-context/scripts/bootstrap.sh
```

### Etapa 3 — Executar comando DCP

Repassar argumentos do usuário via wrapper (não chamar `python scan.py` direto):

```powershell
.\project-context\scripts\dcp.ps1 status --project AtivosCompraMobilizacao
.\project-context\scripts\dcp.ps1 init --project AtivosCompraMobilizacao --discover-ado
.\project-context\scripts\dcp.ps1 verify --project AtivosCompraMobilizacao --branch main --repo sima-backend
```

```bash
./project-context/scripts/dcp.sh sync --project AtivosCompraMobilizacao
```

### Etapa 4 — Handoff

Após bootstrap OK → continuar com [project-scanner](project-scanner/SKILL.md) ou [us-implementation-planner](us-implementation-planner/SKILL.md).

---

## Falhas comuns

| Erro | Ação |
| --- | --- |
| winget indisponível | Orientar instalação manual Python 3.10+ e reexecutar bootstrap |
| dotnet ausente | Avisar: scan leve OK; indexer Roslyn desabilitado |
| git ausente | Instalar Git; obrigatório para sync/verify |
| `local_path` null no project-map | Editar `project-map.yaml` com caminho do clone |

## Artefatos gerados (gitignore)

```text
project-context/scripts/.venv/
project-context/scripts/.python-path
```

Não commitar venv.
