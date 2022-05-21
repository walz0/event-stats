import json

# https://www.reddit.com/r/smashbros/comments/71e6sq/twitch_extension_for_smash_calling_all_developers/

with open("colbol.json", "r") as data:
    colbol = json.loads(data.read())["result"]
    print(colbol[list(colbol.keys())[0]]["sets"])
