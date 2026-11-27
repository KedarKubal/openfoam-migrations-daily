# MIGRATION.md

## Paper
**Title:** Using the Ansys Fluent for simulation of two-sided lid-driven flow in a staggered cavity  
**Authors:** Jelena Đ. Marković, Nataša Lj. Lukić, Jelena D. Ilić, Branislava G. Nikolovski, Milan N. Sovilj, Ivana M. Šijački  
**Year:** 2012  
**Link:** http://www.doiserbia.nb.rs/img/doi/1450-7188/2012/1450-71881243169M.pdf  
**Original tool:** ANSYS FLUENT

## Mapping
| Paper setup | OpenFOAM equivalent |
|-------------|---------------------|
| Solver: ANSYS FLUENT (finite volume) | simpleFoam (incompressible steady) |
| Turbulence: laminar (low Re) | simulationType laminar |
| Mesh: not specified exactly (assumed structured) | blockMesh 64x64 |
| BCs: moving lids (parallel/antiparallel), no-slip walls | fixedValue on movingTop/Bottom, noSlip on fixedWalls |
| Schemes: not detailed | linearUpwind for convection |
| Linear solvers: not specified | GAMG for p, smoothSolver for U |

## Assumptions (paper silent)
- Exact staggered geometry offset not fully detailed in available abstract/snippets; approximated as square cavity with top and bottom lids moving in opposite directions (antiparallel).
- Mesh resolution not given; used 64x64 for CI runtime <15 min.
- Specific Re for Table 1 not extracted; used Re=100 (nu=0.01).
- Vortex locations from Table 1 approximated for reference.

## Reference values to reproduce
1. Centerline Ux ~ 0 (Figure 7)
2. Primary vortex approx location (Table 1)
3. Uy at center ~0

## Local run instructions
```bash
cd case
./Allclean
./Allrun
python3 ../verify.py
```
Expected runtime: ~2-5 min on 4-core for 64x64 mesh.

## Expected
Steady laminar solution with counter-rotating vortices from opposing lids.
