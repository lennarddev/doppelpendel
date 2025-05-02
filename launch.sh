#!/bin/bash
cd "$(dirname "$0")"

# Create .venv if missing
if [ ! -d ".venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv .venv
fi

# Activate and run
source .venv/bin/activate
pip install -r requirements.txt
streamlit run main.py