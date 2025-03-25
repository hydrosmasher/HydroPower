from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def injury_advice():
    return {"advice": "Placeholder injury prevention tips for swimmers"}
