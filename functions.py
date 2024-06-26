import streamlit as st
from chatbot import generate_message
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



def create_html_file(hotels):
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hotel Information</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
            }}
            .hotel-card {{
                border: 1px solid #ccc;
                border-radius: 8px;
                padding: 20px;
                margin-bottom: 20px;
            }}
            .hotel-card img {{
                max-width: 100px;
                vertical-align: middle;
            }}
            .hotel-card h3 {{
                margin: 0;
                font-size: 1.2em;
            }}
        </style>
    </head>
    <body>
        <h1>Hotel Information</h1>
        {hotel_details}
    </body>
    </html>
    """

    hotel_details = ""

    def generate_hotel_card(hotel):
        name = hotel['name']
        description = hotel.get('description', 'No description available')
        link = hotel.get('link', '#')
        logo = hotel.get('logo', '')
        rate_per_night = hotel.get('rate_per_night', {}).get('lowest', 'N/A')
        check_in_time = hotel.get('check_in_time', 'N/A')
        check_out_time = hotel.get('check_out_time', 'N/A')
        
        return f"""
        <div class="hotel-card">
            <h3>{name}</h3>
            <img src="{logo}" alt="{name} logo">
            <p><strong>Description:</strong> {description}</p>
            <p><strong>Rate per Night:</strong> {rate_per_night}</p>
            <p><strong>Check-in Time:</strong> {check_in_time}</p>
            <p><strong>Check-out Time:</strong> {check_out_time}</p>
            <p><a href="{link}">More details</a></p>
        </div>
        """

    for hotel in hotels:
        hotel_details += generate_hotel_card(hotel)

    html_content = html_template.format(hotel_details=hotel_details)

    with open("hotel_search_results.html", "w", encoding="utf-8") as file:
        file.write(html_content)

