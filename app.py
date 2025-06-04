import streamlit as st

from diet import get_recommendations

st.set_page_config("Smart Diet 🍎", page_icon="🍎", layout="wide")

st.title("🍎 Smart Diet & Food Recommender")

with st.sidebar:
    st.header("Your Profile")
    age  = st.number_input("Age", 1, 100, 25)
    h_cm = st.number_input("Height (cm)", 120, 220, 170)
    w_kg = st.number_input("Weight (kg)", 30, 200, 70)
    conditions = st.multiselect(
        "Health Conditions",
        ["Diabetes", "High Blood Pressure", "PCOD", "None"]
    )
    engine = st.selectbox("Algorithm", ["ml", "rules"])
    k      = st.slider("Meals to show", 3, 10, 5)

bmi = w_kg / (h_cm/100)**2
st.write(f"**BMI:** {bmi:.1f}")

if st.button("Get Recommendations"):
    profile = {"age": age, "bmi": bmi, "conditions": conditions}
    df = get_recommendations(profile, k=k, engine=engine)
    st.dataframe(df, use_container_width=True)
