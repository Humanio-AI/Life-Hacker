import streamlit as st

# -------------------------
# Page setup
# -------------------------
st.set_page_config(page_title="Life Hacker Chatbot", page_icon="🤖")
st.title("🤖 Life Hacker Bot")

# -------------------------
# Session state
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------
# Chatbot logic
# -------------------------
def get_bot_reply(prompt: str) -> str:
    text = prompt.lower().strip()

    # Greetings
    if any(word in text for word in ["hi", "hello", "hey"]):
        return "Hello! I’m Life Hacker Bot. Ask me about productivity, habits, motivation, or daily life tips."

    # Productivity
    elif "productivity" in text or "focus" in text:
        return (
            "A good productivity method is to work in short focused blocks. "
            "Try 25 minutes of work, then take a 5 minute break. "
            "Also remove distractions like phone notifications."
        )

    # Motivation
    elif "motivation" in text or "motivated" in text:
        return (
            "Motivation often comes after action, not before it. "
            "Start with one very small step and build momentum from there."
        )

    # Habits
    elif "habit" in text or "habits" in text:
        return (
            "The best way to build a habit is to make it small and repeatable. "
            "Attach it to something you already do every day."
        )

    # Sleep
    elif "sleep" in text:
        return (
            "For better sleep, try going to bed at the same time each night, "
            "avoid screens before bed, and reduce caffeine later in the day."
        )

    # Health
    elif "health" in text or "exercise" in text or "fitness" in text:
        return (
            "A simple health tip is to focus on consistency: daily walking, enough water, "
            "better sleep, and regular movement all add up."
        )

    # Time management
    elif "time" in text or "manage my day" in text or "schedule" in text:
        return (
            "Try planning your day using three priorities only. "
            "Finish the most important one first before moving on."
        )

    # Stress
    elif "stress" in text or "anxious" in text or "overwhelmed" in text:
        return (
            "When you feel overwhelmed, slow things down. "
            "Write down everything on your mind, then choose just one next step."
        )

    # Money
    elif "money" in text or "save" in text or "budget" in text:
        return (
            "A useful money habit is to separate spending into essentials, goals, and non-essentials. "
            "Track where your money goes each month."
        )

    # Default response
    else:
        return (
            "I’m a simple offline chatbot with no API, so I reply using built-in rules. "
            "Try asking me about productivity, habits, motivation, sleep, stress, health, or time management."
        )

# -------------------------
# Show chat history
# -------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------------
# User input
# -------------------------
prompt = st.chat_input("Ask something...")

if prompt:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get bot reply
    reply = get_bot_reply(prompt)

    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": reply})

    # Show assistant message
    with st.chat_message("assistant"):
        st.markdown(reply)
