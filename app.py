from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from response import chat_answer

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():

  # Use this data in your application logic
  message = request.form['Body']

  # Get answer from ChatGPT
  chatbot_reply = chat_answer(message)
    
  # Initialize TwiML response
  resp = MessagingResponse()
    
  # Add a message
  resp.message(chatbot_reply)
  return str(resp)

if __name__ == "__main__":
  app.run()


