"""
Stage 3: evaluate
Checks the model on the test set. R2 score is the main thing we look at.
If the score is too low, this script exits with an error and the model
never gets pushed to hugging face.
"""
import sys
import json
import yaml
import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


def main():
    params = yaml.safe_load(open("params.yaml"))["evaluate"]

    model = joblib.load("model/model.joblib")
    test_df = pd.read_csv("data/test.csv")
    X_test = test_df.drop(columns=["target"])
    y_test = test_df["target"]

    preds = model.predict(X_test)

    mse = mean_squared_error(y_test, preds)
    metrics = {
        "r2": r2_score(y_test, preds),
        "mse": mse,
        "rmse": float(np.sqrt(mse)),
        "mae": mean_absolute_error(y_test, preds),
    }

    with open("metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    print(json.dumps(metrics, indent=2))

    if metrics["r2"] < params["min_r2"]:
        print(
            f"FAIL: r2 score {metrics['r2']:.4f} "
            f"is below the gate {params['min_r2']}"
        )
        sys.exit(1)

    print("PASS: model cleared the quality gate")


if __name__ == "__main__":
    main()
