import os
import sys
from PyQt6.QtWidgets import QMessageBox
from requests import *
import webbrowser

f = {}

def externalLink(self, link):
    """ Shows confirmation dialog before opening a link in the default or most recently used browser """
    asklink = QMessageBox()
    asklink.setWindowTitle("Open link")
    asklink.setText("GameMaster is opening \n\"%s\" \nin your default browser.\n\nDo you want to continue?" % link)
    asklink.setStandardButtons(QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Yes)
    asklink.setIcon(QMessageBox.Icon.Question)
    if asklink.exec() == QMessageBox.StandardButton.Ok:
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
    """Not working. Fix dialogs before use."""
    if not "http" in url:
        qm.ABOUT(title='Invalid URL',message='URL must start with "http"', icon='warning')
    else:
        file = get(url)
        f[name] = ""
        for line in file:
            decoded_line = line.decode("utf-8")
            f[name] += decoded_line
    return f[name]

def downloadFile(url, name):
    """Not working. Fix dialogs before use."""
    if not "http" in url:
        qm.ABOUT(title='Invalid URL',message='URL must start with "http"', icon='warning')
    else:
        file = get(url)
        with open(name, "w") as f:
            f.write(file.text)
            f.close()
        return(file.text)
        
