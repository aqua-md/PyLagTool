import json

#Purpose: Parse a game.json for its .exe and memory addresses

#find .exe
def get_game(json):
    return json["ProcessName"]

#find pointer from game version
def get_pointer(json, version):
    for i in json["PatchInfos"]:
        if i["GameVersion"] == str(version):
            return int(i["MainPointer"],16)

#read game.json file
def get_json(file):
    with open(file,"r") as f:
        load_json = json.load(f)
        f.close()
    return load_json

def get_rev_list(json):
    rev = []
    for i in json["PatchInfos"]:
        rev.append(i["GameVersion"])
    return rev
