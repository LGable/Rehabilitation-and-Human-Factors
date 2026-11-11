# Rehabilitation and Human Factors

Applied demonstrations of return-to-work coordination, environmental usability, vocational rehabilitation, care coordination, and functional service delivery.

## What this repository demonstrates

- Connecting functional needs to practical service and workplace design.
- Applying human-factors thinking to environmental and safety questions.
- Structuring return-to-work and vocational-program analysis.
- Using synthetic data without exposing client, patient, student, or employee records.

## Projects

- [Return-to-work coordination](projects/return_to_work.md)
- [Patient and environmental human factors](projects/environmental_safety.md)
- [Functional vocational programming](projects/vocational_programs.md)
- [Clinical and home-health case coordination](projects/care_coordination.md)

## Data and reproducibility

- [`data/return_to_work_synthetic.csv`](data/return_to_work_synthetic.csv) is synthetic vocational demonstration data.
- Read the [data policy](DATA_POLICY.md) before interpreting any metric.
- From this repository directory, run:

```powershell
python scripts/analyze_rtw.py
```

## Interpretation limits

The examples are educational and portfolio demonstrations. They do not represent a clinical recommendation, employer assessment, patient outcome, or validated intervention without appropriate professional review and source evidence.

## Repository map

```text
data/       Synthetic demonstration data
projects/   Rehabilitation and human-factors examples
scripts/    Reproducible analysis scripts
```
