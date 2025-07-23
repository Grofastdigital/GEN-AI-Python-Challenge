import streamlit as st
import qrcode
from PIL import Image
import io
from streamlit_lottie import st_lottie
import requests
import phonenumbers
from phonenumbers import carrier

# --- Page Config ---
st.set_page_config(page_title="🦅 Day 21/50: Premium Phone Number Formatter 🚀", page_icon="📱", layout="centered")

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
        <h1 style='font-size: 48px; background: -webkit-linear-gradient(45deg, #00c6ff, #0072ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>🦅 Day 21/50 - Premium Phone Number Formatter 🚀</h1>
        <p style='font-size: 18px; color: grey;'>Format phone numbers smartly with advanced features for your premium toolkit.</p>
    </div>
""", unsafe_allow_html=True)

# --- User Input ---
phone = st.text_input("📲 Enter your phone number (with or without country code):")

if st.button("📞 Format Number Now"):
    try:
        parsed = phonenumbers.parse(phone, "IN")  # Defaults to India if country code absent
        if phonenumbers.is_valid_number(parsed):
            formatted_intl = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            formatted_natl = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)
            carrier_name = carrier.name_for_number(parsed, "en")

            # ✅ Success Animation
            if lottie_success:
                st_lottie(lottie_success, speed=1, height=200, key="success")

            # ✅ Display Formatted Output
            st.markdown(f"""
            <div style='background: linear-gradient(to right, #00c6ff, #0072ff); padding: 20px; border-radius: 12px; color: white; text-align: center;'>
                <h2>✅ Formatted Number:</h2>
                <p>🌐 International: <b>{formatted_intl}</b></p>
                <p>🇮🇳 National: <b>{formatted_natl}</b></p>
                <p>📡 Carrier: <b>{carrier_name if carrier_name else 'Unknown/NA'}</b></p>
            </div>
            """, unsafe_allow_html=True)

            # ✅ Easy Copy Field
            st.text_input("📋 Copy Formatted Number (Intl):", formatted_intl)

            # ✅ QR Code Generation
            st.subheader("📱 QR Code of Your Number")
            qr = qrcode.make(formatted_intl)
            qr_buf = io.BytesIO()
            qr.save(qr_buf, format="PNG")
            st.image(qr_buf, width=200)

            # ✅ Download as VCF
            vcf_content = f"""BEGIN:VCARD
VERSION:3.0
FN:Saved Contact
TEL;TYPE=CELL:{formatted_intl}
END:VCARD
"""
            vcf_bytes = io.BytesIO(vcf_content.encode('utf-8'))
            st.download_button(
                label="⬇️ Download Contact (.vcf)",
                data=vcf_bytes,
                file_name="contact.vcf",
                mime="text/vcard"
            )

            st.success("🚀 Phone number formatted and ready to save/share.")

        else:
            st.error("❌ The entered number is not a valid phone number. Please check and try again.")
    except Exception as e:
        st.error(f"❌ Error: {e}\nPlease ensure your number is in a correct format (e.g., +919876543210 or 9876543210).")
