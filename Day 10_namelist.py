import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Day 10/50: Name Length Table", page_icon="📋", layout="centered")

st.title("🦅 Day 10/50: Advanced Name Length Analyzer 📋")
st.write("Enter names to analyze their length, check palindromes, and visualize insights for your #50DaysStreamlitChallenge.")

# User decides how many names to input
num_names = st.slider("🖊️ How many names would you like to enter?", 3, 20, 5)

names = [st.text_input(f"✍️ Enter Name {i+1}:", key=f"name_{i}") for i in range(num_names)]

if st.button("✨ Show Analysis Table"):
    filtered_names = [name.strip() for name in names if name.strip()]

    if not filtered_names:
        st.warning("⚠️ Please enter at least one name to analyze.")
    else:
        df = pd.DataFrame({
            "Name": filtered_names,
            "Length": [len(name) for name in filtered_names],
            "Is Palindrome": ["✅ Yes" if name.lower() == name[::-1].lower() else "❌ No" for name in filtered_names],
            "Is Long (>7)": ["🟩 Long" if len(name) > 7 else "🟨 Short" for name in filtered_names],
            "Uppercase": [name.upper() for name in filtered_names]
        })

        st.write("### 📊 Name Analysis Table")
        if len(df) * len(df.columns) > 250_000:
            st.warning("⚠️ Large data detected; displaying without styling.")
            st.dataframe(df)
        else:
            st.dataframe(df.style.background_gradient(cmap="BuGn"))

        # Pie chart of short vs long names
        long_count = sum(1 for name in filtered_names if len(name) > 7)
        short_count = len(filtered_names) - long_count

        pie_df = pd.DataFrame({
            "Category": ["Long Names (>7 chars)", "Short Names (≤7 chars)"],
            "Count": [long_count, short_count]
        })

        fig = px.pie(
            pie_df,
            names="Category",
            values="Count",
            title="🪐 Long vs Short Names Distribution",
            color_discrete_sequence=px.colors.sequential.Teal
        )
        st.plotly_chart(fig, use_container_width=True)

        # Emoji verdicts for each name
        st.write("### 📝 Name Verdicts")
        for idx, row in df.iterrows():
            verdict = "✨"
            if row["Is Palindrome"] == "✅ Yes":
                verdict += " Palindrome,"
            verdict += " Long Name" if row["Is Long (>7)"] == "🟩 Long" else " Short Name"
            st.write(f"- **{row['Name']}** ➡️ {verdict}")

        st.success("✅ Analysis complete! Use this to showcase data string manipulation skills.")

