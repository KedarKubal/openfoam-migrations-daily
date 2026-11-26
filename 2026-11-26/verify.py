#!/usr/bin/env python3
"""
Verify OpenFOAM postProcessing against paper reference values.
Reads reference/reference_values.csv and postProcessing outputs.
Exit 0 only if all quantities pass within tolerance.
Standard library only.
"""
import csv
import os
import sys
import glob

def main():
    ref_path = "reference/reference_values.csv"
    post_dir = "case/postProcessing"
    if not os.path.exists(ref_path):
        print("FAIL: reference CSV missing")
        sys.exit(1)
    if not os.path.exists(post_dir):
        print("FAIL: postProcessing missing")
        sys.exit(1)

    refs = []
    with open(ref_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            refs.append(row)

    # Look for vortex location written by Allrun or probes
    vortex_file = os.path.join(post_dir, "vortex_center.txt")
    results = {}
    if os.path.exists(vortex_file):
        with open(vortex_file) as f:
            for line in f:
                if line.startswith("pv_x"):
                    results["pv_x"] = float(line.split()[1])
                if line.startswith("pv_y"):
                    results["pv_y"] = float(line.split()[1])

    all_pass = True
    for ref in refs:
        q = ref["quantity"]
        ref_val = float(ref["reference_value"])
        tol = float(ref["tolerance"])
        if q not in results:
            print(f"FAIL {q}: not found in postProcessing")
            all_pass = False
            continue
        got = results[q]
        if abs(got - ref_val) <= tol:
            print(f"PASS {q}: {got:.4f} vs {ref_val:.4f} (tol {tol})")
        else:
            print(f"FAIL {q}: {got:.4f} vs {ref_val:.4f} (tol {tol})")
            all_pass = False

    if all_pass:
        print("ALL PASS")
        sys.exit(0)
    else:
        print("SOME FAIL")
        sys.exit(1)

if __name__ == "__main__":
    main()
