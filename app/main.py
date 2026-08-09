from fastapi import FastAPI
from app.routers import analyze

app = FastAPI(title="ScreenSense AI")

# Link our separate routing file to the main application
app.include_router(analyze.router)

@app.get("/")
def read_root():
    return {"status": "online", "message": "The AI Screenshot Analyzer is running!"}
