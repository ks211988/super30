"""Super30 - Complete Development Environment Setup.

This file contains the full setup instructions and the required hello.py
program. Run this file with Python to display the instructions and create
hello.py in the current directory (without overwriting an existing file).

The installer steps must be completed manually; this script does not install
Python, VS Code, Git, or sign in to GitHub.
"""

from pathlib import Path

SETUP_GUIDE = """
SUPER30 - COMPLETE DEVELOPMENT ENVIRONMENT SETUP
================================================

STEP 1: INSTALL AND VERIFY PYTHON
---------------------------------
Download Python: https://www.python.org/downloads/
Open PowerShell or the VS Code terminal and run:
    python --version
    pip --version
Expected Python version example: Python 3.13.x (your version may differ).

STEP 2: SET UP VS CODE
----------------------
Download VS Code: https://code.visualstudio.com/
Install extensions:
    - Python (Microsoft)
    - Pylance (Microsoft)
    - Python Debugger (Microsoft)
    - Jupyter (Microsoft, optional)
Open a terminal: Terminal > New Terminal
Select Python interpreter: Ctrl + Shift + P > Python: Select Interpreter

STEP 3: INSTALL GIT AND CONFIGURE GITHUB
----------------------------------------
Download Git: https://git-scm.com/downloads
Verify Git:
    git --version
Configure Git (replace placeholders with your details):
    git config --global user.name "Your Name"
    git config --global user.email "your-email@example.com"
Sign in to https://github.com/ via VS Code's Accounts menu.
Do not show passwords or access tokens in your demonstration video.

STEP 4: CREATE YOUR SUPER30 PROJECT
-----------------------------------
Open a terminal and run:
    mkdir super30-python
    cd super30-python
    code .
Create hello.py with these TWO SEPARATE lines:
    print("Hello Super30")
    print("My Python environment is ready")
Run it:
    python hello.py
Expected output:
    Hello Super30
    My Python environment is ready

STEP 5: OPTIONAL GIT DEMONSTRATION
----------------------------------
Inside your project folder, run:
    git init
    git add hello.py
    git commit -m "Initial Super30 Python setup"
    git status
You may also use VS Code's Publish to GitHub feature.



HELLO_CODE = 'print("Hello Super30")\nprint("My Python environment is ready")\n'


def create_hello_file(folder: Path = Path.cwd()) -> Path:
    """Create the assignment's hello.py without replacing an existing file."""
    path = folder / "hello.py"
    if path.exists():
        print(f"Existing file left unchanged: {path}")
    else:
        path.write_text(HELLO_CODE, encoding="utf-8")
        print(f"Created: {path}")
    return path


def main() -> None:
    """Display the guide and prepare the required sample Python file."""
    print(SETUP_GUIDE)
    create_hello_file()
    print("\nRequired program output:")
    print("Hello Super30")
    print("My Python environment is ready")


if __name__ == "__main__":
    main()
