@echo off
setlocal enabledelayedexpansion

:: Start TTS service
echo Starting TTS service...
start cmd /k "conda activate tts && cd TTS && python tts_main.py"
timeout /t 5

:: Start FilmAgent
echo Starting FilmAgent...
start cmd /k "conda activate filmagent && cd FilmAgent && python main.py"
timeout /t 5

:: Start React client
echo Starting React client...
start cmd /k "cd client && npm start"

echo All services started successfully!
echo TTS service: http://localhost:8080
echo React client: http://localhost:3000

exit /b 0