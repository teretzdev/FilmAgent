@echo off
setlocal enabledelayedexpansion

echo Starting FilmAgent Setup...

:: Check Python version
python --version | findstr "3.9.18" >nul
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python 3.9.18 is required
    exit /b 1
)

:: Check Node.js
node --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Error: Node.js is required
    exit /b 1
)

:: Setup FilmAgent environment
echo Setting up FilmAgent environment...
conda create -n filmagent python=3.9.18 -y
call conda activate filmagent
pip install -r FilmAgent/env.txt
if %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to install FilmAgent dependencies
    exit /b 1
)

:: Setup TTS environment
echo Setting up TTS environment...
conda create -n tts python=3.9.18 -y
call conda activate tts
pip install -r TTS/env_tts.txt
if %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to install TTS dependencies
    exit /b 1
)

:: Setup React client
echo Setting up React client...
cd client
call npm install
if %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to install React dependencies
    exit /b 1
)
cd ..

:: Create required directories
mkdir FilmAgent\Logs 2>nul
mkdir FilmAgent\Script 2>nul

echo Setup completed successfully!
echo Please ensure you have configured your OpenAI API key in LLMCaller.py
exit /b 0