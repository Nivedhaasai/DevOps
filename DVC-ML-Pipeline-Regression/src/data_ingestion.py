"""
Stage 1: Data Ingestion
------------------------
Loads the scikit-learn Diabetes dataset (regression: quantitative measure of
disease progression one year after baseline) and dumps it as a raw CSV file.

Output:
    data/raw/data.csv
"""

import os
import pandas as pd
from sklearn.datasets import load_diabetes


def load_data() -> pd.DataFrame:
    """Load the sklearn diabetes dataset into a DataFrame."""
    bunch = load_diabetes(as_frame=True)
    df = bunch.frame  #includes feature columns + 'target'
    return df


def save_raw_data(df: pd.DataFrame, out_dir: str = "data/raw") -> None:
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "data.csv")
    df.to_csv(out_path, index=False)
    print(f"[data_ingestion] Saved raw data -> {out_path} (shape={df.shape})")


def main():
    df = load_data()
    save_raw_data(df)


if __name__ == "__main__":
    main()
