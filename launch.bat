@echo off
cd %~dp0

REM Create .venv if missing
IF NOT EXIST .venv (
    echo Creating virtual environment...
    python -m venv .venv
)

call .venv\Scripts\activate

pip install -r requirements.txt

streamlit run main.py

pause