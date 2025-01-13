# Code used for ISCIII's Bioinformatics Master's Thesis
## Structural an functional evaluation of missense mutations in KRAS and their impact on interactions
Author: María Legarreta

### **Abstract**

KRAS (Kirsten Rat Sarcoma Viral Oncogene Homolog) mutations, particularly missense mutations, play a critical role in cancer development by altering protein-protein interactions (PPIs) and disrupting cellular signaling pathways. This thesis analyzes the structural and functional impact of 156 unique missense mutations in KRAS, with a focus on their effects on the interactions. Using computational tools like AlphaFold3 and EvoEF1, the research highlights mutations of critical regions such as the P-loop and Switch I and II regions in KRAS. We also found that mutations within protein-protein interaction (PPI) interfaces exhibit a greater effect on interaction energy compared to those outside the interface, emphasizing their relevance in cancer progression. While most mutations showed minimal structural deviations from the wild-type protein, specific mutations, like D38Y and R149G, caused notable structural changes, likely affecting KRAS functionality. 
This thesis underscores the importance of personalized therapeutic strategies targeting KRAS mutations and provides a foundation for future research. 

### **Objectives**

The main objective of this thesis is to analyze the impact of KRAS missense mutations on the protein-protein interaction interface of KRAS, providing insights into how the interaction between proteins affects cancer progression. 
The specific aims are:
1. To identify and evaluate reported mutations in KRAS, including their frequency in relevant databases.
2. To analyze the structural changes caused by missense mutations in KRAS using structural modeling tools.
3. To calculate the interaction energy for multiple KRAS-related protein pairs using EvoEF1, assessing the impact of mutations on the stability of these interactions.

### **Description of scripts**

This repo contains the following scripts used for the development of this thesis:
- **interfaceResidues.py**: This script identifies and selects the "interface" residues between two chains in a protein complex based on the difference in accessible surface area (dASA) above a specified cutoff
- **find_interfaceResidues.py**: This script loads a protein structure in PyMOL, colors its chains, performs interface residue analysis based on a given dASA cutoff, and saves the results to a file.
- **batch_find_interfaceResidues.py**: This script iterates through directories in the current working directory, and for those starting with a specific prefix, it runs a Python script (find_interfaceResidues.py) to analyze interface residues, passing the directory name and a cutoff value as arguments.
- **proton.py**: This script runs a series of steps for protein analysis based on the EvoEF1 algorithm. It prepares directories and files, processes the interface residues, calculates mutant structures and their energies, detects outliers, and organizes the results into specific output folders, handling errors along the way and cleaning up temporary files.
- **batch_proton.py**: This script reads a list of target protein files from the specified results file (P01116-interfaces.pdb_hm_pioneer.sig.txt). For each target, it constructs the full path of a PDB file and then runs the proton.py script with predefined parameters (EvoEF1 algorithm, cutoff, and IQR) using the subprocess.run() method. If the command is successful, it prints the standard output; otherwise, it catches and prints any errors. The base_command is dynamically populated with the specific PDB file path for each target protein.
- **summary_analysecomplex.py**: This script reads a TSV file with protein mutation data, checks if required columns are present, and then extracts and renames relevant columns before saving them to a new CSV file.
