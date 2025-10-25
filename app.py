import streamlit as st
import base64

st.set_page_config(page_title="AI Bayan – TSK4", page_icon="👧", layout="centered")

page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: url("assets/background_glow.jpg");
    background-size: cover;
}
h1 {
    color: #FFD700;
    text-shadow: 0 0 15px #00BFFF;
    text-align: center;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

st.title("🌟 AI Bayan – TSK4 Edition 🇬🇧")
st.markdown("**Interactive English learning app** — Modules 1–4, 16 lessons")
st.image("assets/logo_girl.png", width=220)
st.markdown("Created by **Bayan** 🩵")

user_input = st.text_input("💬 Ask Bayan something:")
if user_input:
    st.write(f"🤖 *Bayan:* Let's talk about **{user_input}** together!")
