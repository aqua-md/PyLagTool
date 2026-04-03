import customtkinter #needs tk to be installed on the system
from os import listdir
import threading
#---custom packages---
from gameInfo import get_rev_list,get_json
import settings
from save import write_settings
import runner

last_listener = 0

def button_callback():

    #Kills any runner already running.
    global last_listener
    if last_listener != 0:
        runner.stop_listener()

    #Saves data currently in GUI
    if write_settings(
        file_select.get(),
        version_select.get(),
        min_fps_entry.get(),
        max_fps_entry.get(),
        hotkey_select.get(),
    ) == True:

        print("Save successful")
        listener = threading.Thread(target=runner.start_listener, daemon=True) #starts the lag tool
        last_listener = listener #tracks if lag tool is already running

        listener.start() #Bug: thread re creates itself on multiple uses.
        listener.join()

        print("Lag tool active")

    else: print("Invalid input detected")

#reads from settings file for last used values.
min_fps,max_fps = settings.get_FPS()
revision = settings.get_rev()
game_file = settings.get_file()
hotkey = settings.get_hotkey()

rev_list = get_rev_list(get_json(game_file))

#this needs to be abstracted to not rely on a hard coded folder name.
folder_dir = "GameJSON/"
file_list = listdir(folder_dir)

modified_file_list = []
for file in file_list:
    modified_file_list.append(folder_dir+file)

#valid hotkeys from pynput keyboard documentation https://pynput.readthedocs.io/en/latest/_modules/pynput/keyboard/_base.html#Key
hotkey_list = ['alt', 'alt_l', 'alt_r', 'alt_gr', 'backspace', 'caps_lock', 'cmd', 'cmd_l', 'cmd_r', 'ctrl', 'ctrl_l', 'ctrl_r', 'delete', 'down', 'end', 'enter', 'esc', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f20', 'home', 'left', 'page_down', 'page_up', 'right', 'shift', 'shift_l', 'shift_r', 'space', 'tab', 'up', 'media_play_pause', 'media_volume_mute', 'media_volume_down', 'media_volume_up', 'media_previous', 'media_next', 'insert', 'menu', 'num_lock', 'pause', 'print_screen', 'scroll_lock']


app = customtkinter.CTk()
app.geometry("450x250")

file_select = customtkinter.StringVar(value=game_file)
file_combobox = customtkinter.CTkComboBox(app, values=modified_file_list, variable=file_select,state="readonly")
file_combobox.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=3)


version_label = customtkinter.CTkLabel(app, text="Revision:")
version_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")

version_select = customtkinter.StringVar(value=revision)
version_combobox = customtkinter.CTkComboBox(app, values=rev_list, variable=version_select,state="readonly")
version_combobox.grid(row=1, column=1, sticky="ew")


version_label = customtkinter.CTkLabel(app, text="Hotkey:")
version_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")

hotkey_select = customtkinter.StringVar(value=hotkey)
hotkey_combobox = customtkinter.CTkComboBox(app, values=hotkey_list, variable=hotkey_select,state="readonly",width=175)
hotkey_combobox.grid(row=3, column=1, sticky="ew")


min_label = customtkinter.CTkLabel(app, text="Min FPS:")
min_label.grid(row=1, column=2, padx=20, pady=10, sticky="w")

min_fps_entry = customtkinter.CTkEntry(app, width=50)
min_fps_entry.insert(0, int(min_fps))
min_fps_entry.grid(row=1, column=2, padx=20, pady=10, sticky="e")



max_label = customtkinter.CTkLabel(app, text="Max FPS:")
max_label.grid(row=2, column=2, padx=20, pady=10, sticky="w")

max_fps_entry = customtkinter.CTkEntry(app, width=50)
max_fps_entry.insert(0, int(max_fps))
max_fps_entry.grid(row=2, column=2, padx=20, pady=10, sticky="e")


button = customtkinter.CTkButton(app, text="Run Lag Tool", command=button_callback)
button.grid(row=3, column=2, padx=20, sticky="e")

app.mainloop()
