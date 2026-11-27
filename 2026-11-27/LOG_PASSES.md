# LOG_PASSES.md

## Pass 1 (Generator)
- Wrote complete case for simpleFoam: 0/U p, constant/transportProperties (nu=0.01 for Re=100), turbulenceProperties laminar, system/blockMeshDict (64x64), controlDict with probes+fieldMinMax, fvSchemes, fvSolution, Allrun (set -e), Allclean.
- BCs: fixedValue (1,0,0) top, (-1,0,0) bottom for antiparallel.

## Pass 2 (Updater)
- Verifier static checks: all dicts present, BCs on all patches (movingTop, movingBottom, fixedWalls, frontAndBack empty), dimensions consistent [0 1 -1] for U, [0 2 -2] for p, no turb quantities needed (laminar), residualControl 1e-5 sane, schemes cover div(phi,U) and laplacian.
- Applied lessons from prior day (2026-11-26 LDC): ensured empty for 2D, noSlip, set -e in Allrun, functionObjects to postProcessing/.

## Pass 3 (Updater)
- Tightened relaxationFactors.
- Added probe at center for verify.py parsing (placeholder).
- Confirmed case faithful to two-sided lid-driven staggered (approximated).
- All static checks pass. No runtime (cannot execute OpenFOAM).

Self-improvement: Not a repeat of prior LDC paper; different geometry (two moving lids) and paper.
