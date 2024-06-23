from dotenv import load_dotenv
load_dotenv()
import os
import google.generativeai as genai
import streamlit as st

st.title("Plan with Me")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt="""You are a travel agent planner named TravelSensei.You are a chatbot that help people in searching for 
their trips now you have to provide them the answers of their questions based on the question provide in 100
words:
Try to make things more interactive and appropriate. """

def generate_hello_message(query ):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt + query)
    return response.text

