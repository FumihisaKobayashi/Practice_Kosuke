import os
API_TOKEN = os.environ.get('SLACK_TOKEN')

DEFAULT_REPLY = "その言葉の意味は知りません"
 
PLUGINS = [
    'slackbot.plugins'
]

