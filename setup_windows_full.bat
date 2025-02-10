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
call conda env remove -n tts -y 2>nul
call conda create -n tts python=3.9.18 -y

:: Activate TTS environment
call conda activate tts
if %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to activate TTS environment
    exit /b 1
)

:: Install core TTS dependencies
echo Installing core TTS dependencies...
pip install -r TTS/env_tts.txt --no-deps
pip install torch==2.1.0 torchaudio==2.1.0 --index-url https://download.pytorch.org/whl/cpu

:: Try installing optional GPU dependencies
echo Attempting to install GPU dependencies...
pip install torch==2.1.0 torchaudio==2.1.0 --index-url https://download.pytorch.org/whl/cu118 --no-deps || (
    echo GPU dependencies installation failed - falling back to CPU only mode
)

:: Deactivate before setting up FilmAgent
call conda deactivate

:: Setup FilmAgent environment
echo Setting up FilmAgent environment...
call conda env remove -n filmagent -y 2>nul
call conda create -n filmagent python=3.9.18 -y
call conda activate filmagent
pip install -r FilmAgent/env.txt

:: Setup React client
echo Setting up React client...
cd client
call npm install
cd ..

:: Create required directories
mkdir FilmAgent\Logs 2>nul
mkdir FilmAgent\Script 2>nul

echo Setup completed successfully!
echo Note: TTS is running in CPU mode. For GPU support, please install CUDA and cuDNN manually.
exit /b 0