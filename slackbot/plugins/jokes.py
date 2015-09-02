from slackbot.bot import respond_to
from slackbot import utils
import re

@respond_to('joke')
def joke(message):
    joke_body = utils.get_json("http://webknox.com/api/jokes/random")
    message.reply(joke_body["joke"])