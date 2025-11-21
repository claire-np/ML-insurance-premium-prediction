import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def evaluate_model(model, X_test, y_test):
    y_pred_log = model.predict(X_test)

    y_pred = np.expm1(y_pred_log)
    y_true = np.expm1(y_test)

    return {
        "r2": r2_score(y_test, y_pred_log),
        "mae": mean_absolute_error(y_true, y_pred),
        "rmse": np.sqrt(mean_squared_error(y_true, y_pred))
    }
