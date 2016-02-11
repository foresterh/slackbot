from slackbot.bot import listen_to, respond_to
import random

#
# @listen_to('awesome')
# def awesome(message):
#     message.send(random.choice(bot_output.responses["awesome_sauce"]))
#
# @listen_to('how do you feel')
# def feelings(message):
#     message.send(random.choice(bot_output.responses["feelings"]))
#
# @listen_to('who are you')
# def who_am_i(message):
#     message.send(random.choice(bot_output.responses["who_am_i"]))
#
# @listen_to(r'beer me', run_always=True)
# def beer_me(message):
#     message.send(random.choice(bot_output.responses["beers"]))

@respond_to('dance')
def dance(message):
    message.send(':(-<')
    message.send(':(\-<')
    message.send(':o/-<')
    message.send(':(\-<')
    message.send(':-(/-<')
    message.send(':(\-<')
    message.send(':o-<')


# @listen_to(r'(do it)?(now|right away|hurry up)[!]*?$', run_always=True)
# def doit_now(message):
#     message.send(random.choice(bot_output.responses["doit"]))
#
#
# @listen_to(r'd(\')oh', run_always=True)
# def doh(message):
#     message.send(random.choice(bot_output.responses["doh"]))
#
#
# @listen_to(r'fail', run_always=True)
# def fail(message):
#     message.send(random.choice(bot_output.responses["failure"]))
#
#
# @listen_to(r'good morning*', run_always=True)
# def good_morning(message):
#     message = random.choice(bot_output.responses["good_morning"])
#     message.send(message)
#

# @listen_to(r'(?i)good(bye|night| evening| night)[ \t]*$', run_always=True)
# def good_night(message):
#     message.send(random.choice(bot_output.responses["good_night"]))
#

# @listen_to(r'ignore')
# def ignore(message):
#     message.send(random.choice(bot_output.responses["ignore"]))
#

@listen_to('lame')
def lame(message):
    if random.randrange(5) == 1:
        message.send("So's your face")


# @listen_to("(lol|haha|ha ha|rofl|hehe|rolfmao|lmao)")
# def laugh(message):
#     if random.randrange(5) == 1:
#         message.send(random.choice(bot_output.responses["funny"]))
#
#
# @listen_to(r'not (me|you)')
# def not_me(message):
#     message.send(random.choice(bot_output.responses["not_me"]))


@listen_to(r'(what are )?the (three |3 )?(rules|laws)')
def rules(message):
    three_rules = [
        "1. A robot may not injure a human being or, through inaction, allow a human being to come to harm.",
        "2. A robot must obey any orders given to it by human beings, except where such orders would conflict with the First Law.",
        "3. A robot must protect its own existence as long as such protection does not conflict with the First or Second Law."
    ]
    for rule in three_rules:
        message.send(rule)

# @listen_to(r'(did|are|is|can|what|where|when|why|will).*?$')
# def questions(message):
#      message.send(random.choice(bot_output.responses["answers"]))

@listen_to('slap')
def slap(message):
    message.send("/me slaps everyone in the channel")


@listen_to(r'(sudo )?make me a sandwich')
def sandwich(message, sudo):
    if sudo:
        message.send('Okay')
    else:
        message.send('What?  Make it yourself.')


# @listen_to(r'thank(s| you)')
# def thanks(message):
#     message.send(random.choice(bot_output.responses["youre_welcome"]))


@listen_to(r'(yes|no)')
def yes_no(message):
    yesno = ("Of course not.", "Wrong answer!", "Why?", "Are you sure?")
    if random.randrange(5) == 1:
        message.send(random.choice(yesno))


# @listen_to(r'welcome back')
# def welcome_back(message):
#     message.send(random.choice(bot_output.responses["welcome_back"]))


@listen_to('i give up')
def give_up(message):
    message.reply('how French of you')


@listen_to('thank god')
def give_up(message):
    message.reply("you're welcome")


@listen_to('touche')
def give_up(message):
    if random.randrange(5) == 1:
        message.send("douche")
    #bot_ouput.say("douche, {user_nick}")

# @listen_to
# @listen_to('suck', run_always=False)
# def suck(message):
#     message.send(random.choice(bot_output.responses["suck"]))