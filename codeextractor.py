# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

import re
import tempfile
import shutil
import os

def extract_airport_code(text):
    # Use a regular expression to find the code within parentheses
    match = re.search(r'\((\w+)\)', text)
    if match:
        return match.group(1)
    else:
        return None

def process_file(file_path):
    # Use a temporary file to avoid overwriting issues
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w', newline='', encoding='utf-8')
    try:
        with open(file_path, 'r', encoding='utf-8') as infile, temp_file:
            for line in infile:
                airport_code = extract_airport_code(line.strip())
                if airport_code:
                    temp_file.write(airport_code + '\n')
                    
        # Replace the original file with the processed file
        shutil.move(temp_file.name, file_path)
    finally:
        # Clean up the temporary file if it still exists
        if temp_file:
            temp_file.close()
            if os.path.exists(temp_file.name):
                os.remove(temp_file.name)

# Example usage
file_path = 'input.txt'  # Replace with your file path
process_file(file_path)
print(f"Processed data has been written to {file_path}")

