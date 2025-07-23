import streamlit as st
import pandas as pd
import io
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from textblob import TextBlob
from langdetect import detect
from gtts import gTTS
import base64
import plotly.express as px

# --- CONFIG ---
st.set_page_config(page_title="Day 16/50: Ultimate Word Reverser 🚀", page_icon="🔄", layout="wide")

dark_mode = st.toggle("🌙 Dark Mode")

# --- Dynamic Background ---
page_style = """
    <style>
    body {
        background: linear-gradient(to right, #1f4037, #99f2c8);
    }
    </style>
""" if dark_mode else """
    <style>
    body {
        background: linear-gradient(to right, #fceabb, #f8b500);
    }
    </style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# --- Heading ---
st.markdown(f"""
    <h1 style='text-align: center; color: {"#FFFFFF" if dark_mode else "#FF6F61"};'>🦅 Day 16/50 - Ultimate Word Reverser 🚀</h1>
    <p style='text-align: center; color: {"#DDD" if dark_mode else "grey"};'>Reverse each word + sentiment, language, audio & fancy charts.</p>
""", unsafe_allow_html=True)

sentence = st.text_area("✍️ Enter a sentence to reverse each word:", height=150, placeholder="Type your sentence here...")

if st.button("🔄 Reverse Words in Style"):
    if sentence.strip():
        words = sentence.strip().split()
        reversed_words = [word[::-1] for word in words]

        word_lengths = [len(word) for word in words]
        reversed_lengths = [len(word) for word in reversed_words]

        # --- Sentiment & Language ---
        blob = TextBlob(sentence)
        polarity = blob.sentiment.polarity
        lang = detect(sentence)

        sentiment = "😊 Positive" if polarity > 0 else "😐 Neutral" if polarity == 0 else "☹️ Negative"

        df = pd.DataFrame({
            "Original Word": words,
            "Length": word_lengths,
            "Reversed Word": reversed_words,
            "Reversed Length": reversed_lengths,
        })

        st.markdown(f"""
        <div style='background: linear-gradient(to right, #00c6ff, #0072ff); padding: 15px; border-radius: 10px; color: white;'>
            <h3>📋 Reversed Words Table + Analytics</h3>
            <p><b>Detected Language:</b> {lang.upper()}</p>
            <p><b>Sentiment:</b> {sentiment} (Polarity: {polarity:.2f})</p>
        </div>
        """, unsafe_allow_html=True)

        st.dataframe(df, use_container_width=True, height=400)

        reversed_sentence = " ".join(reversed_words)

        st.markdown(f"""
        <div style='background: linear-gradient(to right, #f7971e, #ffd200); padding: 15px; border-radius: 10px; color: black;'>
            <h3>🔤 Reversed Sentence</h3>
        </div>
        """, unsafe_allow_html=True)

        st.code(reversed_sentence, language='text')

        # --- WordCloud ---
        st.subheader("☁️ Word Cloud of Original Words")
        wordcloud = WordCloud(width=800, height=400, background_color='black' if dark_mode else 'white').generate(" ".join(words))
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)

        # --- Word Length Chart ---
        st.subheader("📊 Word Lengths Chart")
        fig_bar = px.bar(df, x="Original Word", y="Length", color="Length", text="Length")
        st.plotly_chart(fig_bar, use_container_width=True)

        # --- Audio Readout ---
        st.subheader("🔊 Listen to Reversed Sentence")
        tts = gTTS(reversed_sentence)
        tts_bytes = io.BytesIO()
        tts.write_to_fp(tts_bytes)
        audio_bytes = tts_bytes.getvalue()

        st.audio(audio_bytes, format='audio/mp3')

        # --- Download ---
        reversed_bytes = io.BytesIO(reversed_sentence.encode('utf-8'))
        st.download_button(
            label="⬇️ Download Reversed Sentence (.txt)",
            data=reversed_bytes,
            file_name="reversed_sentence.txt",
            mime="text/plain"
        )

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇️ Download Table as CSV",
            data=csv,
            file_name="reversed_words.csv",
            mime='text/csv',
        )

        st.success("✅ Words reversed with sentiment, language, audio & charts!")

    else:
        st.error("❌ Please enter a valid sentence.")

