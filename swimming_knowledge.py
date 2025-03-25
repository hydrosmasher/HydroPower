from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def swimming_facts():
    return {"fact": "Placeholder swimming fact about Olympic records"}
