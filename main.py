import os
import shutil
from fastapi import FastAPI, UploadFile, File, Form
from google import genai

app = FastAPI(title="AI Screenshot Analyzer")

# The client automatically looks for an environment variable named 'GEMINI_API_KEY'
client = genai.Client() 

@app.post("/analyze-screenshot/")
async def analyze_screenshot(
    image: UploadFile = File(...),
    # You can pass custom instructions, or it defaults to this general prompt!
    prompt: str = Form("Analyze this screenshot in detail and explain what you see.")
):
    # 1. Save the incoming screenshot to a temporary file on the server
    temp_file_path = f"temp_{image.filename}"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
        
    try:
        # 2. Upload the screenshot to Gemini
        uploaded_image = client.upload(file=temp_file_path)
        
        # 3. Feed the image and the prompt to the Gemini 3.6 Flash model
        response = client.models.generate_content(
            model="gemini-3.6-flash", 
            contents=[uploaded_image, prompt]
        )
        
        # 4. Return the AI's insights!
        return {
            "status": "success",
            "filename": image.filename,
            "ai_analysis": response.text
        }
        
    except Exception as e:
        return {"status": "error", "message": str(e)}
        
    finally:
        # 5. Clean up the temporary file so our server doesn't get cluttered
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)