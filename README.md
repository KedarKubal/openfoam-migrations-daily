# OpenFOAM Migrations (Daily)

Each dated folder migrates one published study from a proprietary tool to OpenFOAM and checks the result against the paper's published values.

## Status key
- `UNVALIDATED`: generated, not yet run
- `VALIDATED`: CI ran the case and all quantities are within tolerance
- `MISMATCH`: ran, but at least one quantity is out of tolerance
- `RUN_FAILED`: solver crashed or timed out

See `LOG.md` for the daily index.

## Run a case
Actions tab → run-case → Run workflow → enter the folder date (YYYY-MM-DD).
Or: `gh workflow run run.yml -f day=YYYY-MM-DD`

## Caveats
Cases are written by an LLM and the reference values are extracted from papers by an LLM. Treat `VALIDATED` as "matches the recorded reference values", and spot-check those values against the paper.
