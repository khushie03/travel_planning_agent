import streamlit as st
from chatbot  import generate_message
from serpapi import GoogleSearch
def chat_app():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    prompt = st.chat_input("Say something")
    if prompt:
        st.write(f"User has sent the following prompt: {prompt}")
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.markdown(prompt)
        
        response = generate_message(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        with st.chat_message("assistant"):
            st.markdown(response)



params = {
  "engine": "google_flights",
  "departure_id": "PEK",
  "arrival_id": "AUS",
  "outbound_date": "2024-06-26",
  "return_date": "2024-07-02",
  "currency": "USD",
  "hl": "en",
  "api_key": "c8b912a9727723424bffac813a03eb897d43cee8cfac0741c3b266a6cb8bef71"
}

search = GoogleSearch(params)
results = search.get_dict()