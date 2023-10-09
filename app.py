import streamlit as st


# st.set_page_config(page_title="Dictateor", page_icon=":speech_balloon:", layout="wide")
st.set_page_config(page_title="MedLearn", page_icon=":pill:")
st.title("MedLearn")
st.write("Hello I am MedLearn a virtual assistant custom trained to asnwser your medical questions!", font=("arial", 20))
st.write("Ask me anything!")


user_input = st.text_input("You:", "")

# Define a function to generate bot responses
def chatbot_response(user_message):
    # Replace this with your chatbot logic
    # You can use any chatbot library or API here
    # For simplicity, let's echo the user's message
    return f"Bot: {user_message}"

# Check if the user has entered a message
if user_input:
    # Display the user's message
    st.text(f"You: {user_input}")

    # Generate and display the bot's response
    bot_response = chatbot_response(user_input)
    st.text(bot_response)

# Add a submit button
st.button("Submit")

# Add a clear button to reset the conversation
if st.button("Clear"):
    user_input = ""