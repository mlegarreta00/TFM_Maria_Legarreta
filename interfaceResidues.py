from pymol import cmd, stored

def interfaceResidues(cmpx, cA='c. A', cB='c. B', cutoff=1.0, selName="interface"):
    """
    interfaceResidues -- Finds 'interface' residues between two chains in a complex.

    PARAMETERS:
        cmpx: The complex containing cA and cB.
        cA: Chain A to analyze.
        cB: Chain B to analyze.
        cutoff: Difference in area (dASA) above which residues are considered interface residues.
        selName: Name of the selection to create.

    RETURNS:
        - A list of tuples with (modelName, residueNumber, dASA).
        - Creates a selection in PyMOL with the name `selName`.
    """
    # Save user's settings before modifying them
    oldDS = cmd.get("dot_solvent")
    cmd.set("dot_solvent", 1)

    # Temporary object and selection names
    tempC, selName1 = "tempComplex", selName + "1"
    chA, chB = "chA", "chB"

    # Create a temporary complex and disable the original
    cmd.create(tempC, cmpx)
    cmd.disable(cmpx)

    # Remove unnecessary chains
    cmd.remove(tempC + f" and not (polymer and ({cA} or {cB}))")

    # Get the area of the complete complex
    cmd.get_area(tempC, load_b=1)
    cmd.alter(tempC, 'q=b')  # Copy areas from b to q

    # Extract the two chains and calculate their individual areas
    cmd.extract(chA, f"{tempC} and ({cA})")
    cmd.extract(chB, f"{tempC} and ({cB})")
    cmd.get_area(chA, load_b=1)
    cmd.get_area(chB, load_b=1)

    # Update the area difference in the `b` field
    cmd.alter(f"{chA} or {chB}", "b=b-q")

    # Store residues exceeding the cutoff
    stored.r, rVal, seen = [], [], []
    cmd.iterate(f'{chA} or {chB}', 'stored.r.append((model, resi, chain, b))')

    # Enable the original complex and initialize the selection
    cmd.enable(cmpx)
    cmd.select(selName1, 'none')

    # Process residues and create the selection
    for (model, resi, chain, diff) in stored.r:
        key = f"{resi}-{model}-{chain}"
        if abs(diff) >= float(cutoff):
            if key in seen:
                continue
            seen.append(key)
            rVal.append((model, resi, diff))
            cmd.select(selName1, selName1 + f" or (model {model} and chain {chain} and resi {resi})")

    # Transfer the selection to the original complex
    cmd.select(selName, f"{cmpx} in {selName1}")

    # Clean up temporary objects
    cmd.delete(selName1)
    cmd.delete(chA)
    cmd.delete(chB)
    cmd.delete(tempC)

    # Enable the selection
    cmd.enable(selName)

    # Restore original settings
    cmd.set("dot_solvent", oldDS)

    return rVal

# Extend PyMOL with this function
cmd.extend("interfaceResidues", interfaceResidues)
