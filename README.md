# cse210-06 "Ping Pong"
Final project cse210 - winter 2022

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command

```
python3 cse210-06 
```

You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
cse210-06                 (project root folder)
    +-- assets            (information data used in the game execution)
    +-- game              (specific game classes)
        +-- elements      (various game element classes)
        +-- scene         (scene and scene manager classes)
        +-- scripting     (various game action classes)
        +-- services      (various game service classes)
    +-- __main__.py       (entry point for program)
    +-- constants.py      (game constants)
    +-- README.md         (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* Yurinii Fuentes  fue21007@byui.edu 
* Eduardo Prieto  pri21002@byui.edu


## Design
---

* Eduardo Prieto
    - Implement the basic structure
    - Implement the elements classes
    - Implement the services configuration
    - Implement the scene classes
    - Integrate the assets configuration
* Yurinii Fuentes
    - Implement the scripting actions configuration
    - Integrate constants and assets configuration
    - complete main file

## How did you ensure maintainability in your program's design?
Upon completing the integration of the code, it will be established that the values of the attributes that are responsible for intertwining the flow of the process from the initialization of the code to its execution and obtaining the expected result, and thus avoiding errors, must remain in a unified file at which the required maintainability can be applied. In this way, we make sure that it is not necessary to modify the code every time the data needs to be modified. Therefore, in the last steps, the constants file will be implemented, and the assets folder will be implemented, which contains the data to be read and written.