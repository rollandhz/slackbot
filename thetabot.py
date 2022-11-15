
import slack
import ssl
import certifi
import os
from flask import Flask
from slackeventsapi import SlackEventAdapter


SLACK_TOKEN = "xoxb-4371162915714-4371269398274-Q9XLixuObnCzHMHrtCXO9moG"
SIGNING_SECRET = "a5e6fccd30ca4c6443d9be7921f286d2"

ssl._create_default_https_context = ssl._create_unverified_context
sc = slack.WebClient(SLACK_TOKEN,ssl=ssl._create_default_https_context)


app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(SIGNING_SECRET, '/slack/events', app)

client = slack.WebClient(token=SLACK_TOKEN)

@ slack_event_adapter.on('message')
def message(payload):
    print(payload)
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
    print(text)
    if text == "hi":
        client.chat_postMessage(channel=channel_id,text="Hello")


if __name__ == "__main__":
	app.run(debug=True)