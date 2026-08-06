# MLflow-101-Regression

Regression version of [MuthuPalaniappan925/MLflow-101](https://github.com/MuthuPalaniappan925/MLflow-101).
The original repo does MLflow experiment tracking (local + DagsHub) on the
Breast Cancer classification dataset. This does the same thing but for a
regression problem.

**Note on the dataset:** the assignment asked for the Boston Housing dataset,
but `load_boston()` was removed from scikit-learn (1.2+) because it embeds a
feature derived from racial demographics that's been widely criticized. Used
`fetch_california_housing()` instead — it's sklearn's own recommended
replacement and is still a housing-price regression problem with the same
shape (numeric features -> continuous price target).

## What's here

- `ml_flow_regression.ipynb` — trains 3 models, tracks experiments on a local
  MLflow server (`http://127.0.0.1:5000`), picks the best one by R2, registers
  it, pushes it to the Production stage.
- `MLflow_dagshub_regression.ipynb` — same thing, but experiments are logged
  straight to DagsHub instead of a local server.

## Models

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

Picked the best model by **R2 score** (that's the metric this assignment
cares about most, so it's what all three runs get compared on — MSE/RMSE/MAE
are logged too for completeness).

## Results

| Model             | R2     | RMSE   | MAE    |
|-------------------|--------|--------|--------|
| Linear Regression | 0.576  | 0.746  | 0.533  |
| Random Forest     | 0.775  | 0.543  | 0.366  |
| XGBoost           | 0.841  | 0.457  | 0.296  |

XGBoost won, registered as `California_Housing_Best_Model`.

## DagsHub

Experiments are live here: https://dagshub.com/Nivedhaasai/MLflow-Regression

MLflow UI (via DagsHub): https://dagshub.com/Nivedhaasai/MLflow-Regression.mlflow/#/experiments/0

## Running it yourself

```bash
pip install mlflow dagshub scikit-learn xgboost pandas numpy
```

For the local notebook, start an MLflow server first:
```bash
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 127.0.0.1 --port 5000
```

For the DagsHub notebook, `dagshub.init()` will prompt you to authenticate
the first time (or set a token via `dagshub login` / `DAGSHUB_USER_TOKEN`).
