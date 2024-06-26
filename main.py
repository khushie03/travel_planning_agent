import streamlit as st
from streamlit_option_menu import option_menu
from serpapi import GoogleSearch
from functions import chat_app

options = option_menu(
    menu_title="none",
    options=["Flight Searcher", "Chatbot", "Hotel Searcher"],
    icons=["chair", "info-circle", "link"],
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

if options == "Chatbot":
    chat_app()
