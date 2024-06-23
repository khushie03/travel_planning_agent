import streamlit as st
from streamlit_option_menu import option_menu
from chatbot import generate_hello_message

st.set_page_config(
    page_title="travelplanner",
    page_icon=":map:",
    layout="wide"
)

st.title("TravelSensei")

options = option_menu("Select page",
                      options=["Chatbot", "Flight Searcher" , "Hotel Search"],
                      icons=["robot", "airplane", "house"],
                      orientation="horizontal")

def chat_app():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    prompt = st.chat_input("Say something")
    if prompt:
        st.write(f"User has sent the following prompt: {prompt}")
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.markdown(prompt)
        
        response = generate_hello_message(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        with st.chat_message("assistant"):
            st.markdown(response)
    
    
