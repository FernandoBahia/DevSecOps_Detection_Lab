rule Suspicious_PowerShell_Payload
{
    meta:
        description = "Detects suspicious PowerShell-related payload characteristics"
        author = "Fernando Bahia"
        date = "2026-08-18"
        severity = "medium"
        technique = "T1059.001"

    strings:
        $powershell = "powershell" ascii nocase
        $encoded = "-enc" ascii nocase
        $encoded_long = "-encodedcommand" ascii nocase
        $iex = "Invoke-Expression" ascii nocase
        $download = "Invoke-WebRequest" ascii nocase

    condition:
        $powershell and 2 of ($encoded, $encoded_long, $iex, $download)
}
