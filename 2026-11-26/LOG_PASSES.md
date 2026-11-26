# LOG_PASSES.md

## Pass 1 (Generator)
- Wrote complete case: 0/U p, constant/transportProperties turbulenceProperties, system/blockMeshDict controlDict fvSchemes fvSolution, Allrun Allclean.
- Mesh 80x80, simpleFoam laminar, Re=1000 (nu=0.001).
- Function objects: probes + fieldMinMax.
- Verifier checks planned for dictionaries, BCs on all patches, dimensions, no turb inlet (laminar), sane residuals, schemes for div(phi,U) etc.
- All checks static pass on first write.

## Pass 2 (Updater)
- Added vortex_center extraction logic note in Allrun (to be implemented via python in CI or post).
- Confirmed empty patches for 2D, noSlip on walls, fixedValue on lid.
- Tightened residualControl.

## Pass 3 (Updater)
- Finalized Allrun with set -e.
- Updated verify.py to parse vortex_center.txt if written.
- Ensured Allrun exits non-zero on failure.
- No prior LOG.md failures to apply (new repo).

All static verifier checks passed after 3 passes. No runtime validation (cannot execute OpenFOAM here).
