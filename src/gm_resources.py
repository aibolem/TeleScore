"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

import os
import sys
from PyQt6.QtWidgets import QMessageBox
import requests
import webbrowser

f = {}

class GMessageBox():
    """A class defining the types of message boxes we'll be using. I'm dumb and don't know how else to do this, but it didn't look like QMessageBox included the things I was expecting it to lmao"""
    def __init__(self, title, message, type):
        self.title = title
        self.message = message
        self.type = type
        self.popUp = QMessageBox()
        self.popUp.setWindowTitle(title)
        self.popUp.setText(message)
        if "Ask" in type:
            self.popUp.setIcon(QMessageBox.Icon.Question)
            if type == "AskYesNo":
                self.popUp.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            elif type == "AskYesAllNo":
                self.popUp.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.YesToAll | QMessageBox.StandardButton.No)
            else:
                raise Exception("Unknown MessageBox type. Currently available types are AskYesNo, AskYesAllNo, and Info")
        elif type == "Info":
            self.popUp.setIcon(QMessageBox.Icon.Information)
            self.popUp.setStandardButtons(QMessageBox.StandardButton.Ok)
        else:
            raise Exception("Unknown MessageBox type. Currently available types are AskYesNo, AskYesAllNo, and Info")
    def exec(self):
        return self.popUp.exec()

def externalLink(link):
    """ Shows confirmation dialog before opening a link in the default or most recently used browser """
    asklink = GMessageBox("Open link","GameMaster is opening \n\"%s\" \nin your default browser.\n\nDo you want to continue?" % link,"AskYesNo")
    if asklink.exec() == QMessageBox.StandardButton.Yes:
        webbrowser.open(link)
    else:
        None

def resourcePath(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def retrieveFile(url, name):
    if not "http" in url:
        fileWarning = GMessageBox(title='Invalid URL',message='URL must start with "http"', type="Info")
        fileWarning.exec()
        pass
    else:
        file = requests.get(url)
        print(file)
        f[name] = ""
        for line in file:
            f[name] += line.decode("UTF-8")
        return f[name]

def downloadFile(url, name):
    if not "http" in url:
        fileWarning = GMessageBox(title='Invalid URL',message='URL must start with "http"', type="Info")
        fileWarning.exec()
    else:
        file = requests.get(url)
        with open(name, "w") as f:
            f.write(file.text)
            f.close()
        return(file.text)
    