import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import qrcode
from streamlit_lottie import st_lottie
import requests
import base64

# --- Page Config ---
st.set_page_config(page_title="🦅 Day 17/50: Initial Extractor 🚀", page_icon="🅰️", layout="centered")

# --- Lottie Loader ---
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Using a stable Lottie URL from lottiefiles
lottie_success = load_lottieurl("https://lottie.host/aa0d2e41-e897-4d3f-9c90-4322f7c9f5f2/GkIrqxOmZQ.json")

# --- Gradient Header ---
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='font-size: 48px; background: -webkit-linear-gradient(45deg, #00c6ff, #0072ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>🦅 Day 17/50 - Premium Initial Extractor 🚀</h1>
        <p style='font-size: 18px; color: grey;'>Extract, visualize, and download your initials with advanced UI.</p>
    </div>
""", unsafe_allow_html=True)

# --- Input Area ---
full_name = st.text_input("✍️ Enter your full name for initial extraction:")

if st.button("✨ Extract Initials"):
    if full_name.strip():
        parts = full_name.strip().split()
        initials = "".join([p[0].upper() for p in parts])
        char_count = len(full_name.replace(" ", ""))
        word_count = len(parts)
        vowels = sum(1 for c in full_name.lower() if c in "aeiou")
        consonants = sum(1 for c in full_name.lower() if c.isalpha() and c not in "aeiou")

        # --- Display Success Animation if loaded ---
        if lottie_success:
            st_lottie(lottie_success, speed=1, height=200, key="success")
        else:
            st.success("✅ Initials extracted successfully!")

        # --- Results Card ---
        st.markdown(f"""
        <div style='background: linear-gradient(to right, #00c6ff, #0072ff); padding: 20px; border-radius: 12px; color: white; text-align: center;'>
            <h2>✅ Extracted Initials: {initials}</h2>
            <p>🔡 Character Count (no spaces): {char_count} | 📝 Word Count: {word_count} | 🅰️ Vowels: {vowels} | 🅱️ Consonants: {consonants}</p>
        </div>
        """, unsafe_allow_html=True)

        st.code(initials, language='text')

        # --- Badge Image of Initials ---
        st.subheader("🎖️ Your Initials Badge")
        img = Image.new("RGB", (300, 300), color=(0, 114, 255))
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        draw.text((100, 130), initials, fill=(255, 255, 255))
        badge_buf = io.BytesIO()
        img.save(badge_buf, format="PNG")
        st.image(badge_buf)

        # --- QR Code of Initials ---
        st.subheader("📱 QR Code of Your Initials")
        qr = qrcode.make(initials)
        qr_buf = io.BytesIO()
        qr.save(qr_buf, format="PNG")
        st.image(qr_buf, width=200)

        # --- Download Buttons ---
        b64_txt = base64.b64encode(initials.encode()).decode()
        txt_href = f'<a href="data:file/txt;base64,{b64_txt}" download="initials.txt">📥 Download Initials as TXT</a>'
        st.markdown(txt_href, unsafe_allow_html=True)

        b64_badge = base64.b64encode(badge_buf.getvalue()).decode()
        badge_href = f'<a href="data:image/png;base64,{b64_badge}" download="initials_badge.png">📥 Download Badge Image</a>'
        st.markdown(badge_href, unsafe_allow_html=True)

        b64_qr = base64.b64encode(qr_buf.getvalue()).decode()
        qr_href = f'<a href="data:image/png;base64,{b64_qr}" download="initials_qr.png">📥 Download QR Code</a>'
        st.markdown(qr_href, unsafe_allow_html=True)

        st.success("🚀 Extraction complete! Share your initials on your stories and build your personal brand.")

    else:
        st.error("❌ Please enter a valid name to extract initials.")
