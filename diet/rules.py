import pandas as pd

# Load the cleaned food data
FOODS = pd.read_csv("data/processed/foods_clean.csv")

def recommend_rules(profile: dict, k: int = 5) -> pd.DataFrame:
    """
    profile = {
        "bmi": 27.3,
        "age": 24,
        "conditions": ["Diabetes", "High Blood Pressure"]
    }
    """
    df = FOODS.copy()

    # --- Calorie filter ---
    if profile["bmi"] > 25:
        if "calories" in df.columns:
            df = df[df["calories"] <= 500]

    # --- Condition filters ---
    if "Diabetes" in profile["conditions"]:
        if "diabeticfriendly" in df.columns:
            df = df[df["diabeticfriendly"] == 1]

    if "High Blood Pressure" in profile["conditions"]:
        if "sodium_mg" in df.columns:
            df = df[df["sodium_mg"] < 400]

    # --- Fallback if all filtered out ---
    if df.empty:
        df = FOODS.sample(k)

    return df.sample(min(k, len(df))).reset_index(drop=True)
