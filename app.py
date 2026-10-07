import json
import requests
import streamlit as st

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="AI Chatbot - Local Ollama Studio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Polished Custom CSS (Modern Glassmorphic UI)
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

/* Global Font & Spacing */
html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
}

code, pre {
    font-family: 'JetBrains Mono', monospace !important;
}

/* Center and pad the main view cleanly */
.block-container {
    max-width: 980px;
    padding-top: 1.8rem;
    padding-bottom: 5rem;
}

/* Top Hero Banner */
.hero-card {
    background: radial-gradient(120% 120% at 50% 0%, #1e293b 0%, #0f172a 70%, #020617 100%);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    padding: 28px 32px;
    margin-bottom: 24px;
    box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.45);
    position: relative;
    overflow: hidden;
}

.hero-card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(52, 211, 153, 0.6), transparent);
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 4px 12px;
    border-radius: 9999px;
    background: rgba(34, 197, 94, 0.12);
    border: 1px solid rgba(34, 197, 94, 0.3);
    color: #4ade80;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    margin-bottom: 12px;
}

.pulse-dot {
    width: 6px;
    height: 6px;
    background-color: #22c55e;
    border-radius: 50%;
    box-shadow: 0 0 8px #22c55e;
}

.brand-title {
    font-size: 30px;
    font-weight: 800;
    color: #f8fafc;
    letter-spacing: -0.02em;
    margin: 0 0 6px 0;
}

.green-gradient {
    background: linear-gradient(135deg, #4ade80, #10b981);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.brand-subtitle {
    font-size: 14.5px;
    color: #94a3b8;
    line-height: 1.5;
    margin-bottom: 10px;
}

.meta-pill-container {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 10px;
}

.meta-pill {
    font-size: 11.5px;
    font-weight: 500;
    color: #cbd5e1;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.07);
    padding: 3px 10px;
    border-radius: 6px;
}

/* Chat Message Containers */
[data-testid="stChatMessage"] {
    background: rgba(15, 23, 42, 0.55) !important;
    border: 1px solid rgba(255, 255, 255, 0.06) !important;
    border-radius: 16px !important;
    padding: 16px 20px !important;
    margin-bottom: 14px !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15) !important;
    backdrop-filter: blur(8px);
}

/* Distinguish User message card subtly */
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
    background: rgba(30, 41, 59, 0.6) !important;
    border: 1px solid rgba(99, 102, 241, 0.25) !important;
}

/* Sidebar Clean-up */
[data-testid="stSidebar"] {
    background: #090d16 !important;
    border-right: 1px solid rgba(255, 255, 255, 0.07) !important;
}

.sidebar-card {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 12px;
    padding: 14px 16px;
    margin-top: 18px;
}

.sidebar-title {
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #e2e8f0;
    margin-bottom: 8px;
}

.sidebar-note {
    font-size: 12.5px;
    color: #94a3b8;
    line-height: 1.55;
    margin: 4px 0;
}

/* Styled Clear Button */
.stButton > button {
    width: 100%;
    border-radius: 10px;
    background: linear-gradient(135deg, #10b981, #059669);
    color: #ffffff;
    font-weight: 700;
    font-size: 14px;
    border: none;
    padding: 8px 16px;
    box-shadow: 0 4px 12px rgba(16, 185, 129, 0.25);
    transition: all 0.2s ease;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #059669, #047857);
    color: #ffffff;
    box-shadow: 0 6px 18px rgba(16, 185, 129, 0.35);
    transform: translateY(-1px);
}

/* Chat Input field refinement */
[data-testid="stChatInput"] {
    border-radius: 14px !important;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header / Hero Card
# -----------------------------
st.markdown("""
<div class="hero-card">
    <div class="hero-badge">
        <span class="pulse-dot"></span> Local Inference Active
    </div>
    <div class="brand-title">Ollama <span class="green-gradient">Neural Studio</span></div>
    <div class="brand-subtitle">High-performance conversational workspace powered entirely on your machine. Privacy-first, zero cloud latency, zero token costs.</div>
    <div class="meta-pill-container">
        <span class="meta-pill">⚡ Real-time Token Streaming</span>
        <span class="meta-pill">🧠 State Memory Preservation</span>
        <span class="meta-pill">🎛️ Dynamic Sampling Control</span>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Ollama Settings
# -----------------------------
OLLAMA_URL = "http://localhost:11434/api/chat"

with st.sidebar:
    st.markdown("### ⚙️ Engine Parameters")

    model = st.selectbox(
        "Model Selection",
        ["llama3.2", "llama3.1", "llama3", "mistral", "gemma2", "qwen2.5", "qwen2.5:3b"],
        index=0
    )

    temperature = st.slider(
        "Sampling Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="0 = focused & deterministic, 1 = creative & diverse"
    )

    system_prompt = st.text_area(
        "System Instruction",
        value="You are a helpful AI assistant. Explain concepts clearly and simply. When useful, respond with examples.",
        height=120
    )

    if st.button("🗑️ Reset Context"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("""
    <div class="sidebar-card">
        <div class="sidebar-title">💡 Architecture Notes</div>
        <div class="sidebar-note">• <b>Local Engine:</b> Zero external API telemetry.</div>
        <div class="sidebar-note">• <b>Stateless Core:</b> Prior turns reinjected per cycle.</div>
        <div class="sidebar-note">• <b>Multilingual:</b> Ready for English, Telugu, & others.</div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# Helper Function
# -----------------------------
def check_ollama_running():
    try:
        response = requests.get("http://localhost:11434", timeout=3)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

# -----------------------------
# Session State / Memory
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Ollama Health Check
# -----------------------------
if not check_ollama_running():
    st.error("⚠️ Ollama daemon not reachable at `http://localhost:11434`")
    st.info("Start Ollama in terminal using:\n```bash\nollama serve\n```\nThen make sure you have the model pulled:\n```bash\nollama pull llama3.2\n```")
    st.stop()

# -----------------------------
# Show Chat History
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# Chat Input & Streaming Execution
# -----------------------------
user_prompt = st.chat_input("Ask anything... AI Chatbot is ready to assist you!")

if user_prompt:
    # 1. Display user message
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    with st.chat_message("user"):
        st.markdown(user_prompt)

    # 2. Build full messages list for Ollama
    messages_for_ollama = [{"role": "system", "content": system_prompt}]
    messages_for_ollama.extend(st.session_state.messages)

    # 3. Stream assistant response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        try:
            payload = {
                "model": model,
                "messages": messages_for_ollama,
                "stream": True,
                "options": {
                    "temperature": temperature
                }
            }

            with requests.post(OLLAMA_URL, json=payload, stream=True, timeout=120) as response:
                response.raise_for_status()

                for line in response.iter_lines():
                    if line:
                        data = line.decode("utf-8")
                        chunk = json.loads(data)

                        if "message" in chunk and "content" in chunk["message"]:
                            content = chunk["message"]["content"]
                            full_response += content
                            response_placeholder.markdown(full_response + "▌")

                        if chunk.get("done", False):
                            break

            response_placeholder.markdown(full_response)

        except requests.exceptions.HTTPError as e:
            full_response = (
                f"HTTP Error: {str(e)}\n\n"
                f"Most likely the model '{model}' is not downloaded.\n\n"
                f"Run this command in terminal:\n\n"
                f"ollama pull {model}"
            )
            response_placeholder.error(full_response)

        except Exception as e:
            full_response = f"Error: {str(e)}"
            response_placeholder.error(full_response)

    # 4. Store assistant response in memory
    st.session_state.messages.append({"role": "assistant", "content": full_response})