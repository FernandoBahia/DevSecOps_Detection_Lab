# Simulações de Detecção

Este diretório contém scripts de simulação controlados usados para representar cenários correspondentes às regras de detecção.

Os scripts são **artefatos de simulação** e não têm a intenção de representar cadeias completas de ataque.

## Estrutura

simulations/
├── certutil/
│   └── download.ps1
├── mshta/
│   └── remote_hta.ps1
├── powershell/
│   ├── download_activity.ps1
│   └── encoded_command.ps1
└── regsvr32/
    └── remote_scriptlet.ps1

## Simulações disponíveis

| Simulação                          | Finalidade                                    |
| ---------------------------------- | --------------------------------------------- |
| powershell/encoded_command.ps1     | Simula execução de PowerShell codificado      |
| powershell/download_activity.ps1   | Simula atividade de download via PowerShell   |
| certutil/download.ps1              | Simula comportamento de download via Certutil |
| mshta/remote_hta.ps1               | Simula execução via Mshta                     |
| regsvr32/remote_scriptlet.ps1      | Simula execução de scriptlet via Regsvr32     |

## Telemetria

As simulações são representadas no projeto por amostras de telemetria em JSON localizadas em:

telemetry/samples/


O Detection Engine opera sobre essas amostras de telemetria, em vez de exigir a execução dos scripts de simulação.

## Propósito

A camada de simulação fornece casos de teste reproduzíveis para engenharia de detecção.

Cada cenário pode ser associado ao seguinte fluxo:

Simulação
    ↓
Telemetria
    ↓
Regra de Detecção
    ↓
Detection Engine
    ↓
Resultado Esperado

O projeto utiliza essa abordagem para testar a lógica de detecção sem a necessidade de um ambiente Windows real de ataque.
