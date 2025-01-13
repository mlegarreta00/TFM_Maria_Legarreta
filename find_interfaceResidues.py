import argparse
from pymol import cmd, stored, util
from interfaceResidues import interfaceResidues

def load_and_color_chains(input_name, obj_name, color_map):
    """
    Load a structure and color its chains according to the provided color map.
    """
    cmd.load(f"{input_name}/fold_{input_name}_model_0.cif", obj_name)
    cmd.color(color_map["A"], f"{obj_name} and chain A")
    cmd.color(color_map["B"], f"{obj_name} and chain B")

def run_interface_analysis(obj_name, cutoff, output_file):
    """
    Run the interface analysis and save the selected residues to a file.
    """
    cmd.run("interfaceResidues.py")
    interfaceResidues(obj_name, cutoff=cutoff)

    stored.selected_residues = []
    cmd.iterate('interface', 'stored.selected_residues.append((chain, resi))')

    selected_residues = sorted(set(stored.selected_residues))
    with open(output_file, "w") as f:
        for chain, resi in selected_residues:
            print(f"{chain}{resi}")
            f.write(f"{chain}{resi}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run PyMOL interface analysis script with specified input."
    )
    parser.add_argument(
        "-i", "--input", required=True,
        help="Input name to load structure file and perform analysis"
    )
    parser.add_argument(
        "-c", "--cutoff", type=float, default=1.0,
        help="Cutoff value for interface residue dASA"
    )

    args = parser.parse_args()

    input_name = args.input
    obj_name = f"fold_{input_name}_model_0"
    cutoff_value = args.cutoff

    cmd.reinitialize()

    load_and_color_chains(
        input_name,
        obj_name,
        {"A": "green", "B": "cyan"}
    )

    output_file = f"{input_name}/interface_residues_0.txt"
    run_interface_analysis(obj_name, cutoff=cutoff_value, output_file=output_file)
