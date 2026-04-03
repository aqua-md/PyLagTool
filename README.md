## **USECASE**

Writes to memory addresses of a given executable to limit a UE4 game's framerate to cause lag. 

The program finds the executable name and memory address from a file in the GameJSON folder


## **INSTALLATION**

To use this program, download the code as a zip and extract it.

Open a terminal window in that folder

install the necessary packages with (ideally in a [virtual environment]([url](https://docs.python.org/3/library/venv.html))):
```
pip install -r requirements.txt
```
run the following code to start the lag tool

```
python ./GUI.py
```







Project based on [GordoLagTool]([url](https://github.com/GordoLeal/GordoLagTool)) 
