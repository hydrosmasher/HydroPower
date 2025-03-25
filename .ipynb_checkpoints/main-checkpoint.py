from fastapi import FastAPI
from swim_workout import router as swim_router
from dryland_workout import router as dryland_router
from pace_analysis import router as pace_router
from injury_advice import router as injury_router
from nutrition import router as nutrition_router
from swimming_knowledge import router as knowledge_router

app = FastAPI(title="HydroPower API", description="AI-Powered Swimming Assistant", version="1.0")

# Include all service routers
app.include_router(swim_router, prefix="/swim")
app.include_router(dryland_router, prefix="/dryland")
app.include_router(pace_router, prefix="/pace")
app.include_router(injury_router, prefix="/injury")
app.include_router(nutrition_router, prefix="/nutrition")
app.include_router(knowledge_router, prefix="/knowledge")

@app.get("/")
async def root():
    return {"message": "Welcome to HydroPower API! 🌊🚀"}

