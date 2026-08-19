# Telemetria de Amostras

Este diretório contém amostras de telemetria em JSON normalizado utilizadas pelo Detection Engine.

As amostras representam eventos de process_creation do Windows associados a atividades tanto suspeitas quanto benignas.

## Estrutura

telemetry/
├── README.md
└── samples/
    ├── certutil_download.json
    ├── mshta_remote.json
    ├── regsvr32_remote.json
    └── powershell/
        ├── benign_command.json
        ├── download_activity.json
        └── encoded_command.json

## Categorias de Amostras

### PowerShell

powershell/benign_command.json
powershell/download_activity.json
powershell/encoded_command.json

Essas amostras permitem que o projeto teste tanto detecções esperadas quanto comportamentos benignos do PowerShell.

### LOLBins

O projeto também contém telemetria para:

* Certutil
* Mshta
* Regsvr32

Essas amostras são utilizadas para validar detecções Sigma relacionadas a LOLBins.

## Fluxo de Detecção

A telemetria é consumida pelo engine de detecção em Python:

JSON de Telemetria
      ↓
Normalização
      ↓
Detection Engine
      ↓
Regras Sigma
      ↓
Resultado de Detecção

## Exemplo

Executar a amostra de PowerShell codificado:

make detect FILE=telemetry/samples/powershell/encoded_command.json

O comportamento esperado é a identificação de uma detecção relacionada à regra de PowerShell codificado.

## Design

Os arquivos de telemetria são intencionalmente pequenos e determinísticos.

Eles existem para fornecer entradas de teste reproduzíveis para o pipeline de detecção, e não para funcionar como um sistema completo de coleta de eventos do Windows.
