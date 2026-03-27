# 100 Days of ML

This repository contains daily machine learning practice work, datasets, and notebooks.

## Project Structure

- `day_1.ipynb`: early ML practice notebook.
- `practice1.ipynb`: classification workflow notebook (preprocessing, pipeline, evaluation).
- `ml_classification_dataset.csv`: dataset used for classification examples.
- `student_placement_dataset.csv`: additional dataset for experimentation.
- `model.pkl`: saved model artifact.

## Requirements

- Python 3.10+
- Jupyter Notebook or VS Code with Jupyter extension

Recommended Python packages:

- pandas
- numpy
- matplotlib
- scikit-learn

## Setup

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies.

Example (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install pandas numpy matplotlib scikit-learn jupyter
```

## How to Run

1. Open the project in VS Code.
2. Open `practice1.ipynb` or `day_1.ipynb`.
3. Select the project virtual environment as the notebook kernel.
4. Run cells in order.

## Notes

- Missing values are handled with `SimpleImputer(strategy="mean")` inside a scikit-learn pipeline.
- The current notebook demonstrates a logistic regression classification flow with train/test split and evaluation metrics.

## Future Improvements

- Add a `requirements.txt` file.
- Add model comparison (Logistic Regression vs tree-based models).
- Add proper train/validation/test tracking and experiment logs.