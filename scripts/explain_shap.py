import shap
import pandas as pd
import joblib

# Load data and model
df = pd.read_csv("data/processed/foods_clean.csv")
model = joblib.load("model/diet_model.pkl")

# Match the same features used during training
num_cols = ["calories", "protein_g", "fat_g", "carbs_g"]
cat_cols = ["diet", "flavor_profile", "course"]
cat_cols = [col for col in cat_cols if col in df.columns]
X = df[num_cols + cat_cols]

# Sample 200 rows
X_sample = X.sample(200, random_state=0)

# Preprocess like in training
pre = model.named_steps["pre"]
X_transformed = pre.transform(X_sample)

# Get the classifier and explain
clf = model.named_steps["clf"]
explainer = shap.TreeExplainer(clf)
shap_values = explainer.shap_values(X_transformed)

# Plot (bar chart of feature importance)
shap.summary_plot(
    shap_values,
    X_transformed,
    plot_type="bar",
    feature_names=pre.get_feature_names_out()
)
