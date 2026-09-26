import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model/passenger_satisfaction_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Airline Passenger Satisfaction Prediction System",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ Airline Passenger Satisfaction Prediction System")
st.write("Enter passenger and flight details to predict customer satisfaction.")

# -----------------------------
# Passenger Information
# -----------------------------
with st.expander("👤 Passenger Information", expanded=True):

    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox(
            "Gender",
            ["Female", "Male"]
        )

        travel_type = st.selectbox(
            "Type of Travel",
            ["Business travel", "Personal Travel"]
        )

    with col2:
        customer_type = st.selectbox(
            "Customer Type",
            ["Loyal Customer", "disloyal Customer"]
        )

        travel_class = st.selectbox(
            "Class",
            ["Business", "Eco", "Eco Plus"]
        )

    with col3:
        age = st.number_input(
            "Age",
            min_value=7,
            max_value=100,
            value=30
        )

        flight_distance = st.number_input(
            "Flight Distance",
            min_value=0,
            value=1000
        )

# -----------------------------
# Service Ratings
# -----------------------------
with st.expander("⭐ Service Ratings (0–5)", expanded=True):

    col1, col2, col3 = st.columns(3)

    with col1:
        wifi = st.slider("Inflight Wifi Service", 0, 5, 3)

        departure_arrival = st.slider(
            "Departure/Arrival Time Convenient",
            0, 5, 3
        )

        online_booking = st.slider(
            "Ease of Online Booking",
            0, 5, 3
        )

        gate_location = st.slider(
            "Gate Location",
            0, 5, 3
        )

        food_drink = st.slider(
            "Food and Drink",
            0, 5, 3
        )

    with col2:
        online_boarding = st.slider(
            "Online Boarding",
            0, 5, 3
        )

        seat_comfort = st.slider(
            "Seat Comfort",
            0, 5, 3
        )

        entertainment = st.slider(
            "Inflight Entertainment",
            0, 5, 3
        )

        onboard_service = st.slider(
            "On-board Service",
            0, 5, 3
        )

        legroom = st.slider(
            "Leg Room Service",
            0, 5, 3
        )

    with col3:
        baggage = st.slider(
            "Baggage Handling",
            0, 5, 3
        )

        checkin = st.slider(
            "Check-in Service",
            0, 5, 3
        )

        inflight_service = st.slider(
            "Inflight Service",
            0, 5, 3
        )

        cleanliness = st.slider(
            "Cleanliness",
            0, 5, 3
        )

# -----------------------------
# Flight Details
# -----------------------------
with st.expander("🛫 Flight Details", expanded=True):

    col1, col2 = st.columns(2)

    with col1:
        departure_delay = st.number_input(
            "Departure Delay in Minutes",
            min_value=0,
            value=0
        )

    with col2:
        arrival_delay = st.number_input(
            "Arrival Delay in Minutes",
            min_value=0,
            value=0
        )

# -----------------------------
# Prediction
# -----------------------------
if st.button("🔮 Predict Satisfaction"):

    # Feature engineering exactly as notebook
    total_delay = (
        departure_delay +
        arrival_delay
    )

    delayed_flight = int(total_delay > 15)

    service_ratings = [
        wifi,
        online_booking,
        gate_location,
        food_drink,
        online_boarding,
        seat_comfort,
        entertainment,
        onboard_service,
        legroom,
        baggage,
        checkin,
        inflight_service,
        cleanliness
    ]

    average_service_rating = sum(service_ratings) / len(service_ratings)

    long_haul = int(flight_distance > 3000)

    # Exact features used by the training notebook
    input_df = pd.DataFrame([{

        # Skewed features
        "Flight Distance": flight_distance,
        "Departure Delay in Minutes": departure_delay,
        "Arrival Delay in Minutes": arrival_delay,
        "Total_Delay": total_delay,

        # Scaling features
        "Age": age,
        "Average_Service_Rating": average_service_rating,

        # Discrete features
        "Inflight wifi service": wifi,
        "Departure/Arrival time convenient": departure_arrival,
        "Ease of Online booking": online_booking,
        "Gate location": gate_location,
        "Food and drink": food_drink,
        "Online boarding": online_boarding,
        "Seat comfort": seat_comfort,
        "Inflight entertainment": entertainment,
        "On-board service": onboard_service,
        "Leg room service": legroom,
        "Baggage handling": baggage,
        "Checkin service": checkin,
        "Inflight service": inflight_service,
        "Cleanliness": cleanliness,
        "Delayed_Flight": delayed_flight,
        "Long_Haul": long_haul,

        # Categorical features
        "Gender": gender,
        "Customer Type": customer_type,
        "Type of Travel": travel_type,
        "Class": travel_class
    }])

    # Prediction
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]

    confidence = probability[prediction] * 100

    st.markdown("---")
    st.subheader("Prediction Result")

    if prediction == 1:

        st.success(
            f"😊 **Satisfied Passenger**\n\n"
            f"Confidence: **{confidence:.2f}%**"
        )

    else:

        st.error(
            f"☹️ **Neutral or Dissatisfied Passenger**\n\n"
            f"Confidence: **{confidence:.2f}%**"
        )