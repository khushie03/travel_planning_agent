# travel_planning_agent
Our platform is designed to be your ultimate companion in travel planning, offering a seamless experience for adventurers of all kinds. Whether you're dreaming of a quick getaway or embarking on a globe-trotting expedition, our tools and resources are here to simplify every step of your journey.

To create a README file for your GitHub repository based on the Streamlit app you've shared, you can include the following sections:

---

# Streamlit Travel App

This Streamlit app allows users to search for flights and hotels using the Google Search API through the SerpApi service. It features different functionalities based on user selection:

## Features

### Flight Searcher

- **Inputs:**
  - Onboard date and return date selection
  - Currency selection
  - Current location and destination entry

- **Functionality:**
  - Searches for flights between the selected locations and dates
  - Displays flight details including airline, departure/arrival times, duration, travel class, and price

### Chatbot

- **Functionality:**
  - Launches a chatbot interface for user interaction
  - Gives you travel suggestions and here you are able to interact with it in any language.
  - Make your travel allowances more affordable and memorable.

### Hotel Searcher

- **Inputs:**
  - Search query for hotels
  - Check-in and check-out date selection
  - Number of adults and currency selection

- **Functionality:**
  - Searches for hotels based on the query and dates
  - Displays hotel details including name, description, rate per night, check-in/check-out times, and images

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/khushie03/travel_planning_agent.git
   cd https://github.com/khushie03/travel_planning_agent
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Configuration

Ensure you have obtained an API key from [SerpApi](https://serpapi.com/) and replace `"YOUR_API_KEY"` in `app.py` with your actual API key.

  

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



Feel free to customize this template further based on your specific app details and preferences.
