#!/bin/bash
cd "$(dirname "$0")"

# Create .venv if it doesn't exist
if [ ! -d ".venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv .venv
fi

# Activate the virtual environment
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the Streamlit app
streamlit run main.py