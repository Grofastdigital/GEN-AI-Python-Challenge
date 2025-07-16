import streamlit as st
import re

st.set_page_config(page_title="Day 7/50: Password Strength Checker", page_icon="🔑", layout="centered")

st.title("🦅 Day 7/50: Advanced Password Strength Checker 🔑")
st.write("Check how strong your password is with instant feedback.")

password = st.text_input("🔐 Enter your password:", type="password")

def check_strength(pw):
    score = 0
    feedback = []

    if len(pw) >= 8:
        score += 1
    else:
        feedback.append("❌ Minimum 8 characters")

    if re.search(r"[a-z]", pw):
        score += 1
    else:
        feedback.append("❌ Add lowercase letters")

    if re.search(r"[A-Z]", pw):
        score += 1
    else:
        feedback.append("❌ Add uppercase letters")

    if re.search(r"\d", pw):
        score += 1
    else:
        feedback.append("❌ Add numbers")

    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", pw):
        score += 1
    else:
        feedback.append("❌ Add special characters")

    # Check for common patterns
    if pw.lower() in ["password", "123456", "qwerty"]:
        score = max(score - 2, 0)
        feedback.append("⚠️ Avoid common passwords like 'password' or '123456'")

    return score, feedback

if st.button("✨ Check Strength"):
    if password:
        score, feedback = check_strength(password)

        verdict = {
            0: ("🔴 Very Weak", "red"),
            1: ("🔴 Weak", "orangered"),
            2: ("🟡 Moderate", "orange"),
            3: ("🟡 Fair", "gold"),
            4: ("🟢 Strong", "green"),
            5: ("🟩 Very Strong", "darkgreen")
        }

        st.markdown(
            f"""
            <div style="
                background: {verdict[score][1]};
                color: white;
                padding: 15px;
                border-radius: 10px;
                text-align: center;
                font-size: 24px;
                font-weight: bold;">
                {verdict[score][0]}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.progress(score / 5)

        if feedback:
            st.write("### 🛠️ Recommendations to improve:")
            for f in feedback:
                st.write(f"- {f}")
        else:
            st.success("✅ Your password is strong and meets all criteria!")

    else:
        st.warning("⚠️ Please enter a password to check.")

