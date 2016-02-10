from slackbot.bot import respond_to
from slackbot import utils
import re

@respond_to('joke (.*)')
def joke(message, category):
    url = "https://webknox-jokes.p.mashape.com/jokes/search?&keywords=" + category + "&minRating=5&numJokes=1"
    headers={
        "X-Mashape-Key": "LM6TApHaSPmshsDRI2S9h2W5eYvNp1Iin3Vjsn2ZncHbuAbsHt",
        "Accept": "application/json"
      }
    story = utils.get_json_with_headers(url, headers)
    if story and len(story):
        message.reply(story[0]["joke"])
    else:
        message.send("Couldn't find a joke or you're out of free jokes for the day (limit 5)")