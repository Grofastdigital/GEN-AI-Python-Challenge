import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Day 6/50: Number Comparison", page_icon="🔍", layout="centered")

st.title("🦅 Day 6/50: Number Comparison 🔍")
st.write("Welcome Eagle! Enter three numbers to compare, rank, and visualize easily.")

# Inputs
num1 = st.number_input("🔢 Enter First Number:", value=0.0, step=1.0)
num2 = st.number_input("🔢 Enter Second Number:", value=0.0, step=1.0)
num3 = st.number_input("🔢 Enter Third Number:", value=0.0, step=1.0)

if st.button("✨ Compare & Rank"):
    numbers = [num1, num2, num3]
    labels = ["First Number", "Second Number", "Third Number"]

    # Ranking
    sorted_indices = sorted(range(len(numbers)), key=lambda i: numbers[i], reverse=True)
    ranking = ["🥇 1st", "🥈 2nd", "🥉 3rd"]

    st.write("### 🏆 Rankings")
    for rank, idx in zip(ranking, sorted_indices):
        st.write(f"{rank}: **{labels[idx]}** with value `{numbers[idx]}`")

    # Highlight highest and lowest
    highest = numbers[sorted_indices[0]]
    lowest = numbers[sorted_indices[-1]]

    col1, col2 = st.columns(2)
    col1.success(f"🔝 Highest: `{highest}`")
    col2.error(f"🔻 Lowest: `{lowest}`")

    # Create DataFrame for bar chart
    df = pd.DataFrame({
        "Label": labels,
        "Value": numbers
    })

    fig = px.bar(
        df,
        x="Label",
        y="Value",
        color="Value",
        text="Value",
        color_continuous_scale="Viridis",
        title="📊 Number Comparison Chart"
    )
    fig.update_traces(textposition="outside")
    fig.update_layout(yaxis=dict(title="Value"))

    st.plotly_chart(fig, use_container_width=True)

    # Tip based on comparison
    if highest == lowest:
        st.info("⚖️ All values are equal.")
    else:
        st.info("💡 Tip: Use this to compare marks, expenses, or KPI metrics visually.")

