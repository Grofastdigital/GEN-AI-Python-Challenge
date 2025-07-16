import streamlit as st
import pandas as pd

st.set_page_config(page_title="Day 3/50: Even or Odd Checker", page_icon="🦅", layout="centered")

st.title("🦅 Day 3/50: Even or Odd Checker 🔢")
st.write("Welcome Eagle! Paste your numbers below to visually check which are even or odd.")

# Initialize history in session state
if "day3_history" not in st.session_state:
    st.session_state.day3_history = []

num_list = st.text_area("📋 Enter comma-separated numbers (e.g., 1, 2, 3, 4, 5):")

if st.button("✨ Check"):
    try:
        numbers = [int(n.strip()) for n in num_list.split(",") if n.strip() != ""]
        
        results = []
        even_count = 0
        odd_count = 0
        
        for n in numbers:
            if n % 2 == 0:
                even_count += 1
                badge = "<span style='color:green; font-weight:bold;'>Even ✅</span>"
            else:
                odd_count += 1
                badge = "<span style='color:blue; font-weight:bold;'>Odd 🔵</span>"
            results.append({"Number": n, "Type": badge})

        df = pd.DataFrame(results)

        # Convert DataFrame to HTML table with row gradient
        def render_table(df):
            html = "<table style='border-collapse: collapse; width: 100%;'>"
            html += "<tr><th style='padding: 8px; border: 1px solid #ddd;'>Number</th><th style='padding: 8px; border: 1px solid #ddd;'>Type</th></tr>"
            for i, row in df.iterrows():
                color = "#f0fff0" if i % 2 == 0 else "#f0f8ff"
                html += f"<tr style='background-color:{color};'><td style='padding: 8px; border: 1px solid #ddd;'>{row['Number']}</td><td style='padding: 8px; border: 1px solid #ddd;'>{row['Type']}</td></tr>"
            html += "</table>"
            return html

        st.markdown(render_table(df), unsafe_allow_html=True)

        st.success(f"✅ Found {even_count} even and {odd_count} odd numbers out of {len(numbers)} total numbers.")
        st.balloons()

        # Save to history
        st.session_state.day3_history.append({
            "input": num_list,
            "even": even_count,
            "odd": odd_count
        })

    except Exception as e:
        st.error(f"⚠️ Please enter valid integers separated by commas. Error: {str(e)}")

# Show History
if st.session_state.day3_history:
    with st.expander("📜 View History"):
        for idx, entry in enumerate(reversed(st.session_state.day3_history[-5:]), 1):
            st.write(f"{idx}. `{entry['input']}` ➔ ✅ {entry['even']} Even | 🔵 {entry['odd']} Odd")

