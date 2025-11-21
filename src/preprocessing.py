import numpy as np
import pandas as pd

def engineer_features(df):
    df["log_charges"] = np.log1p(df["charges"])
    df = pd.get_dummies(df, columns=["sex", "smoker", "region"], drop_first=True)
    df["bmi_smoker"] = df["bmi"] * df["smoker_yes"]
    return df
