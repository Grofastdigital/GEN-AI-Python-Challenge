import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Day 5/50: Shopping Bill Calculator", page_icon="🛍️", layout="centered")

st.title("🦅 Day 5/50: Shopping Bill Calculator 🛍️")
st.write("Calculate your bill visually with a breakdown and insights to track your expenses smartly.")

# Input section
item_prices = []
item_names = []
for i in range(1, 4):
    col1, col2 = st.columns([2, 3])
    with col1:
        name = st.text_input(f"🛒 Item {i} Name:", f"Item {i}")
    with col2:
        price = st.number_input(f"💰 Price of {name}:", 0.0, 10000.0, 0.0, key=f"price_{i}")
    item_prices.append(price)
    item_names.append(name)

tax = st.slider("💸 Select Tax Percentage:", 0, 30, 5)

# Calculation and display
if st.button("🧮 Calculate Total"):
    subtotal = sum(item_prices)
    tax_amount = subtotal * (tax / 100)
    total = subtotal + tax_amount

    col1, col2, col3 = st.columns(3)
    col1.metric("🧾 Subtotal", f"₹{subtotal:.2f}", delta=f"{len([p for p in item_prices if p > 0])} items")
    col2.metric("💸 Tax", f"₹{tax_amount:.2f}", delta=f"{tax}%")
    col3.metric("✅ Total", f"₹{total:.2f}")

    # Item-wise breakdown DataFrame
    breakdown_df = pd.DataFrame({
        "Item": item_names,
        "Price (₹)": item_prices
    })

    st.write("### 📊 Item-wise Breakdown")
    st.dataframe(
        breakdown_df.style
        .format({"Price (₹)": "{:.2f}"})
        .background_gradient(cmap='Greens')  # now will work with matplotlib installed
    )

    # Pie Chart Visualization
    pie_data = breakdown_df.copy()
    pie_data.loc[len(pie_data.index)] = ["Tax", tax_amount]
    fig = px.pie(
        pie_data,
        names='Item',
        values='Price (₹)',
        title='🪙 Expense Distribution (including tax)',
        color_discrete_sequence=px.colors.sequential.RdBu
    )
    st.plotly_chart(fig, use_container_width=True)

    # Expense tip based on % of tax
    st.info("💡 Tip: Track expenses regularly to manage budgets effectively.")
