import sys
import os

# Add the project root to Python path so 'diet_rules' can be found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from diet_rules import recommend_rules

def test_rules_returns_rows():
    profile = {"bmi": 30, "age": 22, "conditions": ["Diabetes"]}
    df = recommend_rules(profile, k=3)
    assert len(df) == 3
