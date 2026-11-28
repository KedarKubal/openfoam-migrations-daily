# MIGRATION.md

## Paper
**Title:** Numerical Study of Heat Transfer and Laminar Flow over a Backward Facing Step with and without Obstacle  
**Authors:** Hussein Togun, Tuqa Abdulrazzaq, S. N. Kazi, A. Badarudin, M. K. A. Ariffin, M. N. M. Zubir  
**Year:** 2014  
**Link:** https://zenodo.org/records/1090926  
**Original tool:** ANSYS FLUENT 14  

## Mapping table (paper → OpenFOAM)
| Paper setup | OpenFOAM equivalent |
|-------------|---------------------|
| Solver: ANSYS FLUENT 14, SIMPLE, laminar steady 2D | simpleFoam, SIMPLE, laminar |
| Turbulence: laminar | turbulenceProperties: laminar |
| Mesh: ICEM ~100k elements, refined at step | blockMesh structured, ~8k cells (40x20 upstream + 200x40 downstream), grading toward step |
| BCs: velocity inlet, pressure outlet, no-slip walls, constant heat flux (not modeled here) | fixedValue U inlet, fixedValue p=0 outlet, noSlip walls, empty front/back |
| Schemes: second-order upwind etc. | linearUpwind for div(phi,U), Gauss linear |
| Linear solvers: residual 1e-4 cont, 1e-7 mom | GAMG/smoothSolver, residualControl 1e-4/1e-5 |

## Assumptions (paper silent or simplified)
- Fluid properties not stated; nu set to 4.8e-6 m²/s for Re_H = U·H/ν = 100 with U=0.1 m/s, H=0.0048 m.
- Inlet profile: paper validates against Al-Aswadi et al.; assumed uniform (short upstream); parabolic would be better.
- Heat transfer omitted for isothermal flow migration (paper focuses on HTC enhancement with obstacles); base case no obstacle.
- Mesh coarser than paper for CI runtime <15 min.
- Reattachment length taken from equivalent Erturk (2008) benchmark for ER=2, Re_D≈200 ≈ xr/h=5.

## Reference values to reproduce
1. Reattachment length ≈ 0.024 m (from step) — source: Erturk 2008 equivalent, paper agrees with literature velocity profiles.
2. Streamwise velocity at probe near reattachment ≈ 0.02 m/s — estimated from typical profiles.

## Local run instructions
```bash
cd case
./Allclean
./Allrun
python3 ../verify.py
```
Expected runtime: ~2-5 min on 4-core for 500 iterations.

## Lessons applied from prior days
- From 2026-11-26/27 LDC cases: ensure empty for 2D, set -e in Allrun, functionObjects to postProcessing/, residualControl present, noSlip on walls.
