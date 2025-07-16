import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Day 13/50: Advanced Max Finder", page_icon="📈")

st.title("🦅 Day 13/50: Advanced List Maximum Finder 📈")

nums = st.text_area("🔢 Enter numbers separated by commas (e.g., 10, 20, 30):")

if st.button("🚀 Find Maximum"):
    try:
        numbers = [float(n.strip()) for n in nums.split(",") if n.strip()]
        if not numbers:
            st.warning("⚠️ Please enter at least one valid number.")
        else:
            max_num = numbers[0]
            steps = []

            for idx, n in enumerate(numbers[1:], start=2):
                status = ""
                if n > max_num:
                    max_num = n
                    status = "✅ Updated Max"
                else:
                    status = "❌ No Change"
                steps.append({"Step": f"Compare with input #{idx}", "Value": n, "Max So Far": max_num, "Status": status})

            df_steps = pd.DataFrame(steps)

            st.markdown("### 🪄 Step-by-Step Comparison Table")
            st.dataframe(df_steps.style.applymap(
                lambda val: "background-color: #d4edda" if "✅" in str(val) else ""))

            st.success(f"🎯 **Maximum number found: `{max_num}` ✅**")

            st.markdown("### 📊 Visual Representation of All Numbers")
            df_plot = pd.DataFrame({"Number": numbers})
            fig = px.bar(df_plot, y="Number", text="Number",
                         color=df_plot["Number"] == max_num,
                         color_discrete_map={True: "green", False: "lightblue"},
                         title="Entered Numbers Highlighting the Maximum",
                         labels={"color": "Is Maximum?"})
            fig.update_traces(textposition="outside")
            st.plotly_chart(fig, use_container_width=True)

            st.info("✨ Keep challenging yourself daily to master data analysis skills!")

    except Exception as e:
        st.error(f"❌ Invalid input. Please enter only numbers separated by commas.\n\nDetails: {e}")
