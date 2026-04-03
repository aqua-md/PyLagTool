import json

def get_file():
    with open("settings.json","r") as f:
        settings = json.load(f)
        f.close()
    return settings["GameFile"]

def get_rev():
    with open("settings.json","r") as f:
        settings = json.load(f)
        f.close()
    return settings["GameVersion"]

def get_FPS():
    with open("settings.json","r") as f:
        settings = json.load(f)
        f.close()
    return float(settings["MinFPS"]),float(settings["MaxFPS"])

def get_hotkey():
    with open("settings.json","r") as f:
        settings = json.load(f)
        f.close()
    return settings["Hotkey"]
