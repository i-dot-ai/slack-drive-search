import os
import logging

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

logging.basicConfig(level=logging.DEBUG)

load_dotenv()


SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_SIGNING_SECRET = os.environ["SLACK_SIGNING_SECRET"]



# Initializes your app with your bot token and socket mode handler
app = App(token=SLACK_BOT_TOKEN)


@app.message("hello")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(f"Here are the relevant contents of your Drive...")


@app.event("app_mention")
def handle_mention(body, say, logger):
    user = body["event"]["user"]
    # single logger call
    # global logger is passed to listener
    logger.debug(body)
    say(f"{user} mentioned your app")


@app.command("/drive")
def handle_some_command(ack, body, logger, say):
    ack()
    logger.info(body)
    say("wooo!")



# Start your app
if __name__ == "__main__":
    print("===========")
    print(SLACK_APP_TOKEN)
    print(SLACK_BOT_TOKEN)
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
