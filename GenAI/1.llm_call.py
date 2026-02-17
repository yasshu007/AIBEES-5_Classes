import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Initialize the model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
        google_api_key = os.getenv("GOOGLE_API_KEY"),
            temperature=0) # 0 - 2  

            # Prepare messages system and user
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    #{"role": "user", "content": "Who is Vikesh Pulimamidi?"}
    #{"role": "user", "content": "Who is Gadiraju Yashwanth Kumar Raju?"}
    {"role": "user", "content": "Who is Movva Raiteja?"}
           ]

# Invoke the model
response = llm.invoke(messages)
print(response.content)