from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def generate_dryland_workout():
    return {"workout": "Placeholder dryland training for core strength"}
