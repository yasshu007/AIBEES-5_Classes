import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7,  # 0 - 2
    # max_output_tokens=100,
)
st.title("Welcome to the Personalized Chatbot of YASH:")
st.title("type exit or quit to end:")
st.balloons()

print("--- Welcome to the Personalized Chatbot (type 'exit' or 'quit' to end) --- ")
user_input = st.text_input("You: ")
while True:
    #user_input = st.text_input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input}
    ]
    #response = llm.invoke(messages)
    #print(f"Bot: {response.content}")

    st.write("**Answer:**")
    #st.write(response.content)
    st.balloons()

