import streamlit as st
import qrcode
from PIL import Image
import io
from streamlit_lottie import st_lottie
import requests
import base64
import re

# --- Page Config ---
st.set_page_config(page_title="🦅 Day 19/50: Premium Email Username Extractor 🚀", page_icon="✉️", layout="centered")

# --- Lottie Loader ---
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Stable Lottie success animation
lottie_success = load_lottieurl("https://lottie.host/aa0d2e41-e897-4d3f-9c90-4322f7c9f5f2/GkIrqxOmZQ.json")

# --- Gradient Header ---
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='font-size: 48px; background: -webkit-linear-gradient(45deg, #00c6ff, #0072ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>🦅 Day 19/50 - Premium Email Username Extractor 🚀</h1>
        <p style='font-size: 18px; color: grey;'>Extract and analyze your email username with advanced premium features.</p>
    </div>
""", unsafe_allow_html=True)

# --- User Input ---
email = st.text_input("✍️ Enter your email for username extraction:")

# --- Extract Button ---
if st.button("📤 Extract Username"):
    # ✅ Corrected Regex
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.match(email_pattern, email):
        username = email.split("@")[0]
        domain = email.split("@")[1]
        char_count = len(username)
        alphas = sum(c.isalpha() for c in username)
        digits = sum(c.isdigit() for c in username)
        specials = char_count - alphas - digits

        # ✅ Success Animation
        if lottie_success:
            st_lottie(lottie_success, speed=1, height=200, key="success")

        # ✅ Results Card
        st.markdown(f"""
        <div style='background: linear-gradient(to right, #00c6ff, #0072ff); padding: 20px; border-radius: 12px; color: white; text-align: center;'>
            <h2>✅ Extracted Username: {username}</h2>
            <p>🔡 Characters: {char_count} | 🔠 Letters: {alphas} | #️⃣ Digits: {digits} | ✨ Specials: {specials}</p>
            <p>🌐 Domain: {domain}</p>
        </div>
        """, unsafe_allow_html=True)

        # ✅ Code block for copy-paste
        st.code(username, language='text')

        # ✅ Easy copy field
        st.text_input("📋 Copy Username:", username)

        # ✅ QR Code Generation
        st.subheader("📱 QR Code of Your Username")
        qr = qrcode.make(username)
        qr_buf = io.BytesIO()
        qr.save(qr_buf, format="PNG")
        st.image(qr_buf, width=200)

        # ✅ Download as .txt
        username_bytes = io.BytesIO(username.encode('utf-8'))
        st.download_button(
            label="⬇️ Download Username as .txt",
            data=username_bytes,
            file_name="username.txt",
            mime="text/plain"
        )

        st.success("🚀 Username extraction complete! Share or store your username securely.")

    else:
        st.error("❌ Please enter a valid email address.")
