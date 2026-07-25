############################################################
# IMPORTS
############################################################
import streamlit as st
from groq import Groq
from PIL import Image
import os

############################################################
# GROQ CLIENT (Chatbot engine)
############################################################
# Uses your private Streamlit Secret
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

############################################################
# TOP BANNER (Ocean background)
############################################################
ocean = Image.open("background.png")
thin_ocean = ocean.crop((0, 0, ocean.width, 500))
st.image(thin_ocean, width=900)

############################################################
# DIVIDER BELOW BANNER
############################################################
st.markdown(
    "<hr style='margin:0; border: none; border-top: 2px solid #ffffff33;'>",
    unsafe_allow_html=True
)

############################################################
# HEADER SECTION (Shark icon + Dr. Ray at Play title)
############################################################
col1, col2 = st.columns([1, 6])

with col1:
    st.image("Shark.png", width=80)

with col2:
    st.markdown("""
    <div style='padding-top: 12px;'>
        <h1 style='font-size: 42px; font-family: Georgia, serif; font-weight: bold; margin: 0;'>
            <span style='color: #00bcd4;'>Dr. Ray at Play</span>
            <span style='font-size: 32px; font-weight: normal; vertical-align: super; color: #0088CC;'>™</span>
            <span style='font-size: 20px; font-weight: normal; opacity: 0.8; color: red;'> chatbot</span>
        </h1>
    </div>
    """, unsafe_allow_html=True)

############################################################
# INPUT WIDGET KEY (needed for Clear button)
############################################################
if "input_key" not in st.session_state:
    st.session_state.input_key = "chat_input_1"

############################################################
# INPUT BOX
############################################################
user_input = st.text_input(
    "Ask me anything - Go ahead:",
    key=st.session_state.input_key
)

############################################################
# BUTTON ROW (Send + Clear)
############################################################
colA, colB = st.columns([1, 1])
with colA:
    send_clicked = st.button("Send")
with colB:
    clear_clicked = st.button("Clear")

############################################################
# CLEAR BUTTON BEHAVIOR
############################################################
if clear_clicked:
    st.session_state.input_key = f"{st.session_state.input_key}_x"
    st.rerun()

############################################################
# SEND BUTTON BEHAVIOR
############################################################
if send_clicked:
    if not user_input.strip():
        st.write("How can I help you?")
    else:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": user_input}]
        )
        st.write(response.choices[0].message.content)

st.markdown("""
<hr style='margin-top: 40px; border: none; border-top: 1px solid #66c2ff55;'>

<div style='text-align: center; font-size: 16px; color: #0088CC; padding-top: 10px;'>
    ~ Thanks for chatting with <span style='font-weight: bold;'>Dr. Ray at Play</span><span style='font-size: 14px; vertical-align: super;'>™</span> ~
</div>

<div style='text-align: center; font-size: 14px; opacity: 0.8; padding-top: 12px;'>
    © 2026 DrRayatPlay.com ~ All Rights Reserved.
</div>

<div style='text-align: center; font-size: 13px; opacity: 0.7; padding-top: 4px;'>
    Designed and Developed by Sharon Rubino, B.S., MCS
</div>
""", unsafe_allow_html=True)


