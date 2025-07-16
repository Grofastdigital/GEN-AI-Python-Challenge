import streamlit as st

st.title("🦅 Day 1/50 — Personal Greeting")

st.write("Welcome Eagle! Let's craft your personalized message.")

name = st.text_input("💬 Enter your name:")
age = st.number_input("🎂 Enter your age:", min_value=0, max_value=120, step=1)
color = st.color_picker("🎨 Pick your favorite color:")

if st.button("✨ Generate Greeting"):
    if name:
        st.markdown(
            f"<h3 style='color:{color}'>Hey {name}! 🦅</h3>"
            f"<p style='color:{color}'>At {age} years young, your vibe matches your favorite color beautifully!</p>"
            f"<p style='color:{color}'>#FlyHighwithAI ✨</p>",
            unsafe_allow_html=True
        )
    else:
        st.warning("Please enter your name to receive your greeting.")
