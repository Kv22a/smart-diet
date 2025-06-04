from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List
from diet import get_recommendations

app = FastAPI(title="Smart Diet API", version="0.1.0")

class Profile(BaseModel):
    age: int = Field(..., gt=0, lt=120)
    bmi: float = Field(..., gt=10, lt=60)
    conditions: List[str] = []

class Result(BaseModel):
    name: str
    calories: float
    protein_g: float
    fat_g: float
    carbs_g: float

@app.post("/recommend", response_model=List[Result])
def recommend(profile: Profile, k: int = 5, engine: str = "ml"):
    df = get_recommendations(profile.model_dump(), k=k, engine=engine)
    return df[["name", "calories", "protein_g", "fat_g", "carbs_g"]].to_dict(orient="records")
