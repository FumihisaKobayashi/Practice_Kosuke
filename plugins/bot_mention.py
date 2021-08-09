from slackbot.bot import respond_to
from anime import get_anime_list
import random


@respond_to("アニメ")
def hello(message):
    anime_list = get_anime_list()
    anime = random.choice(anime_list)["title"]
    message.reply(anime)
