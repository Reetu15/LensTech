import os
import shutil
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.ai_engine import analyze_image_with_gemini

# Create the router
router = APIRouter(
    prefix="/api",
    tags=["Screenshot Analysis"]
)

@router.post("/analyze-screenshot/")
async def analyze_screenshot(
    image: UploadFile = File(...),
    prompt: str = Form("Analyze this screenshot in detail and explain what you see.")
):
    temp_file_path = f"temp_{image.filename}"
    
    # Save the file temporarily
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
        
    try:
        # Call the logic from our separate services file!
        analysis = analyze_image_with_gemini(temp_file_path, prompt)
        
        return {
            "status": "success",
            "filename": image.filename,
            "ai_analysis": analysis
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Clean up the temp file
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
