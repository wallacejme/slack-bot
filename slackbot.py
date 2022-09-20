import os
import sys
import argparse

import oyaml as yaml
from slack_bolt import App
from slack_sdk.errors import SlackApiError


# Sets up command line interface
cli_parser = argparse.ArgumentParser(
    prog="python slackbot.py",
    description="Sends message to a Slack channel"
)

cli_parser.add_argument("Message",
                        metavar="message",
                        type=str,
                        help="the message to be sent")

cli_parser.add_argument("-c",
                        "--channel",
                        type=str,
                        help="the channel the message will be sent to",
                        required=True)

args = cli_parser.parse_args()


# Loads app settings
path = os.environ.get("SLACKBOT_CONFIG_FILE_PATH", "config.yaml")
with open(path, "r") as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print("Error: couldn't load config file.")
        print(f"Exception trown: {exc}")
        sys.exit()


# Validates config file
for key in config.keys():
    if config.get(key) is None:
        print(f"ERROR: Setting '{key}' in {path} is missing.")
        sys.exit()


# Initializes app with your bot token and signing secret
app = App(
    token=config.get("slack_bot_token"),
    signing_secret=config.get("slack_signing_secret")
)

channel_id = None
channel_name = args.channel
message = args.Message
try:
    # Call the conversations.list method using the WebClient
    for result in app.client.conversations_list():
        if channel_id is not None:
            break
        for channel in result["channels"]:
            if channel["name"] == channel_name:
                channel_id = channel["id"]
                #Print result
                print(f"Found conversation ID: {channel_id}")
                break

    # Call the conversations.list method using the WebClient
    result = app.client.chat_postMessage(
        channel=channel_id,
        text=message
        # You could also use a blocks[] array to send richer content
    )
    # Print result, which includes information about the message (like TS)
    print(result)

except SlackApiError as e:
    print(f"Error: {e}")