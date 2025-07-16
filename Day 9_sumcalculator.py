import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Day 9/50: Advanced Sum Calculator", page_icon="➕", layout="centered")

st.title("🦅 Day 9/50: Advanced Sum Calculator ➕")
st.write("Calculate sums in a range with visualization and insights for your practice and learning.")

# Inputs
col1, col2 = st.columns(2)
with col1:
    a = st.number_input("🔢 Start of range (a):", 0, 100000, 1)
with col2:
    b = st.number_input("🔢 End of range (b):", 1, 100000, 10)

mode = st.radio(
    "✨ What would you like to calculate?",
    ["Total Sum", "Sum of Even Numbers", "Sum of Odd Numbers"]
)

if st.button("🧮 Calculate"):
    if a > b:
        st.error("❌ The start of the range should not be greater than the end.")
    elif b - a > 15000:
        st.error("⚠️ Range too large for visualization. Please use a smaller range (max 15,000 numbers) to ensure smooth performance.")
    else:
        nums = list(range(a, b + 1))
        if mode == "Total Sum":
            total = sum(nums)
            formula = f"Using formula: sum = (n/2)*(first + last) = ({len(nums)}/2)*({a} + {b})"
        elif mode == "Sum of Even Numbers":
            evens = [n for n in nums if n % 2 == 0]
            total = sum(evens)
            formula = f"Count of even numbers: {len(evens)}"
        else:
            odds = [n for n in nums if n % 2 != 0]
            total = sum(odds)
            formula = f"Count of odd numbers: {len(odds)}"

        st.markdown(
            f"""
            <div style="
                background-color: #4CAF50;
                color: white;
                padding: 15px;
                border-radius: 10px;
                text-align: center;
                font-size: 24px;
                font-weight: bold;">
                ✅ {mode}: {total}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.info(f"📘 **Calculation Details:** {formula}")

        # Generate DataFrame for learning and visualization
        df = pd.DataFrame({
            "Number": nums,
            "Type": ["Even" if n % 2 == 0 else "Odd" for n in nums],
        })
        df["Cumulative Sum"] = df["Number"].cumsum()

        st.write("### 📊 Number Details Table")
        # Dynamic styling fallback
        if len(df) * len(df.columns) > 250_000:
            st.warning("⚠️ Large data detected; displaying without gradient styling for smooth performance.")
            st.dataframe(df)
        else:
            st.dataframe(df.style.background_gradient(cmap="YlGnBu"))

        # Line Chart of Cumulative Sum
        fig = px.line(
            df,
            x="Number",
            y="Cumulative Sum",
            color="Type",
            title="📈 Cumulative Sum Progress",
            markers=True
        )
        st.plotly_chart(fig, use_container_width=True)

        st.success("✅ Calculation completed! Use this for quick dataset analysis and learning.")

