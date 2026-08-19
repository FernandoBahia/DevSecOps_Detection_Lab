# DevSecOps Detection Lab

Laboratório de Detection Engineering e DevSecOps focado em
detecção baseada em comportamento, testes automatizados e
validação contínua de regras de segurança.

## Objetivos

- Criar regras Sigma
- Simular eventos de segurança
- Validar detecções automaticamente
- Testar regras com Python
- Utilizar YARA para detecção baseada em conteúdo
- Integrar validações ao GitHub Actions

## Architecture

Telemetry
   ↓
Detection Engine
   ↓
Sigma / YARA
   ↓
Detection Match
   ↓
Automated Tests
   ↓
GitHub Actions

## Detection Coverage

- Suspicious PowerShell execution
- Encoded PowerShell
- PowerShell download activity
- Certutil download activity
- Mshta remote execution
- Regsvr32 remote scriptlet execution

## Running

```bash
source .venv/bin/activate

pytest -q

python -m python.runner