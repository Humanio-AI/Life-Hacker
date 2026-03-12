
import streamlit as st

BOT_NAME = "Life Hacker"

st.set_page_config(page_title=f"{BOT_NAME} Bot", page_icon="🤖")
st.title(f"🤖 {BOT_NAME} Bot")


def get_bot_reply(prompt: str) -> str:
    text = prompt.lower().strip()

    # Name questions
    if (
        "what is your name" in text
        or "what's your name" in text
        or "who are you" in text
        or "your name" in text
        or "what are you called" in text
        or "tell me your name" in text
    ):
        return f"My name is {BOT_NAME}."

    # Greetings
    elif any(word in text for word in ["hi", "hello", "hey"]):
        return f"Hello! I'm {BOT_NAME}. Ask me about productivity, habits, motivation, sleep, stress, health, or time management."

    # Sleep
    elif "sleep" in text:
        return "For better sleep, try going to bed at the same time each night, avoid screens before bed, and reduce caffeine later in the day."

    # Productivity / focus
    elif "productivity" in text or "focus" in text:
        return "A good productivity method is to work in focused blocks. Try 25 minutes of work, then take a 5 minute break."

    # Motivation
    elif "motivation" in text or "motivated" in text:
        return "Motivation often comes after action. Start with one small step and build momentum from there."

    # Habits
    elif "habit" in text or "habits" in text:
        return "The best way to build a habit is to make it small and repeatable. Attach it to something you already do every day."

    # Health
    elif "health" in text or "exercise" in text or "fitness" in text:
        return "A simple health tip is to focus on consistency: daily walking, enough water, better sleep, and regular movement all add up."

    # Time management
    elif "time" in text or "schedule" in text or "manage my day" in text:
        return "Try planning your day using three priorities only. Finish the most important one first."

    # Stress
    elif "stress" in text or "anxious" in text or "overwhelmed" in text:
        return "When you feel overwhelmed, write everything down, then choose just one next step."

    # Default
    else:
        return f"I'm {BOT_NAME}. I can help with productivity, habits, motivation, sleep, stress, health, and time management."


if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask something...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    reply = get_bot_reply(prompt)

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)
