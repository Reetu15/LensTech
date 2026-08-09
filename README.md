# 🔍 LensTech: AI Screenshot Analyzer

LensTech is a full-stack web application that leverages advanced artificial intelligence to instantly analyze and summarize uploaded screenshots. 

## 🌐 Live Application
* **Frontend App:** [https://lenstech.streamlit.app]
* **Backend API Docs:** [https://lenstech.onrender.com/docs]

## 🏗️ Architecture & Tech Stack
This project is built with a modular architecture, strictly separating the user interface from the API routing and AI services.

* **Frontend:** Streamlit (Hosted on Streamlit Community Cloud)
* **Backend:** FastAPI, Python (Hosted on Render)
* **AI Engine:** Google Generative AI (`gemini-3.5-flash`)
* **Libraries:** `requests`, `python-multipart`, `uvicorn`

## 🚀 How It Works
1. A user uploads an image via the Streamlit interface.
2. The Streamlit app sends the image buffer via a secure HTTP POST request to the FastAPI backend.
3. The FastAPI router intercepts the payload and passes it to a dedicated AI service module.
4. The service module utilizes the Google Gen AI SDK to process the image and extract key insights.
5. The processed summary is returned as a JSON response and rendered instantly on the frontend.
