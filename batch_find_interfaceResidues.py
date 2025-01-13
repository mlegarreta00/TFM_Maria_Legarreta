import os
import subprocess

cutoff_value = 5.0
target_prefix = "p01116_"

for directory in os.listdir():
    if os.path.isdir(directory) and directory.startswith(target_prefix):
        input_name = directory
        print(f"Processing directory: {input_name}")
        subprocess.run([
            "python", "find_interfaceResidues.py",
            "-i", input_name,
            "-c", str(cutoff_value)
        ], check=True)
