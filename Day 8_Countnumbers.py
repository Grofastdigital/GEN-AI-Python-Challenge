import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Day 8/50: Count Numbers", page_icon="🔢", layout="centered")

st.title("🦅 Day 8/50: Number Type Counter & Analyzer 🔢")
st.write("Enter comma-separated numbers to get a breakdown of positives, negatives, and zeros, with sums and averages.")

nums = st.text_area("✍️ Enter numbers separated by commas (e.g., 1, -2, 0, 5, -6):")

if st.button("✨ Analyze"):
    try:
        numbers = [float(n.strip()) for n in nums.split(",") if n.strip()]
        if not numbers:
            st.warning("⚠️ Please enter at least one valid number.")
        else:
            # Counts
            positive_count = sum(1 for n in numbers if n > 0)
            negative_count = sum(1 for n in numbers if n < 0)
            zero_count = sum(1 for n in numbers if n == 0)

            # Sums
            positive_sum = sum(n for n in numbers if n > 0)
            negative_sum = sum(n for n in numbers if n < 0)
            zero_sum = sum(n for n in numbers if n == 0)

            # Averages
            positive_avg = positive_sum / positive_count if positive_count else 0
            negative_avg = negative_sum / negative_count if negative_count else 0

            # Display in color-coded cards
            col1, col2, col3 = st.columns(3)
            col1.metric("✅ Positive Count", positive_count)
            col2.metric("❌ Negative Count", negative_count)
            col3.metric("⚫ Zero Count", zero_count)

            # DataFrame display
            df = pd.DataFrame({
                "Type": ["Positive ✅", "Negative ❌", "Zero ⚫"],
                "Count": [positive_count, negative_count, zero_count],
                "Sum": [positive_sum, negative_sum, zero_sum],
                "Average": [positive_avg, negative_avg, 0]
            })

            st.write("### 📊 Breakdown Table")
            st.dataframe(
                df.style.format({"Sum": "{:.2f}", "Average": "{:.2f}"})
                .background_gradient(cmap="PuBu")
            )

            # Pie chart of counts
            fig_pie = px.pie(
                df,
                names="Type",
                values="Count",
                title="🪐 Distribution of Number Types",
                color_discrete_sequence=px.colors.sequential.Teal
            )
            st.plotly_chart(fig_pie, use_container_width=True)

            # Bar chart of sums
            fig_bar = px.bar(
                df,
                x="Type",
                y="Sum",
                color="Type",
                text="Sum",
                title="💹 Sum of Values by Type",
                color_discrete_sequence=px.colors.qualitative.Set2
            )
            fig_bar.update_traces(texttemplate='%{text:.2f}', textposition="outside")
            st.plotly_chart(fig_bar, use_container_width=True)

            st.success("✅ Analysis completed successfully! Use this to analyze any dataset quickly.")

    except Exception as e:
        st.error(f"❌ An error occurred: {e}")
