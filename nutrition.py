from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_nutritional_plan():
    return {"nutrition": "Placeholder diet plan for high-performance swimming"}
