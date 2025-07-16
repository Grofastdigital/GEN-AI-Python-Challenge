import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Day 14/50: Advanced Vowel Counter", page_icon="🅰️")

st.title("🦅 Day 14/50: Advanced Vowel Counter 🅰️🅾️")

word = st.text_input("🔤 Enter a word or sentence:")

if st.button("🚀 Count Vowels"):
    if not word.strip():
        st.warning("⚠️ Please enter a non-empty word or sentence.")
    else:
        vowels = "aeiouAEIOU"
        vowel_counts = {v: 0 for v in "aeiou"}

        for char in word.lower():
            if char in vowel_counts:
                vowel_counts[char] += 1

        total_vowels = sum(vowel_counts.values())

        df_vowels = pd.DataFrame({
            "Vowel": list(vowel_counts.keys()),
            "Count": list(vowel_counts.values())
        })

        # Highlight the vowel with max count
        max_count = df_vowels["Count"].max()
        df_vowels["Most Frequent"] = ["✅" if c == max_count and c > 0 else "" for c in df_vowels["Count"]]

        st.markdown("### 🗂️ Vowel Count Table")
        st.dataframe(df_vowels.style.applymap(
            lambda val: "background-color: #d4edda" if val == "✅" else ""
        ))

        st.success(f"🔍 **Total vowels in '{word}': {total_vowels} ✅**")

        if total_vowels > 0:
            st.markdown("### 📊 Vowel Distribution Chart")
            fig = px.bar(
                df_vowels, x="Vowel", y="Count", color="Count",
                color_continuous_scale="Tealgrn",
                text="Count", title="Vowel Frequency in Input",
                labels={"Count": "Frequency"}
            )
            fig.update_traces(textposition="outside")
            st.plotly_chart(fig, use_container_width=True)

        st.info("✨ Keep practicing daily to master data analysis & Python visualization!")

