#!/bin/bash

# Description: This script sets up a Python virtual environment (if not already created), activates it,
#              and runs test scripts for data preprocessing, parsing, and summarization.

# Step 1: Check if virtual environment exists, if not, create it
if [ ! -d "venv" ]; then
  echo "Virtual environment not found. Creating one..."
  python -m venv venv
  echo "Virtual environment created."
else
  echo "Virtual environment already exists."
fi

# Step 2: Activate the virtual environment
if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
  # Linux/Mac
  echo "Activating the virtual linux environment..."
  source venv/bin/activate
  which python
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
  # Windows
  echo "Activating the virtual windows environment..."
  source venv/Scripts/activate
else
  echo "Unsupported OS type: $OSTYPE"
  exit 1
fi

# Step 3: Install required packages
echo "Installing required packages..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
  echo "Failed to install required packages. Exiting."
  deactivate
  exit 1
fi

# Step 4: Run the test scripts
# Test data extraction
echo "Running data extraction tests..."
python ./data_preprocessing/test_extraction.py
if [ $? -ne 0 ]; then
  echo "Data extraction tests failed. Exiting."
  deactivate
  exit 1c
fi

# Test data parsing
echo "Running data parsing tests..."
python ./data_parsing/test_parsing.py
if [ $? -ne 0 ]; then
  echo "Data parsing tests failed. Exiting."
  deactivate
  exit 1
fi

# Test data summarization
echo "Running data summarization tests..."
python ./data_summarization/test_summarization.py
if [ $? -ne 0 ]; then
  echo "Data summarization tests failed. Exiting."
  deactivate
  exit 1
fi

# Step 5: Deactivate the virtual environment
echo "Deactivating the virtual environment..."
deactivate

echo "All tests passed successfully!"
