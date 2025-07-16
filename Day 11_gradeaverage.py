import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Day 11/50: Grade Average Calculator", page_icon="📝", layout="centered")

st.title("🦅 Day 11/50: Advanced Grade Average Calculator 📝")
st.write("Calculate and visualize your test scores average for effective study tracking.")

# User decides how many test scores
num_tests = st.slider("🖊️ How many test scores would you like to enter?", 3, 15, 5)

# Pass mark selection
pass_mark = st.number_input("✅ Set Pass Mark (%):", 0.0, 100.0, 40.0, step=1.0)

grades = [st.number_input(f"✍️ Enter Test Score {i+1}:", 0.0, 100.0, 0.0, step=1.0, key=f"grade_{i}") for i in range(num_tests)]

if st.button("📊 Calculate & Show Insights"):
    grades_array = np.array(grades)
    average = np.mean(grades_array)
    highest = np.max(grades_array)
    lowest = np.min(grades_array)
    result = "✅ Pass" if average >= pass_mark else "❌ Fail"

    # Metric cards for quick insights
    col1, col2, col3 = st.columns(3)
    col1.metric("📈 Average", f"{average:.2f}%")
    col2.metric("🏆 Highest", f"{highest:.2f}%")
    col3.metric("📉 Lowest", f"{lowest:.2f}%")

    st.markdown(
        f"""
        <div style="
            background-color: {'#4CAF50' if result == '✅ Pass' else '#f44336'};
            color: white;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;">
            {result}
        </div>
        """,
        unsafe_allow_html=True
    )

    # Progress bar showing how close to 100%
    st.write("### 📊 Progress Towards 100%")
    st.progress(min(int(average), 100))

    # DataFrame view
    df = pd.DataFrame({
        "Test Number": [f"Test {i+1}" for i in range(num_tests)],
        "Score (%)": grades
    })

    st.write("### 🗂️ Score Table")
    st.dataframe(df.style.background_gradient(cmap="YlGnBu"))

    # Histogram to visualize score distribution
    fig = px.histogram(
        df,
        x="Score (%)",
        nbins=10,
        title="📊 Distribution of Test Scores",
        color_discrete_sequence=["#636EFA"]
    )
    st.plotly_chart(fig, use_container_width=True)

    st.success("✅ Analysis completed! Use this to track your study performance.")

