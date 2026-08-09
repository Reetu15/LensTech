from google import genai

# The client automatically looks for the GEMINI_API_KEY environment variable
client = genai.Client() 

def analyze_image_with_gemini(file_path: str, prompt: str) -> str:
    """Uploads an image to Gemini and returns the generated text analysis."""
    
    # 1. Upload the screenshot to Gemini
    uploaded_image = client.files.upload(file=file_path)
    
    # 2. Feed the image and the prompt to the Gemini 3.6 Flash model
    response = client.models.generate_content(
       model="gemini-1.5-flash",
        contents=[uploaded_image, prompt]
    )
    
    return response.text
