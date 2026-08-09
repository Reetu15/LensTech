import streamlit as st
import requests

# Set up the look of the webpage
st.set_page_config(page_title="LensTech AI", page_icon="🔍", layout="centered")

st.title("🔍 LensTech Screenshot Analyzer")
st.write("Upload a screenshot, and our AI will instantly analyze and summarize it.")

# The URL of your live Render backend!
API_URL = "https://lenstech.onrender.com/api/analyze-screenshot/"

# Create a file uploader on the screen
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

# Custom prompt input for the user
user_prompt = st.text_input("What should the AI look for?", value="Summarize the main point of this screenshot in exactly one short sentence.")

# Create an "Analyze" button
if st.button("Analyze Image"):
    if uploaded_file is not None:
        with st.spinner("LensTech AI is analyzing your image..."):
            # Prepare the image and prompt to send to your Render API
            files = {"image": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
            data = {"prompt": user_prompt}
            
            try:
                # Send the request to your backend
                response = requests.post(API_URL, files=files, data=data)
                
                if response.status_code == 200:
                    # Success! Show the AI's answer
                    result = response.json()
                    st.success("Analysis Complete!")
                    st.markdown("### AI Summary:")
                    st.write(result["ai_analysis"])
                else:
                    st.error(f"Backend Error: {response.status_code}")
                    
            except Exception as e:
                st.error("Could not connect to the LensTech backend. Is Render awake?")
    else:
        st.warning("Please upload an image first!")
