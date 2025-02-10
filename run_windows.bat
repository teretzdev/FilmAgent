@echo off
setlocal enabledelayedexpansion

:: Ensure we start with no active environment
call conda deactivate

:: Start TTS service
echo Starting TTS service...
start cmd /k "call conda activate tts && cd TTS && python tts_main.py"
timeout /t 5

:: Start FilmAgent
echo Starting FilmAgent...
start cmd /k "call conda activate filmagent && cd FilmAgent && python main.py"
timeout /t 5

:: Start React client
echo Starting React client...
start cmd /k "cd client && npm start"

echo All services started successfully!
echo TTS service: http://localhost:8080
echo FilmAgent service: http://localhost:8000
echo React client: http://localhost:3000

exit /b 0