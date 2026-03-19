import random
import re
import streamlit as st

BOT_NAME = "Life Hacker"

st.set_page_config(page_title=f"{BOT_NAME} Bot", page_icon="🤖", layout="centered")
st.title(f"🤖 {BOT_NAME}")
st.caption("Ask about productivity, habits, motivation, sleep, stress, health, or time management.")


# ----------------------------
# Helper functions
# ----------------------------
def clean_text(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", "", text)
    return text


def contains_any(text: str, keywords: list[str]) -> bool:
    return any(word in text for word in keywords)


def pick_response(options: list[str]) -> str:
    return random.choice(options)


# ----------------------------
# Bot response logic
# ----------------------------
def get_bot_reply(prompt: str) -> str:
    text = clean_text(prompt)

    # Name / identity
    if contains_any(text, [
        "what is your name",
        "whats your name",
        "who are you",
        "your name",
        "what are you called",
        "tell me your name"
    ]):
        return f"My name is {BOT_NAME}. I help with productivity, habits, motivation, sleep, stress, health, and time management."

    # Greeting
    if text in ["hi", "hello", "hey", "hiya", "yo", "good morning", "good evening"]:
        return pick_response([
            f"Hello! I'm {BOT_NAME}. What would you like help with today?",
            f"Hey! I'm {BOT_NAME}. Ask me about sleep, focus, habits, stress, or time management.",
            f"Hi! I'm {BOT_NAME}. Tell me what you're struggling with and I'll try to help."
        ])

    # Thanks
    if contains_any(text, ["thanks", "thank you", "thx"]):
        return pick_response([
            "You're welcome.",
            "No problem.",
            "Glad to help.",
            "Anytime."
        ])

    # Sleep
    if contains_any(text, [
        "sleep", "sleeping", "insomnia", "cant sleep", "cannot sleep",
        "bedtime", "rest", "wake up tired", "tired in the morning"
    ]):
        return pick_response([
            "To sleep better, try going to bed and waking up at the same time each day, avoid screens before bed, and reduce caffeine later in the day.",
            "A better sleep routine usually starts with consistency. Keep a regular bedtime, make your room cool and dark, and avoid heavy meals late at night.",
            "If your sleep is poor, focus on a simple evening routine: dim lights, avoid your phone, and give yourself time to wind down properly."
        ])

    # Productivity / focus / procrastination
    if contains_any(text, [
        "productive", "productivity", "focus", "concentrate",
        "concentration", "procrastinate", "procrastination",
        "get more done", "be more productive", "stay focused"
    ]):
        return pick_response([
            "To be more productive, choose one main priority, remove distractions, and work in short focused blocks such as 25 minutes on and 5 minutes off.",
            "A simple productivity method is to decide your top 3 tasks for the day and do the hardest one first before checking messages too often.",
            "If you want better focus, reduce multitasking, put your phone away, and work on one clear task at a time."
        ])

    # Motivation
    if contains_any(text, [
        "motivation", "motivated", "unmotivated", "lazy",
        "no motivation", "cant get started", "cannot get started"
    ]):
        return pick_response([
            "Motivation often comes after action, not before it. Start with one very small step and build momentum from there.",
            "When you feel unmotivated, make the task easier. Aim to begin for just 5 minutes instead of trying to do everything at once.",
            "A good trick for motivation is lowering the barrier to start. Small wins create momentum."
        ])

    # Habits / routines / discipline
    if contains_any(text, [
        "habit", "habits", "routine", "routines", "discipline",
        "build a habit", "good habits", "daily routine"
    ]):
        return pick_response([
            "The best way to build a habit is to make it small and repeatable. Start so small that it feels easy to do every day.",
            "To create a strong habit, attach it to something you already do, like stretching after brushing your teeth or reading after dinner.",
            "Consistency matters more than intensity. A small habit done daily beats a big habit done occasionally."
        ])

    # Stress / anxiety / overwhelmed
    if contains_any(text, [
        "stress", "stressed", "anxious", "anxiety",
        "overwhelmed", "burnout", "too much on", "panic"
    ]):
        return pick_response([
            "When you feel overwhelmed, write everything down, then choose just one next step. Clarity reduces stress.",
            "A helpful way to handle stress is to slow things down. Breathe, list what is in your control, and focus on one thing at a time.",
            "If you are stressed, try reducing mental clutter first. Get your thoughts out of your head and onto paper."
        ])

    # Health / fitness / exercise
    if contains_any(text, [
        "health", "healthy", "exercise", "fitness",
        "workout", "walking", "diet", "energy"
    ]):
        return pick_response([
            "A simple health approach is to focus on basics: daily movement, enough water, regular sleep, and balanced meals.",
            "You do not need a perfect routine. Walking more, sleeping better, and staying consistent with movement can improve your health a lot.",
            "If you want better health, start with habits you can keep: regular movement, better sleep, and fewer extremes."
        ])

    # Time management / planning
    if contains_any(text, [
        "time management", "manage my time", "schedule",
        "planning", "plan my day", "busy", "too busy",
        "manage my day", "organise my day", "organize my day"
    ]):
        return pick_response([
            "A good time management habit is to plan your day around just 3 main priorities instead of trying to do everything.",
            "If your day feels too busy, block out time for important work first and leave smaller tasks for later.",
            "A strong daily plan starts with one must-do task, two should-do tasks, and everything else after that."
        ])

    # Morning routines
    if contains_any(text, [
        "morning routine", "morning", "start my day", "better morning"
    ]):
        return pick_response([
            "A good morning routine can be simple: wake up at a consistent time, drink water, avoid checking your phone immediately, and start with one clear task.",
            "For a better morning, keep the first 30 minutes calm and intentional. Light, water, movement, and a clear plan can help a lot."
        ])

    # Evening routines
    if contains_any(text, [
        "evening routine", "night routine", "before bed"
    ]):
        return pick_response([
            "A good evening routine helps you slow down. Reduce screen time, dim the lights, and prepare for the next day before bed.",
            "For a calmer evening, keep things simple: tidy up, stop work properly, and give your brain time to switch off."
        ])

    # General help / what can you do
    if contains_any(text, [
        "help", "what can you do", "what do you do", "how can you help"
    ]):
        return (
            f"I'm {BOT_NAME}. I can help with productivity, focus, motivation, habits, sleep, stress, health, and time management. "
            "Try asking something like 'how can I stop procrastinating' or 'how do I sleep better'."
        )

    # Very short unclear messages
    if len(text.split()) <= 2:
        return (
            f"I can help with productivity, sleep, stress, habits, health, and time management. "
            "Try asking a full question, like 'how can I focus better at work?'"
        )

    # Default fallback
    return (
        f"I’m {BOT_NAME}. I’m not fully AI-powered, so I work best on topics like productivity, habits, motivation, sleep, stress, health, and time management. "
        "Try asking something more specific in one of those areas."
    )


# ----------------------------
# Sidebar
# ----------------------------
with st.sidebar:
    st.header("Try asking")
    st.write("- How can I sleep better?")
    st.write("- How do I stop procrastinating?")
    st.write("- How can I build better habits?")
    st.write("- How do I manage stress?")
    st.write("- How can I be more productive?")
    st.write("- How should I plan my day?")

    if st.button("Clear chat"):
        st.session_state.messages = []
        st.rerun()


# ----------------------------
# Chat state
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": f"Hello! I'm {BOT_NAME}. Ask me about productivity, habits, motivation, sleep, stress, health, or time management."
        }
    ]


# ----------------------------
# Display chat history
# ----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# ----------------------------
# Chat input
# ----------------------------
prompt = st.chat_input("Ask something...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    reply = get_bot_reply(prompt)

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)
