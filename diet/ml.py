import joblib
import pandas as pd

FOODS = pd.read_csv("data/processed/foods_clean.csv")
PIPE = joblib.load("model/diet_model.pkl")

def recommend_ml(profile: dict, k: int = 5):
    """Return top-k foods with highest predicted score (probability)."""
    X_all = FOODS.drop(columns=["target"], errors="ignore")
    proba = PIPE.predict_proba(X_all)[:, 1]
    FOODS["score"] = proba
    top = FOODS.sort_values("score", ascending=False).head(k)
    return top.reset_index(drop=True)
