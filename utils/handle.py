from utils import *

import datetime

import pandas as pd
import os


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
        return eval(param)