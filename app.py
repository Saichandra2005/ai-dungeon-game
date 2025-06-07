import streamlit as st
import google.generativeai as genai

# Setup Gemini
genai.configure(api_key="AIzaSyA6Ot4bNF6GKV6D3_MxAkisEWUlrbFT5qw")  # Replace with your real key
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Streamlit title
st.title("🧙 AI Dungeon: The Rise of Eldoria")
st.markdown("Welcome, adventurer! Begin your journey in this fantasy world.")

# Memory for story
if "story" not in st.session_state:
    st.session_state.story = (
        "Narrator: Welcome to the Kingdom of Eldoria, a land of magic and danger. "
        "You awaken in a small village with a strange mark glowing on your hand. "
        "Rumors whisper of a dark prophecy...\n"
    )

# Text input
user_input = st.text_input("What will you do?", key="input")

# Generate and show story
if user_input:
    # Update story prompt
    st.session_state.story += f"\nPlayer: {user_input}\nNarrator:"

    # Get response from Gemini
    response = model.generate_content(st.session_state.story)
    narration = response.text.strip()

    # Add response to story
    st.session_state.story += f" {narration}\n"

    # Display the latest narration
    st.markdown(f"**Narrator:** {narration}")

# Show full history
with st.expander("📜 Full Story So Far"):
    st.text(st.session_state.story)
