"""
Core recommendation logic.
Implement recommend_rules() or ML-based recommend_ml().
"""

from diet_rules import recommend_rules
from diet_ml import recommend_ml

def get_recommendations(profile, k=5, engine="ml"):
    if engine == "rules":
        return recommend_rules(profile, k)
    return recommend_ml(profile, k)

