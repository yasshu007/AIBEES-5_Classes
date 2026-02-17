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

st.title("Yash: LLM Details Checkpoint")
st.balloons()

name = st.text_input("Enter your Name:")
age = st.number_input("Enter your age:")
expertise = st.text_input("Enter your area of expertise:")

if st.button("Get Answer"):
    messages = [
        {"role": "system", "content": "You are a helpful assitant."},  
        {"role": "user", "content": name + "who has experience in " + expertise }
        ]
    st.write("**Answer:**")
    st.write(llm.invoke(messages).content)
    st.balloons()

