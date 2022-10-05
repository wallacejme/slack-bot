# slack-bot
A python bot that posts messages to Slack channels

## Setup

### Install dependencies
```
pip install -Ur requirements.txt
```

### Ajust configurations
Create a `config.yaml` file by creating a copy of `config.TEMPLATE.yaml`.
```
cp config.TEMPLATE.yaml config.yaml
```

Edit it to match your slack app credentials.

## Usage
```
python slackbot.py (-c | --channel) CHANNEL MESSAGE
```
