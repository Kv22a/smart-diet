import pandas as pd, pathlib, numpy as np

RAW_PATH = pathlib.Path("data/raw/indian_food.csv")
OUT_PATH = pathlib.Path("data/processed/foods_clean.csv")

# Load the data
df = pd.read_csv(RAW_PATH)

# 1️⃣ Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# 2️⃣ Convert time columns to numeric
df["prep_time"] = pd.to_numeric(df["prep_time"], errors="coerce")
df["cook_time"] = pd.to_numeric(df["cook_time"], errors="coerce")

# 3️⃣ Drop rows with missing times
df = df.dropna(subset=["prep_time", "cook_time"])

# 4️⃣ Add total_time and quick_recipe flag
df["total_time"] = df["prep_time"] + df["cook_time"]
df["quick_recipe"] = (df["total_time"] < 30).astype(int)

# 5️⃣ Save cleaned data
OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUT_PATH, index=False)

print("✅ Saved cleaned file:", OUT_PATH)

