@echo off
setlocal
cd /d "%~dp0"

set "TARGET=%~1"
if "%TARGET%"=="" (
  docker compose run --rm latex
) else (
  docker compose run --rm latex bash -lc "bash tools/build.sh %TARGET%"
)

exit /b %ERRORLEVEL%
