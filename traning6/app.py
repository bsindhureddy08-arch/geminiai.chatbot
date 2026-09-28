import streamlit as st
import ollama

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI CHATBOT")
st.write("Welcome to your AI chatbot!")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Enter your prompt...")

if prompt:
    # Show user message
    st.chat_message("user").write(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Send conversation to Ollama
    response = ollama.chat(
        model="llama3.2",
        messages=st.session_state.messages
    )

    answer = response["message"]["content"]

    # Show AI response
    st.chat_message("assistant").write(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })