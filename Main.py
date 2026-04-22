import subprocess
import sys
import os

script_path = r"D:\Ashish Doc\Ashish\AI-engineer\1. Python\17. Command_Line_Arguments.py"

number1 = 25
number2 = 15
operation = "sub"

script_args = [str(number1), str(number2), operation]

try:
    print(f"Attempting to run script using interpreter: {sys.executable}")

    result = subprocess.run(
            [sys.executable, script_path] + script_args,
            check=True,  # Raise a CalledProcessError if the script returns a non-zero exit code
            capture_output=True, # Capture stdout and stderr
            text=True
        )

    print("\n--- Script Output (STDOUT) ---")
    print(result.stdout)

    if result.stderr:
        print("\n--- Script Errors (STDERR) ---")
        print(result.stderr)

    print(f"\nScript finished with exit code: {result.returncode}")

except Exception as exp:
    print(f"An error occured: {exp}")
