from .rules import recommend_rules
from .ml import recommend_ml

def get_recommendations(profile: dict, k: int = 5, engine: str = "ml"):
    """
    Return a k-row DataFrame of foods for the given user profile.
    engine ∈ {"ml", "rules"}
    """
    if engine == "rules":
        return recommend_rules(profile, k)
    return recommend_ml(profile, k)
