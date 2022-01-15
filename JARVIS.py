import datetime

import json
import time
import sys

CONFIGURATIONS = json.load(open('./data/config.json'))

# import pandas

from utils import daytime
from utils.handle import handleCommand

def greet(name:str) -> None:
    """
    Greeting Logic Based on current time as Good Morning, Good Afternoon and Good Evening
    """
    hour = int(datetime.datetime.now().strftime("%H"))
    partOfDay = daytime.whichPartOfDay(hour=hour)
    if partOfDay == "morning":
        return f"Hello {name}! Good Morning. How're you? All good. Tell me how I may help you. "
    elif partOfDay == "afternoon":
        return f"Good Afternoon {name}! How's the day going? May I help you"
    else:
        return f"Good Evening! How may I help at the end of the day?"

def acceptCommand() -> str:
    cmd = input("-> ")
    return cmd


if __name__ == "__main__":
    greeting = greet("Divyanshu")
    print(greeting)

    while True:
        cmd = acceptCommand()
        if len(cmd.split(" ")) == 1:
            cmd,param = cmd.split(" ") + [None]
        else:
            cmd, param = cmd.split(" ")
        response = handleCommand(cmd, param)
        print(response)

        if response[0:3] == "Bye":
            time.sleep(.5)
            sys.exit()