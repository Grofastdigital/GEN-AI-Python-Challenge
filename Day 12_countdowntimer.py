import streamlit as st
import time
import plotly.graph_objs as go
import random

st.set_page_config(page_title="Day 12/50: Advanced Countdown Timer", page_icon="⏱️")

st.title("🦅 Day 12/50: Advanced Countdown Timer ⏱️")

# Session state for advanced control
if 'running' not in st.session_state:
    st.session_state.running = False
if 'paused' not in st.session_state:
    st.session_state.paused = False

seconds = st.slider("⏳ Select countdown time (seconds):", 5, 180, 15)

start_col, pause_col, reset_col = st.columns(3)

if start_col.button("🚀 Start / Resume"):
    st.session_state.running = True
    st.session_state.paused = False

if pause_col.button("⏸️ Pause"):
    st.session_state.paused = True

if reset_col.button("🔄 Reset"):
    st.session_state.running = False
    st.session_state.paused = False
    st.rerun()

progress_placeholder = st.empty()
gauge_placeholder = st.empty()
msg_placeholder = st.empty()

def get_color(progress):
    if progress < 0.33:
        return "red"
    elif progress < 0.66:
        return "orange"
    else:
        return "green"

motivational_quotes = [
    "✨ Keep pushing your limits!",
    "💡 Small steps build big momentum.",
    "🚀 You're closer than you think!",
    "🔥 Consistency is key!",
    "🎯 Stay focused and finish strong!"
]

if st.session_state.running and not st.session_state.paused:
    for i in range(seconds, -1, -1):
        if st.session_state.paused or not st.session_state.running:
            break

        progress = (seconds - i) / seconds

        progress_placeholder.progress(progress)

        # Plotly Gauge for circular aesthetic progress
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=i,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Seconds Remaining"},
            gauge={
                'axis': {'range': [0, seconds]},
                'bar': {'color': get_color(progress)},
                'steps': [
                    {'range': [0, seconds / 3], 'color': "#FFCCCC"},
                    {'range': [seconds / 3, 2 * seconds / 3], 'color': "#FFE5CC"},
                    {'range': [2 * seconds / 3, seconds], 'color': "#CCFFCC"}
                ]
            }
        ))
        gauge_placeholder.plotly_chart(fig, use_container_width=True)

        time.sleep(1)

    if not st.session_state.paused:
        st.balloons()
        msg_placeholder.success("⏰ **Time's Up!** Great job completing your countdown! 🚀")
        st.info(random.choice(motivational_quotes))
        st.session_state.running = False
