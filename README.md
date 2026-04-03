## **USECASE**

Writes to memory addresses of a given executable to limit a UE4 game's framerate to cause lag. 

The program finds the executable name and memory address from a file in the GameJSON folder


## **INSTALLATION**

- To use this program, download the code as a zip and extract it.

- Open a terminal window in that folder

- install the necessary packages with (ideally in a [virtual environment]([url](https://docs.python.org/3/library/venv.html))):
```
pip install -r requirements.txt
```
- run the following code to start the lag tool

```
python ./GUI.py
```




## **ADDITIONAL INFO**


Project based on [GordoLagTool]([url](https://github.com/GordoLeal/GordoLagTool)). 


Creating a GameJSON is done in a similar way to creating a .game file (setting the FrameRateLimit value in the game's 'GameUserSettings.ini' to a large number (eg: 123456.0), except by using the program [GameConqueror]([url](https://github.com/scanmem/scanmem)) instead of CheatEngine. 



