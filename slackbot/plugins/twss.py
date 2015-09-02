import re
from slackbot.bot import listen_to
import random

@listen_to("(big|small|long|hard|soft|mouth|face|good|fast|slow|in there|on there|in that|on that|wet|dry|suck|blow|jaw|all in|fit that|fit it|hurts|hot|huge|balls|stuck|deep)", re.IGNORECASE)
def twss(message):
    if random.choice(range(10)) == 1:
        message.send("THAT'S WHAT SHE SAID!")