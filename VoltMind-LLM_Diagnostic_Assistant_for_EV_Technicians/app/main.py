import streamlit as st
import time
from pipeline.retriever import hybrid_search
from pipeline.generator import generate_diagnosis
from utils.youtube_helper import get_youtube_videos

# =========================================================
# ⚙️ PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="VoltMind | EV Diagnostics",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# 🎨 GLOBAL CSS
# =========================================================
st.markdown("""
<style>

/* Hide Streamlit UI */
header {visibility: hidden;}
footer {visibility: hidden;}
#MainMenu {visibility: hidden;}

/* Main App */
.stApp {
    background-color: #050816;
    color: white;
}

/* Login Card */
.login-card {
    background: rgba(17, 25, 40, 0.85);
    padding: 40px;
    border-radius: 24px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 0 40px rgba(0,0,0,0.3);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #0b1120;
    border-right: 1px solid rgba(255,255,255,0.05);
}

/* Chat bubbles */
.user-msg {
    background: #1e293b;
    padding: 14px;
    border-radius: 16px;
    margin-bottom: 10px;
}

.bot-msg {
    background: #111827;
    padding: 14px;
    border-radius: 16px;
    margin-bottom: 10px;
    border: 1px solid rgba(255,255,255,0.05);
}

/* Input box */
[data-testid="stChatInput"] {
    border-top: 1px solid rgba(255,255,255,0.08);
    padding-top: 10px;
}

/* Buttons */
.stButton button {
    border-radius: 12px;
    height: 45px;
    font-weight: 600;
    border: none;
}

/* Logo Glow */
.glow {
    color: #60a5fa;
    text-shadow: 0 0 15px rgba(96,165,250,0.7);
}

.small-text {
    opacity: 0.7;
    font-size: 0.9rem;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# 🧠 SESSION STATE
# =========================================================
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "messages" not in st.session_state:
    st.session_state.messages = []

if "videos" not in st.session_state:
    st.session_state.videos = []

# =========================================================
# 🔐 LOGIN PAGE
# =========================================================
if not st.session_state.authenticated:

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.3, 1])

    with col2:

        st.markdown("""
        <div class="login-card">

        <h1 style="text-align:center;">
        ⚡ <span class="glow">VoltMind</span>
        </h1>

        <p style="text-align:center; font-size:1.1rem; opacity:0.8;">
        AI-Powered EV Diagnostic Assistant
        </p>

        <br>

        <p style="text-align:center;" class="small-text">
        Diagnose EV issues, analyze faults, access repair insights,
        and interact with an intelligent automotive assistant.
        </p>

        <br><br>

        </div>
        """, unsafe_allow_html=True)

        # -----------------------------
        # 🌐 GOOGLE LOGIN
        # -----------------------------
        if st.button("🌐 Continue with Google", use_container_width=True, type="primary"):

            with st.spinner("Signing in..."):
                time.sleep(1)

            st.session_state.authenticated = True
            st.rerun()

        st.write("")

        # -----------------------------
        # ✉️ EMAIL LOGIN MOCK
        # -----------------------------
        email = st.text_input("Email Address")
        password = st.text_input("Password", type="password")

        if st.button("🔑 Sign In", use_container_width=True):

            if email and password:

                with st.spinner("Authenticating..."):
                    time.sleep(1)

                st.session_state.authenticated = True
                st.rerun()

            else:
                st.warning("Please enter email and password")

        st.markdown("""
        <p style='text-align:center; margin-top:15px;' class='small-text'>
            Don’t have an account? <span class='glow'>Create one</span>
        </p>
        """, unsafe_allow_html=True)

# =========================================================
# 🚀 MAIN APP
# =========================================================
else:

    # =====================================================
    # 📚 SIDEBAR
    # =====================================================
    with st.sidebar:

        st.markdown("""
        <h2 style='margin-top:-10px;'>
            ⚡ <span class='glow'>VoltMind</span>
        </h2>
        """, unsafe_allow_html=True)

        st.caption("EV Diagnostic Workspace")

        st.write("")

        if st.button("➕ New Chat", use_container_width=True):
            st.session_state.messages = []
            st.session_state.videos = []
            st.rerun()

        st.divider()

        st.caption("Recent Diagnostics")

        st.button("🔋 Battery Thermal Fault", use_container_width=True)
        st.button("⚙️ Motor Noise Analysis", use_container_width=True)
        st.button("🔌 Charging Port Failure", use_container_width=True)
        st.button("🛞 Uneven Tire Wear", use_container_width=True)

        st.divider()

        st.caption("System Status")
        st.success("AI Engine Online")
        st.success("Vector Database Connected")
        st.success("Gemini API Active")

        st.markdown("<br><br>", unsafe_allow_html=True)

        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.authenticated = False
            st.session_state.messages = []
            st.session_state.videos = []
            st.rerun()

    # =====================================================
    # 🏠 MAIN HEADER
    # =====================================================
    st.markdown("""
    <h1>
        ⚡ <span class='glow'>VoltMind</span>
    </h1>
    """, unsafe_allow_html=True)

    st.caption("Chat with your AI EV diagnostic assistant")

    st.write("")

    # =====================================================
    # 💬 DISPLAY CHAT
    # =====================================================
    for message in st.session_state.messages:

        if message["role"] == "user":
            st.markdown(
                f"<div class='user-msg'>🧑 {message['content']}</div>",
                unsafe_allow_html=True
            )

        else:
            st.markdown(
                f"<div class='bot-msg'>🤖 {message['content']}</div>",
                unsafe_allow_html=True
            )

    # =====================================================
    # 🎥 VIDEO SECTION
    # =====================================================
    if st.session_state.videos:

        st.subheader("🎥 Suggested Videos")

        shown = False

        for v in st.session_state.videos:

            if "watch?v=" in v["link"]:

                st.markdown(f"**{v['title']}**")

                vid = v["link"].split("v=")[-1].split("&")[0]

                st.video(f"https://www.youtube.com/watch?v={vid}")

                shown = True

        if not shown:
            st.info("Explore related EV fixes on YouTube")

    # =====================================================
    # ⌨️ CHAT INPUT
    # =====================================================
    prompt = st.chat_input(
        "Describe the EV issue (e.g., Battery overheating after long drive)..."
    )

    if prompt:

        # ---------------- USER MESSAGE ----------------
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        with st.spinner("Analyzing EV systems... ⚡"):

            # =================================================
            # 🧠 FIRST MESSAGE → FULL PIPELINE
            # =================================================
            if len(st.session_state.messages) <= 1:

                docs = hybrid_search(prompt)

                response = generate_diagnosis(prompt, docs)

                videos = get_youtube_videos(
                    prompt + " EV repair fix tutorial"
                )

                st.session_state.videos = videos

            # =================================================
            # 💬 FOLLOW-UP CHAT
            # =================================================
            else:

                context = "\n".join([
                    msg["content"]
                    for msg in st.session_state.messages
                    if msg["role"] == "assistant"
                ])

                followup_prompt = f"""
You are an EV expert assistant.

Previous context:
{context}

User follow-up:
{prompt}

Answer clearly and conversationally.
"""

                response = generate_diagnosis(followup_prompt, [])

        # ---------------- BOT MESSAGE ----------------
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

        st.rerun()