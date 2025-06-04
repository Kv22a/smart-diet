import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from diet import get_recommendations

def test_ml_scores_descending():
    df = get_recommendations({"bmi": 22, "conditions": []}, k=5, engine="ml")
    assert df["score"].is_monotonic_decreasing
