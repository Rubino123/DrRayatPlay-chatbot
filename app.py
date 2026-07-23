import streamlit as st
from groq import Groq
from PIL import Image
import os

# Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Wide, thin ocean strip (Streamlit-safe cropping)
ocean = Image.open("background.png")
thin_ocean = ocean.crop((0, 0, ocean.width, 500))   # 500px tall strip
st.image(thin_ocean, width=900)

# Divider line
st.markdown("<hr style='margin:0; border: none; border-top: 2px solid #ffffff33;'>", unsafe_allow_html=True)

# Shark + Header using Streamlit columns
col1, col2 = st.columns([1, 6])

with col1:
    st.image("Shark.png", width=80)

with col2:
    st.markdown("""
    <div style='padding-top: 12px;'>
        <h1 style='font-size: 42px; font-family: Georgia, serif; font-weight: bold; margin: 0;'>
            <span style='color: #00bcd4;'>DrRayatPlay</span>
            <span style='font-size: 32px; font-weight: normal; vertical-align: super; color: #0088CC;'>™</span>
            <span style='font-size: 20px; font-weight: normal; opacity: 0.8; color: red;'> chatbot</span>
        </h1>
    </div>
    """, unsafe_allow_html=True)

# User input
user_input = st.text_input("Ask me anything - Go ahead:")

# Chatbot response
if st.button("Send"):
    if not user_input.strip():
        st.write("How can I help you?")
    else:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": user_input}]
        )
        st.write(response.choices[0].message.content)

