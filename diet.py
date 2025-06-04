"""
Core recommendation logic.
Implement recommend_rules() or ML-based recommend_ml().
"""

from diet_rules import recommend_rules

def get_recommendations(profile, k=5):
    return recommend_rules(profile, k)
