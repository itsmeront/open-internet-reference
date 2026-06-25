@echo off
setlocal

cd /d "%~dp0"

if exist ".venv\Scripts\python.exe" (
  ".venv\Scripts\python.exe" tools\serve.py %*
) else (
  python tools\serve.py %*
)

endlocal
