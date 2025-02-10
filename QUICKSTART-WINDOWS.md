# Quickstart Guide for Windows Users

Welcome to the FilmAgent project! This guide will walk you through the steps to set up and start the project on a Windows environment. Follow the instructions below to get started.

---

## Prerequisites

Before you begin, ensure that the following prerequisites are met:

1. **Windows Operating System**:
   - This guide is tailored for Windows 10/11 users.

2. **Conda Installation**:
   - Download and install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/).
   - Ensure that Conda is added to your system's PATH during installation.

3. **Git Installation**:
   - Download and install [Git](https://git-scm.com/).
   - Verify the installation by running the following command in a terminal:
     ```cmd
     git --version
     ```

4. **Python Version**:
   - Ensure Python 3.9.18 is installed. Conda will handle this during the setup process.

---

## Step 1: Clone the Repository

Open a terminal (Command Prompt or PowerShell) and run the following commands to clone the FilmAgent repository:

```cmd
git clone https://github.com/teretzdev/FilmAgent.git
cd FilmAgent
```

---

## Step 2: Run the Setup Script

The `setup_windows.bat` script automates the setup process. It will:
- Check for Conda installation.
- Create and activate a Conda environment named `filmagent`.
- Install the required dependencies from `env.txt`.
- Start the FilmAgent project.

To execute the script, run the following command:

```cmd
setup_windows.bat
```

### Expected Output

The script will guide you through the setup process. Upon successful execution, you should see the following message:

```
Setup and startup completed successfully!
```

---

## Step 3: Verify the Installation

1. **Check the Logs**:
   - Navigate to the `Logs` directory to view the setup logs.

2. **Check the Script Directory**:
   - Ensure that the `Script` directory contains the generated files.

---

## Additional Configuration

### Modify File Paths (Optional)

If you encounter issues with file paths, ensure that all paths in the scripts are updated to use Windows-style paths. For example:

```python
ROOT_PATH = "C:\\path\\to\\FilmAgent"
```

Use double backslashes (`\\`) or raw strings (`r"C:\path\to\"`) to avoid escape sequence issues.

---

## Troubleshooting

### Common Issues

1. **Conda Not Found**:
   - Ensure that Conda is installed and added to your system's PATH.
   - Restart your terminal and try again.

2. **Dependency Installation Fails**:
   - Check the `env.txt` file for any missing or incompatible dependencies.
   - Manually install the dependencies using:
     ```cmd
     pip install -r env.txt
     ```

3. **Script Errors**:
   - Review the error messages in the terminal and the `Logs` directory.
   - Ensure that all prerequisites are met.

---

## Next Steps

Once the setup is complete, you can explore the following features:

1. **Generate Images**:
   - Use the `image_generator.py` script to create images for video sequences.

2. **Generate Audio**:
   - Use the `GenerateAudio.py` script to add voice acting to your scripts.

3. **Run the ReactJS Frontend**:
   - Follow the instructions in the `README.md` file to set up the frontend.

---

## Need Help?

If you encounter any issues or have questions, feel free to open an issue on the [GitHub repository](https://github.com/teretzdev/FilmAgent/issues).

Happy Filmmaking!
```

---

### Step 4: Review the Code
- The file is named `QUICKSTART-WINDOWS.md` and is placed in the root directory as requested.
- The content includes:
  - Prerequisites for Windows users.
  - Step-by-step instructions for cloning the repository, running the setup script, and verifying the installation.
  - Additional configuration tips for Windows environments.
  - Troubleshooting steps for common issues.
- The guide is clear, well-structured, and uses markdown formatting with code blocks for commands.

---

### Final Output
```
# Quickstart Guide for Windows Users

Welcome to the FilmAgent project! This guide will walk you through the steps to set up and start the project on a Windows environment. Follow the instructions below to get started.

---

## Prerequisites

Before you begin, ensure that the following prerequisites are met:

1. **Windows Operating System**:
   - This guide is tailored for Windows 10/11 users.

2. **Conda Installation**:
   - Download and install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/).
   - Ensure that Conda is added to your system's PATH during installation.

3. **Git Installation**:
   - Download and install [Git](https://git-scm.com/).
   - Verify the installation by running the following command in a terminal:
     ```cmd
     git --version
     ```

4. **Python Version**:
   - Ensure Python 3.9.18 is installed. Conda will handle this during the setup process.

---

## Step 1: Clone the Repository

Open a terminal (Command Prompt or PowerShell) and run the following commands to clone the FilmAgent repository:

```cmd
git clone https://github.com/teretzdev/FilmAgent.git
cd FilmAgent
```

---

## Step 2: Run the Setup Script

The `setup_windows.bat` script automates the setup process. It will:
- Check for Conda installation.
- Create and activate a Conda environment named `filmagent`.
- Install the required dependencies from `env.txt`.
- Start the FilmAgent project.

To execute the script, run the following command:

```cmd
setup_windows.bat
```

### Expected Output

The script will guide you through the setup process. Upon successful execution, you should see the following message:

```
Setup and startup completed successfully!
```

---

## Step 3: Verify the Installation

1. **Check the Logs**:
   - Navigate to the `Logs` directory to view the setup logs.

2. **Check the Script Directory**:
   - Ensure that the `Script` directory contains the generated files.

---

## Additional Configuration

### Modify File Paths (Optional)

If you encounter issues with file paths, ensure that all paths in the scripts are updated to use Windows-style paths. For example:

```python
ROOT_PATH = "C:\\path\\to\\FilmAgent"
```

Use double backslashes (`\\`) or raw strings (`r"C:\path\to\"`) to avoid escape sequence issues.

---

## Troubleshooting

### Common Issues

1. **Conda Not Found**:
   - Ensure that Conda is installed and added to your system's PATH.
   - Restart your terminal and try again.

2. **Dependency Installation Fails**:
   - Check the `env.txt` file for any missing or incompatible dependencies.
   - Manually install the dependencies using:
     ```cmd
     pip install -r env.txt
     ```

3. **Script Errors**:
   - Review the error messages in the terminal and the `Logs` directory.
   - Ensure that all prerequisites are met.

---

## Next Steps

Once the setup is complete, you can explore the following features:

1. **Generate Images**:
   - Use the `image_generator.py` script to create images for video sequences.

2. **Generate Audio**:
   - Use the `GenerateAudio.py` script to add voice acting to your scripts.

3. **Run the ReactJS Frontend**:
   - Follow the instructions in the `README.md` file to set up the frontend.

---

## Need Help?

If you encounter any issues or have questions, feel free to open an issue on the [GitHub repository](https://github.com/teretzdev/FilmAgent/issues).

Happy Filmmaking!
