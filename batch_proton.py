import os
import subprocess
base_dir = "/home/vant/Documents/Master/TFM/new_project/data/KRAS/pioneer/af3"
base_command = "python ./proton.py --pdb {pdb_file} --chain_ID A --algorithm EvoEF1 --cut_off 5.0 --IQR 1.5"
results_file = "/home/vant/Documents/Master/TFM/new_project/data/KRAS/pioneer/af3/results/P01116-interfaces.pdb_hm_pioneer.sig.txt"
with open(results_file, "r") as f:
	targets = [line.strip() for line in f.readlines()]
for target in targets:
	pdb_file = f"{base_dir}/{target}/fold_{target}_model_0.pdb"
	command = base_command.format(pdb_file=pdb_file)
	try:
    		print(f"Executing: {command}")
    		result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    		print(f"Output:\n{result.stdout}")
	except subprocess.CalledProcessError as e:
    		print(f"Command failed with error:\n{e.stderr}")

