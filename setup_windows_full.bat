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

:: Setup TTS environment first
echo Setting up TTS environment...
call conda deactivate
call conda env remove -n tts -y
call conda create -n tts python=3.9.18 -y
if %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to create TTS environment
    exit /b 1
)

:: Activate and install TTS dependencies
call conda activate tts
if %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to activate TTS environment
    exit /b 1
)

:: Install basic requirements first
pip install fastapi uvicorn
if %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to install basic TTS dependencies
    exit /b 1
)

:: Install remaining TTS requirements
pip install -r TTS\env_tts.txt
if %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to install TTS dependencies
    exit /b 1
)

:: Deactivate before setting up FilmAgent
call conda deactivate

:: Setup FilmAgent environment
echo Setting up FilmAgent environment...
call conda env remove -n filmagent -y
call conda create -n filmagent python=3.9.18 -y
call conda activate filmagent
pip install -r FilmAgent\env.txt
if %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to install FilmAgent dependencies
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

:: Verify environments
call conda env list | findstr "tts"
if %ERRORLEVEL% NEQ 0 (
    echo Error: TTS environment not properly created
    exit /b 1
)

call conda env list | findstr "filmagent"
if %ERRORLEVEL% NEQ 0 (
    echo Error: FilmAgent environment not properly created
    exit /b 1
)

echo Setup completed successfully!
echo Please ensure you have configured your OpenAI API key in LLMCaller.py
exit /b 0