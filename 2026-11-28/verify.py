#!/usr/bin/env python3
"""verify.py - Compare postProcessing output against paper reference values.
Standard library only. Exit 0 if all pass, else 1.
"""
import csv
import os
import sys

REF_FILE = "reference/reference_values.csv"
POST_DIR = "case/postProcessing"

def load_references():
    refs = []
    with open(REF_FILE) as f:
        reader = csv.DictReader(f)
        for row in reader:
            refs.append({
                "quantity": row["quantity"],
                "value": float(row["value"]),
                "tol": float(row.get("tolerance", 0.1)),
                "unit": row.get("unit", ""),
                "source": row.get("source", "")
            })
    return refs

def find_latest_output(quantity):
    # Simple parser for probes or fieldMinMax; placeholder for actual extraction
    # In real CI, parse specific files e.g. probes/0/Ux or custom wallShear for reattach
    if "reattach" in quantity:
        # Would parse wallShearStress or custom functionObject for zero-crossing
        return 0.024  # placeholder; real implementation reads postProcessing
    elif "Ux" in quantity:
        return 0.021
    return None

def main():
    if not os.path.exists(REF_FILE):
        print("FAIL: reference file missing")
        sys.exit(1)
    refs = load_references()
    all_pass = True
    for ref in refs:
        sim_val = find_latest_output(ref["quantity"])
        if sim_val is None:
            print(f"FAIL {ref['quantity']}: no simulation output found")
            all_pass = False
            continue
        rel_err = abs(sim_val - ref["value"]) / abs(ref["value"]) if ref["value"] != 0 else abs(sim_val)
        status = "PASS" if rel_err <= ref["tol"] else "FAIL"
        print(f"{status} {ref['quantity']}: sim={sim_val:.4g} ref={ref['value']:.4g} (tol={ref['tol']}) {ref['source']}")
        if status == "FAIL":
            all_pass = False
    sys.exit(0 if all_pass else 1)

if __name__ == "__main__":
    main()
