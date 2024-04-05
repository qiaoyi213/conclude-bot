import json
def get_discord_token():
    token = json.load(open('../token.json'))["discord-token"]
    return token

def get_openai_api_key():
    token = json.load(open('../token.json'))["OPENAI_API_KEY"]
    return token