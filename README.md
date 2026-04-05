# 100 Days of ML

This repository contains machine learning practice notebooks, datasets, saved model artifacts, and an additional Flask backend mini-project (`curequest`) for symptom-based disease suggestion.

## Repository Structure

```
100_days_of_ml/
├─ csv_files/
│  ├─ ml_classification_dataset.csv
│  └─ student_placement_dataset.csv
├─ practice _and_experiments/
│  ├─ day_1.ipynb
│  ├─ practice1.ipynb
│  └─ data_understanding_and_EDA.ipynb
├─ saved_models/
│  └─ model.pkl
├─ curequest/
│  ├─ app.py
│  ├─ logic.py
│  ├─ db_config.py
│  ├─ requirements.txt
│  ├─ SQL (2).txt
│  ├─ SQL data (2).txt
│  └─ README.md
└─ README.md
```

## ML Practice Track

The notebook-focused part of this repository is organized around practice and experiments:

- `practice _and_experiments/day_1.ipynb`: early notebook work.
- `practice _and_experiments/practice1.ipynb`: classification workflow experiments.
- `practice _and_experiments/data_understanding_and_EDA.ipynb`: data understanding and exploratory analysis.
- `csv_files/`: datasets used by the notebooks.
- `saved_models/model.pkl`: serialized trained model artifact.

### Recommended Environment (for notebooks)

- Python 3.10+
- VS Code + Jupyter extension (or Jupyter Lab/Notebook)
- Common packages:
	- pandas
	- numpy
	- matplotlib
	- scikit-learn
	- jupyter

Example setup (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install pandas numpy matplotlib scikit-learn jupyter
```

## CureQuest Track

`curequest/` is a Flask + MySQL backend service that suggests possible diseases from symptom input.

- API entry: `curequest/app.py`
- Core matching logic: `curequest/logic.py`
- DB config: `curequest/db_config.py`
- SQL schema and seed data:
	- `curequest/SQL (2).txt`
	- `curequest/SQL data (2).txt`

Install and run CureQuest:

```powershell
cd curequest
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Default local API: `http://127.0.0.1:5001`

## Notes

- This repo now contains both ML practice material and a backend project.
- For CureQuest API details and request/response examples, see `curequest/README.md`.

## Next Improvements

- Add a root-level `requirements.txt` (or separate environment files) for notebook dependencies.
- Add notebook run instructions with expected outputs for each day.
- Add tests for the CureQuest API and matching logic.