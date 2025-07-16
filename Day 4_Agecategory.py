import streamlit as st

st.set_page_config(page_title="Day 4/50: Age Category Checker", page_icon="🦅", layout="centered")

st.title("🦅 Day 4/50: Age Category Checker 🎂")
st.write("Welcome Eagle! Enter your age below to discover your category with style.")

# Initialize history
if "day4_history" not in st.session_state:
    st.session_state.day4_history = []

age = st.number_input("🎂 Enter your age:", 0, 120, 25)

if st.button("✨ Check Category"):
    if age <= 12:
        category = "Child 🧒"
        color = "#2196F3"  # Blue
        message = "Enjoy your playful days and keep smiling! 🌈"
        trigger = "balloons"
    elif 13 <= age <= 19:
        category = "Teenager 🧑‍🎓"
        color = "#9C27B0"  # Purple
        message = "Stay curious and keep learning! 🚀"
        trigger = "balloons"
    elif 20 <= age <= 59:
        category = "Adult 👨‍💼"
        color = "#4CAF50"  # Green
        message = "Keep striving and growing! 💼"
        trigger = None
    else:
        category = "Senior 👴"
        color = "#607D8B"  # Gray
        message = "Your wisdom is your superpower! 🦉"
        trigger = "snow"

    # Fancy gradient display card
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, {color} 0%, #ffffff 100%);
            padding: 20px;
            border-radius: 15px;
            border: 3px solid {color};
            text-align: center;
            box-shadow: 0 0 15px {color};
        ">
            <h2 style="color:#000000; font-size: 28px;">{category}</h2>
            <p style="font-size: 20px;">{message}</p>
            <p style="font-size: 16px; color: #333;">You are {age} years old.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Celebrate based on category
    if trigger == "balloons":
        st.balloons()
    elif trigger == "snow":
        st.snow()

    # Save to history
    st.session_state.day4_history.append({
        "age": age,
        "category": category
    })

# Show history
if st.session_state.day4_history:
    with st.expander("📜 View History"):
        for idx, entry in enumerate(reversed(st.session_state.day4_history[-5:]), 1):
            st.write(f"{idx}. Age: **{entry['age']}** ➔ {entry['category']}")

