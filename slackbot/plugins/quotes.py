from slackbot.bot import respond_to
from slackbot import utils

@respond_to('quote (.*)')
def joke(message, person_name):
    url = "http://www.iheartquotes.com/api/v1/random?source=%s"
    #second_url = "http://en.wikiquote.org/w/api.php"
    if person_name:
        quote_api = url % person_name.replace(' ','_')
        user_quote = utils.get_text(quote_api)
        if user_quote:
            return user_quote
        else:
            return "Never heard of him."