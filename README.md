# DevSecOps Detection Lab

Laboratório de **Detection as Code** focado no desenvolvimento, validação e testes de detecções de segurança utilizando **Sigma, YARA, Python, telemetria simulada e Docker**.

O projeto demonstra um fluxo simplificado de DevSecOps aplicado à engenharia de detecções de segurança:

Telemetria Simulada
        │
        ▼
Normalização de Telemetria
        │
        ▼
Motor de Detecção
   ┌────┴────┐
   ▼         ▼
 Sigma      YARA
   │         │
   └────┬────┘
        ▼
 Resultado de Detecção
        │
        ▼
 Validação Automatizada
        │
        ▼
 Docker / CI

## Objetivos

* Desenvolver detecções de segurança como código.
* Validar regras Sigma automaticamente.
* Testar detecções contra telemetria simulada de processos Windows.
* Manter regras de detecção versionadas no Git.
* Executar o pipeline de validação localmente e via Docker.
* Demonstrar um fluxo reproduzível de Detection as Code.

## Tecnologias

* Python 3.12
* Sigma
* YARA
* PyYAML
* pytest
* Docker
* Docker Compose
* GitHub Actions

## Cobertura de Detecções

O laboratório atualmente contém detecções para execução no Windows e atividades relacionadas a LOLBins, incluindo:

* PowerShell codificado (Encoded PowerShell)
* Execução de PowerShell
* Download via PowerShell
* PowerShell WebClient
* Download via Certutil
* Execução via Mshta
* Execução via Regsvr32
* Execução via Rundll32
* Execução via WMIC
* Download via Bitsadmin

O YARA também é utilizado para validar padrões suspeitos de payloads PowerShell.

## Estrutura do Projeto

DevSecOps_Detection_Lab/
│
├── config/
│   └── lab.yml
│
├── detections/
│   ├── sigma/
│   └── yara/
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── docs/
│   └── architecture/
│       └── architecture.md
│
├── python/
│   ├── engine/
│   ├── normalizers/
│   ├── validators/
│   ├── tests/
│   └── runner.py
│
├── simulations/
│   ├── certutil/
│   ├── mshta/
│   ├── powershell/
│   └── regsvr32/
│
├── telemetry/
│   └── samples/
│
├── Makefile
├── requirements.txt
└── README.md

## Requisitos

Para execução local:

* Python 3.12+
* pip
* Sigma CLI
* YARA
* GNU Make

Para execução em container:

* Docker
* Docker Compose

## Configuração Local

Criar e ativar ambiente virtual:

python3 -m venv .venv
source .venv/bin/activate

Instalar dependências:

pip install -r requirements.txt

## Validar Regras Sigma

Executar:

make validate

Ou diretamente:

sigma check detections/sigma/*.yml

Resultado esperado:

Found 0 errors, 0 condition errors and 0 issues.
No rule errors found.
No condition errors found.
No validation issues found.

## Executar Pipeline de Detecção

Executar o pipeline completo:

make test

O pipeline valida:

1. Regras Sigma
2. Estrutura das detecções
3. Testes Python
4. Regras YARA

Resultado esperado:

Detection Pipeline: PASS

## Testar uma Telemetria Específica

Exemplo:

make detect FILE=telemetry/samples/powershell/encoded_command.json

O motor de detecção deve identificar a atividade simulada de PowerShell codificado e gerar o resultado correspondente.

Outros exemplos disponíveis:

telemetry/samples/powershell/benign_command.json
telemetry/samples/powershell/download_activity.json
telemetry/samples/powershell/encoded_command.json
telemetry/samples/certutil_download.json
telemetry/samples/mshta_remote.json
telemetry/samples/regsvr32_remote.json

## Docker

Build do container:

docker compose -f docker/docker-compose.yml build

Executar pipeline completo:

make docker-test

Isso executa o mesmo pipeline de validação dentro de um ambiente Docker reproduzível com Python e YARA.

Resultado esperado:

Detection Pipeline: PASS

Executar uma detecção específica via Docker:

docker compose -f docker/docker-compose.yml run --rm \
    detection-lab \
    python -m python.engine.detection_engine \
    telemetry/samples/powershell/encoded_command.json

## Testes Automatizados

O projeto contém testes Python para:

python/tests/test_sigma_detection.py
python/tests/test_validate_sigma.py
python/tests/test_yara_detection.py

O mesmo fluxo de validação também é utilizado no pipeline de CI.

## Fluxo de Engenharia de Detecção

Novas detecções seguem o fluxo:

Criar Detecção
      │
      ▼
Regra Sigma/YARA
      │
      ▼
Telemetria Simulada
      │
      ▼
Teste Automatizado
      │
      ▼
Validação
      │
      ▼
Commit no Git
      │
      ▼
Pipeline de CI

Isso permite que regras de detecção sejam versionadas, revisadas e validadas automaticamente como código de aplicação.

## Escopo

Este repositório é intencionalmente focado no ciclo de vida da engenharia de detecções.

Ele não implementa um SIEM completo, SOC ou plataforma de monitoramento de segurança em produção.

O objetivo é demonstrar os princípios centrais de **Detection as Code e DevSecOps aplicado à engenharia de detecções de segurança**.

## Autor

**Fernando Bahia**

Infraestrutura de TI | Cyber Security | Cloud | DevSecOps
