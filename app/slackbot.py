import os
import logging

from dotenv import load_dotenv
import requests
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


logging.basicConfig(level=logging.DEBUG)


load_dotenv()


SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_SIGNING_SECRET = os.environ["SLACK_SIGNING_SECRET"]
DRIVE_SEARCH_ENDPOINT = os.environ["DRIVE_SEARCH_ENDPOINT"]


# Initializes your app with your bot token and socket mode handler
app = App(token=SLACK_BOT_TOKEN)


@app.command("/drive")
def handle_drive_command(ack, body, logger, say):
    ack()
    search_text = body.get("text", "")
    logger.info(body)
    logger.info(f"Searching for {search_text}.")
    url = f"{DRIVE_SEARCH_ENDPOINT}{search_text}"
    response = requests.get(url)

    if response.status_code == 200:
        response_dict = response.json()
        list_results = response_dict["results"]
        file_details= [f"{l["filename"]}, {l["file_key"]}" for l in list_results]
        full_text_output = f"Related docs from your drive \n: {'\n'.join(file_details)}"
        say(full_text_output)
    else:
        say("ERROR!")


if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
