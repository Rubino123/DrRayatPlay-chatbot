import streamlit as st
from groq import Groq

import os
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


st.markdown("""
<h1 style='font-size: 42px; font-family: Georgia, serif; font-weight: bold;'>
    Dr. Ray at Play <span style='font-size: 20px; font-weight: normal; opacity: 0.8;'>chatbot</span>
</h1>
""", unsafe_allow_html=True)


user_input = st.text_input("Ask me anything - Go ahead:")


if st.button("Send"):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    st.write(response.choices[0].message.content)

