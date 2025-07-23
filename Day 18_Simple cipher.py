import streamlit as st
import qrcode
from PIL import Image
import io
from streamlit_lottie import st_lottie
import requests
import base64

# --- Page Config ---
st.set_page_config(page_title="🦅 Day 18/50: Premium Simple Cipher 🚀", page_icon="🔐", layout="centered")

# --- Lottie Loader ---
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

lottie_success = load_lottieurl("https://lottie.host/aa0d2e41-e897-4d3f-9c90-4322f7c9f5f2/GkIrqxOmZQ.json")

# --- Gradient Header ---
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='font-size: 48px; background: -webkit-linear-gradient(45deg, #00c6ff, #0072ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>🦅 Day 18/50 - Premium Simple Cipher 🚀</h1>
        <p style='font-size: 18px; color: grey;'>Encrypt your words with a customizable cipher and premium features for your advanced Streamlit challenge.</p>
    </div>
""", unsafe_allow_html=True)

# --- User Input ---
word = st.text_input("✍️ Enter a word to encrypt:")

# --- Cipher Shift Control ---
shift_value = st.slider("🔄 Select shift value for encryption (Caesar cipher strength):", 1, 25, 1)

if st.button("🔐 Encrypt Now"):
    if word.strip():
        encrypted = ""
        for char in word:
            if char.isalpha():
                shift = ord('a') if char.islower() else ord('A')
                encrypted += chr((ord(char) - shift + shift_value) % 26 + shift)
            else:
                encrypted += char

        # Show success animation
        if lottie_success:
            st_lottie(lottie_success, speed=1, height=200, key="success")

        char_count = len(word.replace(" ", ""))
        word_count = len(word.split())

        st.markdown(f"""
        <div style='background: linear-gradient(to right, #00c6ff, #0072ff); padding: 20px; border-radius: 12px; color: white; text-align: center;'>
            <h2>✅ Encrypted Text: {encrypted}</h2>
            <p>🔡 Character Count (no spaces): {char_count} | 📝 Word Count: {word_count} | 🔄 Shift Applied: {shift_value}</p>
        </div>
        """, unsafe_allow_html=True)

        st.code(encrypted, language='text')

        # --- Copy to Clipboard ---
        st.text_input("📋 Copy Encrypted Text:", encrypted)

        # --- QR Code of Encrypted Text ---
        st.subheader("📱 QR Code of Encrypted Text")
        qr = qrcode.make(encrypted)
        qr_buf = io.BytesIO()
        qr.save(qr_buf, format="PNG")
        st.image(qr_buf, width=200)

        # --- Download Encrypted Text ---
        encrypted_bytes = io.BytesIO(encrypted.encode('utf-8'))
        st.download_button(
            label="⬇️ Download Encrypted Text as .txt",
            data=encrypted_bytes,
            file_name="encrypted_text.txt",
            mime="text/plain"
        )

        st.success("🚀 Encryption complete! Share your encrypted message securely.")

    else:
        st.error("❌ Please enter a valid word to encrypt.")
