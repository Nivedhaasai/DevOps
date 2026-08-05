# DVC ML Pipeline — Regression

A regression counterpart to [MuthuPalaniappan925/DVC-ML-Pipeline](https://github.com/MuthuPalaniappan925/DVC-ML-Pipeline),
which builds a classification pipeline on the Breast Cancer Wisconsin dataset.
This version swaps in the scikit-learn **Diabetes dataset** (predicting a
quantitative measure of disease progression) and a `RandomForestRegressor`,
keeping the same 5-stage DVC pipeline structure:

1. **data_ingestion** — loads `sklearn.datasets.load_diabetes` -> `data/raw/data.csv`
2. **data_preprocessing** — cleans column names, drops duplicates, fills missing values -> `data/processed/data.csv`
3. **feature_engineering** — train/test split + `StandardScaler` -> `data/features/{train,test}.csv`
4. **model_building** — trains a `RandomForestRegressor` -> `model.pkl`
5. **model_evaluation** — computes regression metrics -> `metrics.json`

## Results

```
mae         43.63964
mse       2894.46005
r2_score     0.45368
rmse        53.80019
```

## Setup & Run

### 1. Install dependencies
```bash
pip install dvc scikit-learn pandas joblib pyyaml numpy
```

### 2. Initialize Git + DVC
```bash
git init
dvc init
```

### 3. Run the pipeline
```bash
dvc repro
```

### 4. View the DAG
```bash
dvc dag
```

### 5. View metrics
```bash
dvc metrics show
```

### 6. Commit to Git
```bash
git add .
git commit -m "Initial DVC pipeline"
```

---

**Re-run after changing code/params:**
```bash
dvc repro
```

**Force re-run everything:**
```bash
dvc repro -f
```
