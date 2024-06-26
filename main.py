import streamlit as st
from streamlit_option_menu import option_menu
from serpapi import GoogleSearch
import os
from functions import chat_app, create_html_file

options = option_menu(
    menu_title=None,
    options=["Flight Searcher", "Chatbot", "Hotel Searcher"],
    icons=["airplane", "info-circle", "hotel"],
    orientation="horizontal",
)

def generate_flight_card(flight):
    departure = flight['departure_airport']
    arrival = flight['arrival_airport']
    airline_logo = flight['airline_logo']
    airline = flight['airline']
    duration = flight['duration']
    flight_number = flight['flight_number']
    travel_class = flight['travel_class']
    price = flight.get('price', 'N/A')
    often_delayed = "Yes" if flight.get('often_delayed_by_over_30_min') else "No"
    
    return f"""
    <div class="flight-card">
        <h3>Flight {flight_number}</h3>
        <img src="{airline_logo}" alt="{airline} logo">
        <p><strong>Airline:</strong> {airline}</p>
        <p><strong>Departure:</strong> {departure['name']} ({departure['id']}) at {departure['time']}</p>
        <p><strong>Arrival:</strong> {arrival['name']} ({arrival['id']}) at {arrival['time']}</p>
        <p><strong>Duration:</strong> {duration} minutes</p>
        <p><strong>Travel Class:</strong> {travel_class}</p>
        <p><strong>Price:</strong> {price}</p>
        <p><strong>Often Delayed:</strong> {often_delayed}</p>
    </div>
    """

if options == "Flight Searcher":
    onboard_date = st.date_input("Enter the onboard date")
    return_date = st.date_input("Enter the return date")
    currency = st.selectbox("Select Currency", ["USD", "INR"])
    current_location = st.text_input("Enter your current location")
    destination = st.text_input("Enter your destination")

    if st.button("Search Flights"):
        params = {
            "engine": "google_flights",
            "departure_id": current_location,
            "arrival_id": destination,
            "outbound_date": str(onboard_date),
            "return_date": str(return_date),
            "currency": currency,
            "hl": "en",
            "api_key": "c8b912a9727723424bffac813a03eb897d43cee8cfac0741c3b266a6cb8bef71"
        }
        
        search = GoogleSearch(params)
        results = search.get_dict()

        flight_details = ""

        if 'best_flights' in results:
            for best_flight in results['best_flights']:
                for flight in best_flight['flights']:
                    flight_details += generate_flight_card(flight)

        if 'other_flights' in results:
            for other_flight in results['other_flights']:
                for flight in other_flight['flights']:
                    flight_details += generate_flight_card(flight)

        if flight_details:
            st.markdown("""
            <style>
                .flight-card {
                    border: 1px solid #ccc;
                    border-radius: 8px;
                    padding: 20px;
                    margin-bottom: 20px;
                }
                .flight-card img {
                    max-width: 50px;
                    vertical-align: middle;
                }
                .flight-card h3 {
                    margin: 0;
                    font-size: 1.2em;
                }
            </style>
            """, unsafe_allow_html=True)
            st.markdown(flight_details, unsafe_allow_html=True)
        else:
            st.info("No flight details available.")


def generate_hotel_card(hotel):
    name = hotel['name']
    description = hotel.get('description', 'No description available')
    link = hotel.get('link', '#')
    
    rate_per_night = hotel.get('rate_per_night', {}).get('lowest', 'N/A')
    check_in_time = hotel.get('check_in_time', 'N/A')
    check_out_time = hotel.get('check_out_time', 'N/A')
    images = hotel.get('images', [])
    image_gallery = ""
    for image in images:
        thumbnail = image.get('thumbnail', '')
        image_gallery += f'<img src="{thumbnail}" alt="{name} thumbnail" style="max-width:100px; margin:5px;">'
    return f"""
    <div class="hotel-card">
        <h3>{name}</h3>
        <div class="image-gallery">
            {image_gallery}
        </div>
        <p><strong>Description:</strong> {description}</p>
        <p><strong>Rate per Night:</strong> {rate_per_night}</p>
        <p><strong>Check-in Time:</strong> {check_in_time}</p>
        <p><strong>Check-out Time:</strong> {check_out_time}</p>
        <p><a href="{link}">More details</a></p>
    </div>
    """

if options == "Chatbot":
    chat_app()

if options == "Hotel Searcher":
    query = st.text_input("Enter your search query")
    check_in_date = st.date_input("Enter the check-in date")
    check_out_date = st.date_input("Enter the check-out date")
    num_persons = st.number_input("Enter number of adults", min_value=1, step=1)
    currency = st.selectbox("Select Currency", ["USD", "INR"])

    if st.button("Search Hotels"):
        params = {
            "engine": "google_hotels",
            "q": query,
            "check_in_date": str(check_in_date),
            "check_out_date": str(check_out_date),
            "adults": num_persons,
            "currency": currency,
            "gl": "us",
            "hl": "en",
            "api_key": "c8b912a9727723424bffac813a03eb897d43cee8cfac0741c3b266a6cb8bef71"
        }

        search = GoogleSearch(params)
        results = search.get_dict()

        if 'properties' in results:
            hotel_details = ""
            for hotel in results['properties']:
                hotel_details += generate_hotel_card(hotel)

            st.markdown("""
            <style>
                .hotel-card {
                    border: 1px solid #ccc;
                    border-radius: 8px;
                    padding: 20px;
                    margin-bottom: 20px;
                }
                .hotel-card img {
                    max-width: 100px;
                    vertical-align: middle;
                }
                .hotel-card h3 {
                    margin: 0;
                    font-size: 1.2em;
                }
            </style>
            """, unsafe_allow_html=True)
            st.markdown(hotel_details, unsafe_allow_html=True)
        else:
            st.info("No hotel details available.")
