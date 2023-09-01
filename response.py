import openai
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

#Get the OpenAI API Key from .env
openai.api_key = os.getenv('OPENAI_API_KEY')

#Configure the chatbot
chat_history = [ {"role": "system", "content": "You are going to be a chatbot whose only task is  \
                  translating text from spanish to english or viceversa. Any question or query that  \
                  is not related to translation between spanish and english reply by saying: \
                  I am sorry but I can only translate between spanish and english."} ]

# Function to reply to the user
def chat_answer(messages, temperature=0):
    #Append the user´s message to the chat history
    chat_history.append({"role": "user", "content": messages})
    #Configure the chatbot
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history,
        temperature=temperature, 
    )
    #Retrieve the chatbot´s reply
    chat_answer = response.choices[0].message["content"]
    #Remove the user´s message from the chat history
    chat_history.pop()
    #return the chatbot´s answer
    return chat_answer