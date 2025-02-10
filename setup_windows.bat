@echo off
:: setup_windows.bat - Automates the setup and startup of the FilmAgent project on Windows.

:: Step 1: Check if Conda is installed
echo Checking for Conda installation...
conda --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Error: Conda is not installed or not added to PATH.
    echo Please install Conda and ensure it is accessible from the command line.
    exit /b 1
)

:: Step 2: Check if the 'filmagent' environment already exists
echo Checking for existing Conda environment 'filmagent'...
conda env list | findstr "filmagent" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Creating Conda environment 'filmagent' with Python 3.9.18...
    conda create -n filmagent python==3.9.18 -y
    if %ERRORLEVEL% NEQ 0 (
        echo Error: Failed to create Conda environment.
        exit /b 1
    )
) else (
    echo Conda environment 'filmagent' already exists.
)

:: Step 3: Activate the 'filmagent' environment
echo Activating Conda environment 'filmagent'...
call conda activate filmagent
if %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to activate Conda environment.
    exit /b 1
)

:: Step 4: Install dependencies from env.txt
echo Installing dependencies from env.txt...
pip install -r env.txt
if %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to install dependencies.
    exit /b 1
)

:: Step 5: Run the main script
echo Starting the FilmAgent project...
python main.py
if %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to start the FilmAgent project.
    exit /b 1
)

echo Setup and startup completed successfully!
exit /b 0
```

### Explanation of the Code:
1. **Conda Check**:
   - The script first checks if Conda is installed by running `conda --version`.
   - If Conda is not found, it exits with an error message.

2. **Environment Check**:
   - It checks if the `filmagent` environment already exists using `conda env list` and `findstr`.
   - If the environment doesn't exist, it creates one with Python 3.9.18.

3. **Environment Activation**:
   - The script activates the `filmagent` environment using `call conda activate filmagent`.

4. **Dependency Installation**:
   - It installs the required dependencies listed in `env.txt` using `pip install -r env.txt`.

5. **Run the Main Script**:
   - Finally, it runs the `main.py` script to start the project.

6. **Error Handling**:
   - Each step checks for errors using `%ERRORLEVEL%` and provides meaningful feedback if something goes wrong.

### Final Output:
```
@echo off
:: setup_windows.bat - Automates the setup and startup of the FilmAgent project on Windows.

:: Step 1: Check if Conda is installed
echo Checking for Conda installation...
conda --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Error: Conda is not installed or not added to PATH.
    echo Please install Conda and ensure it is accessible from the command line.
    exit /b 1
)

:: Step 2: Check if the 'filmagent' environment already exists
echo Checking for existing Conda environment 'filmagent'...
conda env list | findstr "filmagent" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Creating Conda environment 'filmagent' with Python 3.9.18...
    conda create -n filmagent python==3.9.18 -y
    if %ERRORLEVEL% NEQ 0 (
        echo Error: Failed to create Conda environment.
        exit /b 1
    )
) else (
    echo Conda environment 'filmagent' already exists.
)

:: Step 3: Activate the 'filmagent' environment
echo Activating Conda environment 'filmagent'...
call conda activate filmagent
if %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to activate Conda environment.
    exit /b 1
)

:: Step 4: Install dependencies from env.txt
echo Installing dependencies from env.txt...
pip install -r env.txt
if %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to install dependencies.
    exit /b 1
)

:: Step 5: Run the main script
echo Starting the FilmAgent project...
python main.py
if %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to start the FilmAgent project.
    exit /b 1
)

echo Setup and startup completed successfully!
exit /b 0
