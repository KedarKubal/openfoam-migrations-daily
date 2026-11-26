# MIGRATION.md

## Paper
**Title:** Numerical Investigation of Fluid In 2D and 3D Lid-Driven Cavity at Different Reynolds Numbers  
**Authors:** Maria Margareta Zau Beu, Jiahn-Horng Chen  
**Year:** 2023  
**Journal:** Jurnal IPTEK, Vol 27 No 1  
**Link:** https://ejurnal.itats.ac.id/iptek/article/view/3427  
**PDF:** https://ejurnal.itats.ac.id/iptek/article/download/3427/3182  
**Proprietary tool:** ANSYS Fluent 19R1  
**License:** CC BY-SA 4.0  

## Mapping Table

| Paper setup | OpenFOAM equivalent | Notes |
|-------------|-----|-------|
| Solver: pressure-based steady | simpleFoam | laminar |
| Turbulence: not specified (laminar assumed for Re=1000) | simulationType laminar | Paper mentions turbulence at high Re but runs steady |
| Mesh: structured 501x501 / 601x601, y+<1, denser near walls | blockMesh 80x80 uniform | Coarser for CI runtime; graded optional |
| BCs: lid U=1 in +x, other walls no-slip | lid fixedValue (1 0 0), walls noSlip, frontAndBack empty | 2D |
| Schemes: least squares (paper) | Gauss linear, linearUpwind | Second-order-ish |
| Linear solvers: not specified | GAMG + smoothSolver | Standard |
| Fluid: incompressible, Re=U L /nu , L=1, U=1 | nu=0.001 for Re=1000 | nondimensional |
| Iterations: up to 10000 | residualControl 1e-4, max 5000 | |

## Assumptions (paper silent)
- Turbulence model: none stated; treated as laminar for the selected Re=1000 case (classic steady).
- Discretization schemes details beyond "least square method".
- Under-relaxation factors, residual criteria exact values.
- Fluid density=1, exact viscosity derivation (set via Re).
- Mesh grading details beyond "denser near walls".
- For 2D migration only; 3D not included to keep runtime low.

## Reference values to reproduce
1. Primary vortex location x = 0.521 (Table 3, 601×601 grid, Re=1000)
2. Primary vortex location y = 0.561 (Table 3, 601×601 grid, Re=1000)
Tolerance ±0.05 (approx 10% relative on the coordinate offset from center).

## Local run instructions
```bash
cd case
./Allclean
./Allrun
```
Expected runtime on 4-core: <2 min (80x80 mesh, simpleFoam converges quickly).

## Notes
Migration focuses on the well-documented Re=1000 2D case. Vortex center is extracted approximately in Allrun via post-processing of the U field (cell closest to min |U| in interior).
