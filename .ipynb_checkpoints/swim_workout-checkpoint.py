from fastapi import APIRouter, Query
import pandas as pd
import random

router = APIRouter()

# Load the updated workout dataset
csv_filename = "/mnt/data/swim_workout_data.csv"
df = pd.read_csv(csv_filename)

@router.get("/")
async def generate_swim_workout(
    stroke: str = Query("freestyle", enum=["freestyle", "backstroke", "breaststroke", "sprint", "IM"]),
    intensity: str = Query("moderate", enum=["easy", "moderate", "high", "max effort"])
):
    """
    Returns a recommended workout based on stroke type and training intensity.
    """
    filtered_workouts = df[(df["Stroke"].str.lower() == stroke.lower()) & (df["Intensity"].str.lower() == intensity.lower())]

    if filtered_workouts.empty:
        return {"message": "No matching workouts found. Try a different intensity or stroke."}

    selected_workout = filtered_workouts.sample(n=1).to_dict(orient="records")[0]

    return {
        "session": selected_workout["Session"],
        "stroke": selected_workout["Stroke"],
        "training_type": selected_workout["Training Type"],
        "intensity": selected_workout["Intensity"],
        "distance": selected_workout["Distance"],
        "reps": selected_workout["Reps"],
        "rest_time": selected_workout["Rest Time"],
        "equipment": selected_workout["Equipment"],
        "notes": selected_workout["Notes"]
    }
