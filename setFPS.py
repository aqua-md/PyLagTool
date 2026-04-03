import PyMemoryEditor


def setFPS(fps,game_name,address):
    try:
        with PyMemoryEditor.OpenProcess(process_name=game_name) as process:
            process.write_process_memory(address,  float, 4, fps)
    except (PyMemoryEditor.ProcessNotFoundError):
            print("Unable to find process:",game_name)
