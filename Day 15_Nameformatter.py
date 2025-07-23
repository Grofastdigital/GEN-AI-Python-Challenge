import streamlit as st
import qrcode
from PIL import Image
import io
import base64

st.set_page_config(page_title="Name Formatter Pro", page_icon="🧑‍💼", layout="centered")

st.markdown(
    "<h1 style='text-align: center; color: #33C1FF;'>🦅 Day 15/50 - Name Formatter Pro 🚀</h1>",
    unsafe_allow_html=True,
)

name = st.text_input("📝 Enter your full name:")

if st.button("🎨 Format Name"):
    if name.strip():
        parts = name.strip().split()
        first = parts[0]
        last = parts[-1]
        initials = "".join([p[0].upper() for p in parts])
        reversed_name = " ".join(parts[::-1])

        char_count = len(name.replace(" ", ""))
        word_count = len(parts)
        ascii_sum = sum(ord(c) for c in name if c != " ")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                f"""
                <div style='background: linear-gradient(to right, #00c6ff, #0072ff); padding: 15px; border-radius: 10px; color: white;'>
                    <h3>Formatted</h3>
                    <p><b>Last, First:</b> {last}, {first}</p>
                    <p><b>Initials:</b> {initials}</p>
                    <p><b>Title Case:</b> {name.title()}</p>
                    <p><b>Character Count:</b> {char_count}</p>
                    <p><b>Word Count:</b> {word_count}</p>
                    <p><b>ASCII Sum:</b> {ascii_sum}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col2:
            st.markdown(
                f"""
                <div style='background: linear-gradient(to right, #f7971e, #ffd200); padding: 15px; border-radius: 10px; color: black;'>
                    <h3>More Formats</h3>
                    <p><b>Reversed Order:</b> {reversed_name}</p>
                    <p><b>Uppercase:</b> {name.upper()}</p>
                    <p><b>Lowercase:</b> {name.lower()}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("---")

        st.subheader("✨ Initials Badge")
        st.markdown(
            f"""
            <div style='
                display: inline-block; 
                background: linear-gradient(135deg, #667eea, #764ba2); 
                color: white; 
                padding: 20px 40px; 
                border-radius: 50px; 
                font-size: 32px; 
                font-weight: bold; 
                box-shadow: 2px 2px 10px rgba(0,0,0,0.3);'>
                {initials}
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Generate QR code
        qr = qrcode.make(name)
