# DevSecOps Detection Lab

## Visão Geral

O **DevSecOps Detection Lab** é um laboratório de **Detection as Code** desenvolvido para demonstrar o ciclo de desenvolvimento, validação e testes automatizados de detecções de segurança.

O projeto utiliza **Sigma, YARA, Python, telemetria simulada, Docker, Git e GitHub Actions** para implementar um fluxo reproduzível de engenharia de detecção.

## Arquitetura

                    ┌──────────────────────┐
                    │   Regras de Detecção │
                    │                      │
                    │     Sigma + YARA     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Telemetria Simulada  │
                    │        JSON          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Detection Engine    │
                    │       Python         │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
        ┌───────────┐    ┌───────────┐    ┌───────────┐
        │ Sigma CLI │    │  Pytest   │    │   YARA    │
        └─────┬─────┘    └─────┬─────┘    └─────┬─────┘
              │                │                │
              └────────────────┼────────────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Automated Validation │
                    │   Python Runner      │
                    └──────────┬───────────┘
                               │
                    ┌──────────┴───────────┐
                    │                      │
                    ▼                      ▼
             ┌────────────┐       ┌────────────────┐
             │   Docker   │       │ GitHub Actions │
             └─────┬──────┘       └───────┬────────┘
                   │                      │
                   └──────────┬───────────┘
                              ▼
                       ┌─────────────┐
                       │ PASS / FAIL │
                       └─────────────┘

## Componentes

### Detection Rules

As regras de detecção são armazenadas no diretório detections/.

detections/
├── sigma/
└── yara/


As regras Sigma são utilizadas para identificar comportamentos suspeitos presentes na telemetria de processos.

As regras YARA são utilizadas para identificar padrões associados a payloads suspeitos.

### Telemetria

A telemetria utilizada pelo laboratório é representada por arquivos JSON determinísticos.

telemetry/
└── samples/

As amostras representam eventos process_creation associados a comportamentos benignos ou suspeitos.

Isso permite executar testes reproduzíveis sem depender de um endpoint Windows real.

### Detection Engine

O motor de detecção está implementado em Python:

python/
└── engine/
    └── detection_engine.py

O engine recebe uma amostra de telemetria, normaliza os dados necessários e verifica correspondência com as regras de detecção disponíveis.

### Validators

Os validadores estão localizados em:

python/
└── validators/

Eles são utilizados para verificar a estrutura e a consistência das detecções antes da execução do pipeline.

### Automated Tests

Os testes automatizados estão localizados em:

python/
└── tests/

O projeto possui testes para:

* Detecções Sigma
* Validação das regras Sigma
* Detecções YARA

O runner.py integra essas validações em um único pipeline.

### Docker

O Docker fornece um ambiente reproduzível para execução do pipeline.

docker/
├── Dockerfile
└── docker-compose.yml

O comando:

make docker-test

executa o pipeline dentro do container.

### Makefile

O Makefile fornece uma interface simplificada para as operações mais importantes do laboratório:

make validate
make test
make docker-test
make detect FILE=<arquivo>
make clean

Isso padroniza a execução das tarefas de desenvolvimento e validação.

### GitHub Actions

O projeto utiliza GitHub Actions para executar automaticamente as validações quando alterações são enviadas ao repositório ou quando um Pull Request é aberto.

O pipeline de CI executa as principais validações do projeto:

Commit / Pull Request
        │
        ▼
GitHub Actions
        │
        ├── Sigma validation
        ├── Detection structure validation
        ├── Python tests
        ├── YARA validation
        └── Detection pipeline
        │
        ▼
     PASS / FAIL


## Fluxo de Detection as Code

O ciclo de desenvolvimento de uma nova detecção segue o fluxo:

Criar Detecção
      │
      ▼
Regra Sigma / YARA
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
GitHub Actions
      │
      ▼
PASS / FAIL
```

Esse modelo permite tratar regras de segurança como artefatos de software, sujeitos a versionamento, validação, testes e integração contínua.

## Tecnologias

* Python
* Sigma
* YARA
* PyYAML
* pytest
* Docker
* Docker Compose
* GNU Make
* Git
* GitHub Actions

## Escopo

O projeto é focado no ciclo de vida da **engenharia de detecções**.

O laboratório não representa uma implementação completa de SIEM, SOC ou plataforma de monitoramento de segurança em produção.

Seu objetivo é demonstrar, de forma prática e reproduzível, os princípios de **Detection as Code e DevSecOps aplicados à engenharia de detecções de segurança**.
