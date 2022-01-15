from utils import *

import datetime

import os
import json

config = json.load(open('data/config.json'))


def handleCommand(cmd: str, param: str) -> None:
    if cmd == "exit":
        return "Bye. Nice talking with you"
    if cmd == "date":
        return f"Today's date is {datetime.datetime.now().strftime('%d-%m-%Y')}"
    if cmd == "day":
        return f"Today is {datetime.datetime.now().strftime('%A')}"
    if cmd == "time":
        return f"The time is {datetime.datetime.now().strftime('%I:%M %p')}"
    if cmd == "calc":
        return str(eval(param))
    if cmd == "profile":
        return str(config) if param == None else str(config[param])
