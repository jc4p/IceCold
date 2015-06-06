from flask import Flask
from random import choice
import twilio.twiml

app = Flask(__name__)

messages = [
    "Come on bro...",
    "Seriously?!",
    "What would Jesus do?",
    "http://i.imgur.com/cUBPKRL.jpg"
]

@app.route("/")
def hello():
    return "This host is used by <a href='https://github.com/jc4p/KeepItCool'>https://github.com/jc4p/KeepItCool</a>"

@app.route("/incoming", methods=["GET", "POST"])
def incoming():
    resp = twilio.twiml.Response()
    response_text = choice(messages)
    if response_text.startswith("http"):
        resp.message("").media(response_text)
    else:
        resp.message(response_text)
    
    return str(resp)
    

if __name__ == "__main__":
    app.run()
