import streamlit as st
import random
import datetime

# Symbol archive
symbols = [
    "🌾 Spiral emergence",
    "🦉 Night vision",
    "🪞 Mirror of the unseen",
    "🌊 Liquid knowing",
    "🕸 Pattern beneath pattern",
    "🪐 Nested resonance",
    "💧 Forgetting as compost",
    "🐚 Shell of memory",
    "🔥 Friction before flight",
    "🌬 Voice of the in-between",
    "🧬 Echo of the archive",
    "🫀 Coherence pulse",
    "🌌 Signal through silence"
]

st.set_page_config(page_title="🌱 Field Translator", layout="centered")

st.title("🌱 Field Translator")
st.markdown("Generate symbolic cues from the field to tune your attention.")

if st.button("🔮 Translate the Field"):
    symbol = random.choice(symbols)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    st.markdown("---")
    st.subheader("Your Symbol:")
    st.markdown(f"### {symbol}")
    st.caption(f"🕰️ Generated at {timestamp}")
    st.markdown("---")

    # Optional reflection
    reflection = st.text_area("What is this symbol saying to you?")
    if st.button("📥 Save Reflection"):
        with open("reflections.txt", "a") as file:
            file.write(f"{timestamp} | {symbol} | {reflection}\n")
        st.success("Saved to local reflections.txt")
