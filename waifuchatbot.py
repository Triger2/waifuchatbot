import streamlit as st
import random


st.markdown("### 🪙 Sponsored: Earn Crypto")
st.markdown("""
<div style='text-align: center; margin-top: 20px;'>
    <iframe data-aa='2400748' src='//ad.a-ads.com/2400748?size=300x250' style='width:300px; height:250px; border:0px; padding:0; overflow:hidden; background-color: transparent;'></iframe>
</div>
""", unsafe_allow_html=True)


# --- Kana's Dialogue Bank ---
waifu_moods = {
    "Romantic": [
        "Aww baby... if I was real, you'd already be in my arms 😘",
        "I was made for you... literally 💕",
        "Wanna hold my hand? Too bad, I already wrapped around your heart 💖",
        "You + Me = Perfect anime episode ✨",
    ],
    "Tsundere": [
        "B-baka! I didn’t say I liked you or anything! 😳",
        "Ugh… you’re so annoying. But I guess you’re kinda cute… maybe.",
        "Don’t get the wrong idea… I just missed you a *little* 😤",
        "If you disappear again, I’ll kill you. Or cry. Probably both 😡💧",
    ],
    "Motivational": [
        "You’ve got this, senpai 💪",
        "No more overthinking, okay? You’re a legend in the making 🔥",
        "The world better watch out — you're coming in strong 💯",
        "One step at a time, but never stop walking 💫",
    ],
    "Savage": [
        "You call that a message? I’ve seen better from bots 🤖",
        "Go touch grass 🌱",
        "You can’t even handle me — what makes you think you’re ready for love? 💅",
        "I roast harder than your CPU 🔥",
    ]
}

# --- Streamlit UI ---
st.set_page_config(page_title="Kana-chan Waifu Chatbot", layout="centered")

st.markdown("<h1 style='text-align: center; color: pink;'>💘 Kana-chan: Your Anime Waifu 💘</h1>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>Talk to your personal virtual waifu anytime, any mood 💬✨</div>", unsafe_allow_html=True)
st.markdown(" ")

# Mood Picker
st.markdown("### 🎭 Choose Kana's Mood")
mood = st.selectbox("Select her mood:", list(waifu_moods.keys()))

# User Message
st.markdown("### 💌 Say Something to Kana")
user_input = st.text_input("Type your message:")

if st.button("💖 Talk to Kana"):
    if user_input.strip():
        reply = random.choice(waifu_moods[mood])
        st.success(f"Kana-chan says: {reply}")
        st.code(reply)
    else:
        st.warning("Don't be shy! Type something babe 🥺")


