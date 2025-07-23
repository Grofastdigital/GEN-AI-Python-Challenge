import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
from streamlit_lottie import st_lottie
import requests
import io

# --- Page Config ---
st.set_page_config(page_title="🦅 Day 20/50: Premium Text Statistics 🚀", page_icon="📊", layout="centered")

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
        <h1 style='font-size: 48px; background: -webkit-linear-gradient(45deg, #00c6ff, #0072ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>🦅 Day 20/50 - Premium Text Statistics Analyzer 🚀</h1>
        <p style='font-size: 18px; color: grey;'>Analyze your text with visual insights and premium features.</p>
    </div>
""", unsafe_allow_html=True)

# --- Text Input ---
paragraph = st.text_area("✍️ Enter your paragraph for analysis:", height=200)

if st.button("📊 Analyze Text Now"):
    if paragraph.strip():
        words = paragraph.split()
        sentences = [s for s in paragraph.replace("!", ".").replace("?", ".").split(".") if s.strip()]
        characters = len(paragraph.replace(" ", ""))
        word_count = len(words)
        sentence_count = len(sentences)
        avg_word_len = round(sum(len(word) for word in words) / word_count, 2) if word_count > 0 else 0
        longest_word = max(words, key=len) if words else ""

        # ✅ Lottie Animation
        if lottie_success:
            st_lottie(lottie_success, speed=1, height=200, key="success")

        # ✅ Display Metrics
        st.markdown(f"""
        <div style='background: linear-gradient(to right, #00c6ff, #0072ff); padding: 20px; border-radius: 12px; color: white; text-align: center;'>
            <h2>✅ Text Analysis Results</h2>
            <p>🔤 <b>Characters (no spaces):</b> {characters}</p>
            <p>🔡 <b>Word Count:</b> {word_count}</p>
            <p>📝 <b>Sentence Count:</b> {sentence_count}</p>
            <p>📏 <b>Average Word Length:</b> {avg_word_len}</p>
            <p>🏆 <b>Longest Word:</b> {longest_word}</p>
        </div>
        """, unsafe_allow_html=True)

        # ✅ Pie Chart
        labels = ['Words', 'Sentences', 'Characters']
        sizes = [word_count, sentence_count, characters]
        colors = ['#ff9999', '#66b3ff', '#99ff99']

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
        ax1.axis('equal')
        st.subheader("📈 Distribution Pie Chart")
        st.pyplot(fig1)

        # ✅ Bar Chart
        fig2, ax2 = plt.subplots()
        ax2.bar(labels, sizes, color=colors)
        ax2.set_title("📊 Text Statistics")
        st.pyplot(fig2)

        # ✅ Word Cloud
        word_freq = Counter(words)
        wc = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)
        fig3, ax3 = plt.subplots(figsize=(10, 5))
        ax3.imshow(wc, interpolation='bilinear')
        ax3.axis('off')
        st.subheader("☁️ Word Cloud")
        st.pyplot(fig3)

        # ✅ Download Report
        report_content = f"""
Text Statistics Report:

Characters (no spaces): {characters}
Word Count: {word_count}
Sentence Count: {sentence_count}
Average Word Length: {avg_word_len}
Longest Word: {longest_word}

Thank you for using the Premium Text Statistics Analyzer!
"""
        report_bytes = io.BytesIO(report_content.encode('utf-8'))
        st.download_button(
            label="⬇️ Download Analysis Report (.txt)",
            data=report_bytes,
            file_name="text_statistics_report.txt",
            mime="text/plain"
        )

        st.success("🚀 Text analysis completed successfully! Use these insights for your content creation and planning.")

    else:
        st.error("❌ Please enter a paragraph for analysis.")
