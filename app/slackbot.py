import os

from dotenv import load_dotenv
import slack

load_dotenv()


SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")

slack_client = slack.WebClient(token=SLACK_BOT_TOKEN)

slack_client.chat_postMessage(channel="general", text="Hello World!")