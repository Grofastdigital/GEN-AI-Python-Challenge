import streamlit as st

st.set_page_config(page_title="Day 2/50: Visual Calculator", page_icon="🦅", layout="centered")

st.title("🦅 Day 2/50: Visual Calculator 🧮")
st.write("Welcome Eagle! Calculate smartly with colors and style.")

# Initialize history in session state
if "history" not in st.session_state:
    st.session_state.history = []

# Color mapping for operations
color_map = {
    "Addition": "#4CAF50",         # Green
    "Subtraction": "#F44336",      # Red
    "Multiplication": "#2196F3",   # Blue
    "Division": "#FF9800"          # Orange
}

emoji_map = {
    "Addition": "➕",
    "Subtraction": "➖",
    "Multiplication": "✖️",
    "Division": "➗"
}

num1 = st.number_input("🔢 Enter First Number:")
num2 = st.number_input("🔢 Enter Second Number:")
operation = st.radio("⚙️ Choose Operation:", ["Addition", "Subtraction", "Multiplication", "Division"], horizontal=True)

if st.button("✨ Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    else:
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Undefined (division by zero) ⚠️"

    # Save to history if valid
    if isinstance(result, (int, float)):
        history_entry = f"{emoji_map[operation]} {num1} {operation} {num2} = {result}"
        st.session_state.history.append(history_entry)

    # Display with colored and gradient result
    if isinstance(result, (int, float)):
        st.markdown(
            f"""
            <div style="
                background: linear-gradient(135deg, {color_map[operation]} 0%, #ffffff 100%);
                padding: 20px;
                border-radius: 12px;
                text-align: center;
                color: #000000;
                font-size: 24px;
                font-weight: bold;
                border: 3px solid {color_map[operation]};
                ">
                {emoji_map[operation]} Result of {operation}: {result}
            </div>
            """,
            unsafe_allow_html=True
        )
        st.balloons()
    else:
        st.error(result)

# Display calculation history
if st.session_state.history:
    with st.expander("📜 View Calculation History"):
        for calc in reversed(st.session_state.history[-10:]):
            st.write(calc)
