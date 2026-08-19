# Telemetria de Amostras

Este diretório contém amostras de telemetria em JSON normalizado utilizadas pelo Detection Engine.

As amostras representam eventos process_creation do Windows associados a atividades suspeitas e benignas.

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

Essas amostras permitem testar tanto comportamentos esperados de detecção quanto atividades benignas de PowerShell.

### LOLBins

O projeto também contém telemetria para:

* Certutil
* Mshta
* Regsvr32

Essas amostras são utilizadas para validar detecções Sigma relacionadas a LOLBins.

## Fluxo de Detecção

A telemetria é consumida pelo Detection Engine em Python:

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

O comportamento esperado é a identificação de uma ou mais detecções relacionadas à atividade de PowerShell codificado.

## Design

Os arquivos de telemetria são intencionalmente pequenos e determinísticos.

Eles existem para fornecer entradas de teste reproduzíveis para o pipeline de detecção e não têm como objetivo funcionar como um sistema completo de coleta de eventos do Windows.
