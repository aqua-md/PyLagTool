from pynput import keyboard
import sys
#---custom packages---
from setFPS import setFPS
import gameInfo
import settings

listener = 0

def start_listener():
    global listener

    min_fps,max_fps = settings.get_FPS()
    revision = settings.get_rev()
    game_file = settings.get_file()
    hotkey = getattr(keyboard.Key, settings.get_hotkey()) #puts hotkey in settings file into readable data for pynput



    game_json = gameInfo.get_json(game_file)
    game = gameInfo.get_game(game_json)
    address = gameInfo.get_pointer(game_json,revision)

    def on_press(key, injected):
        if key == hotkey: #keyboard.Key.[hotkey]
            setFPS(min_fps,game,address)

    def on_release(key, injected):
        if key == hotkey:
            setFPS(max_fps,game,address)

    # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

def stop_listener():
    global listener
    listener.stop()
