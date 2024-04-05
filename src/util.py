import json
def get_discord_token():
    token = json.load(open('../token.json'))["discord-token"]
    return token

