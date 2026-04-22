import subprocess
import os
import sys

script_path = r"D:\Ashish Doc\Ashish\AI-engineer\1. Python\17. Command_Line_Optional_Arguments.py"

number1 = 25
number2 = 15
operation = "mul"


# Command-line arguments must be passed as a list of strings,
# including the flags defined in the parser.
script_args = [
    "--number1", str(number1),
    "--operation", operation,
    "--number2", str(number2)
]

try:
    # Use the system's python executable (sys.executable) to run the script.
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