from slackbot.bot import listen_to, respond_to
import random
import socket
import os

if os.name != "nt":
    import fcntl
    import struct

    def get_interface_ip(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack(b'256s',
                                ifname[:15]))[20:24])

def get_lan_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = [
            "eth0",
            "eth1",
            "eth2",
            "wlan0",
            "wlan1",
            "wifi0",
            "ath0",
            "ath1",
            "ppp0",
            ]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break
            except IOError:
                pass
    return ip

@listen_to('ping')
@respond_to('ping')
def ping(message):
    """.ping -- see if I'm actually listening or off in the corner sleeping"""
    #bot_output.say(random.choice(bot_output.responses["pinging"]))
    message.reply("I gotcha ping right here")



@listen_to('location')
@respond_to('location')
def location(message):
    """.location -- get my ip address and hostname"""
    hostname = socket.gethostname()
    ip = get_lan_ip()
    message.reply("{0} - {1}".format(hostname, ip))


@respond_to('leave (.*)')
def leave_channel(message, channel):
