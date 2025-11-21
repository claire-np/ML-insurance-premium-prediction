from sklearn.ensemble import GradientBoostingRegressor

def train_gb(X_train, y_train):
    model = GradientBoostingRegressor(random_state=42)
    model.fit(X_train, y_train)
    return model
