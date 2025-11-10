import streamlit as st
from openai import OpenAI

# Load OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("💬 Mini ChatGPT (Powered by GPT-4)")
st.caption("Type below to chat. Type 'exit' to quit.")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat
for msg in st.session_state.messages:
    with st.chat_message("user" if msg["role"] == "user" else "assistant"):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Say something…")

if prompt:
    if prompt.lower() == "exit":
        st.toast("👋 Goodbye!")
    else:
        # Show user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking…"):
                response = client.chat.completions.create(
                    model="gpt-4o-mini",  # Lightweight GPT-4 model
                    messages=[
                        {"role": "system", "content": "You are a friendly AI assistant."},
                        *st.session_state.messages
                    ]
                )
                reply = response.choices[0].message.content
                st.markdown(reply)

        # Save AI reply
        st.session_state.messages.append({"role": "assistant", "content": reply})
