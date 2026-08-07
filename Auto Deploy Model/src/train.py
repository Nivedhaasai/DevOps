"""
Stage 2: train
Fits the xgboost regressor on data/train.csv and saves model/model.joblib
Same model type and settings as the mlflow lab champion model.
"""
import yaml
import json
import joblib
import pandas as pd
from pathlib import Path
from xgboost import XGBRegressor

MODEL_DIR = Path("model")


def main():
    params = yaml.safe_load(open("params.yaml"))["train"]
    MODEL_DIR.mkdir(exist_ok=True)

    train_df = pd.read_csv("data/train.csv")
    X_train = train_df.drop(columns=["target"])
    y_train = train_df["target"]

    model = XGBRegressor(
        n_estimators=params["n_estimators"],
        max_depth=params["max_depth"],
        learning_rate=params["learning_rate"],
        random_state=params["random_state"],
    )
    model.fit(X_train, y_train)

    joblib.dump(model, MODEL_DIR / "model.joblib")

    ##save feature names too, need this for the model card later
    with open(MODEL_DIR / "features.json", "w") as f:
        json.dump(list(X_train.columns), f)

    print("Model trained and saved to model/model.joblib")


if __name__ == "__main__":
    main()
