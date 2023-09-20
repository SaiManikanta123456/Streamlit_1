
import openai
import streamlit as st
from dotenv import load_dotenv
import os

# Set your OpenAI API key here

load_dotenv()

openai.api_key = os.getenv("API_KEY")

# Initialize Streamlit app title
st.title("Student Assistant")

# Initialize variables if not present in session state
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
if prompt := st.chat_input("Ask a question related to data science or machine learning"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.spinner("Hold on a moment saii...."):
        assistant_response = openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ]
        )['choices'][0]['message']['content']

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)

    # Explain the assistant's response
    # st.write("Explanation:")
    # if "data science" in prompt.lower():
    #     st.write("The assistant provided information about data science and its applications.")
    #     st.write("You can further explore this topic by reading relevant articles or textbooks.")
    # elif "machine learning" in prompt.lower():
    #     st.write("The assistant explained the basics of machine learning and its importance.")
    #     st.write("You can dive deeper into this topic through online courses or tutorials.")

    # Save the assistant response in the session state
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
