@echo off
setlocal enabledelayedexpansion

:: Generate a unique container name per session
for /f %%a in ('powershell -command "[guid]::NewGuid().ToString()"') do set "USER_CONTAINER=ctf_%%a"

:: Start a new disposable container for the SSH session
echo Launching new container: %USER_CONTAINER%
docker run --rm -it --name %USER_CONTAINER% -p 22:22 ctf_challenge

endlocal
