import json

def write_settings(game_file, revision, min_fps, max_fps, hotkey):
    try:
        min_fps = int(min_fps)
        max_fps = int(max_fps)

        with open("settings.json","w") as f:
            settings = json.dumps({"GameFile":game_file, "GameVersion":revision, "MinFPS":min_fps, "MaxFPS":max_fps, "Hotkey":hotkey}, separators = (",", ":"), indent=4)
            f.write(settings)
            f.close()
        return True
    except ValueError:
        print("Min or Max FPS is not valid")
