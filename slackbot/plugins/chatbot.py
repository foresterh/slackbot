import random
import re
from slackbot.bot import listen_to
from chatterbot import ChatBot

chatty = ChatBot("Marvin")
talked_to = False

@listen_to('.*', re.IGNORECASE)
def chat(message):
    global chatty
    global talked_to

    #message = bot_input.input_string.replace(bot_output.nick.lower(), '{user_nick}').replace('0','').replace('@','')
    response = chatty.get_response(message.body['text'])
    #if (bot_input.direct_message or talked_to or random.randrange(10) == 1) and response:
    if (random.randrange(10) == 1) and response:
        message.send(response)
        #talked_to = bot_input.direct_message
