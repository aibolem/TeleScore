
class CompAttr:
    TABNAME = "TABNAME"
    COMPONENT = "COMPONENT"
    ICON = "ICON"
    NAME = "NAME"
    COLOR = "COLOR"

    timeComponent = {
        "Time Display": {
            "ICON": "src/resources/tdisp.png",
            "HELP": ""
        },
        "Start Time": {
            "ICON": "src/resources/startButton.png",
            NAME: "Start",
            COLOR: "#000000",
            "HELP": ""
        },
        "Stop Time": {
            "ICON": "src/resources/stopButton.png",
            NAME: "Stop",
            COLOR: "#e15554",
            "HELP": ""
        },
        "Reset Time": {
            "ICON": "src/resources/rstButton.png",
            "NAME": "",
            NAME: "Reset",
            COLOR: "#4357ad",
            "HELP": ""
        },
        "Add Seconds": {
            "ICON": "src/resources/addSec.png",
            "NAME": "",
            NAME: "Add [+]\nSeconds",
            COLOR: "#242325",
            "HELP": ""
        },
        "Subtract Seconds": {
            "ICON": "src/resources/subSec.png",
            "NAME": "",
            NAME: "Subtract [+]\nSeconds",
            COLOR: "#242325",
            "HELP": ""
        },
        "Add Minutes": {
            "ICON": "src/resources/addMin.png",
            "NAME": "",
            NAME: "Add [-]\nMinutes",
            COLOR: "#242325",
            "HELP": ""
        },
        "Subtract Minutes": {
            "ICON": "src/resources/subMin.png",
            "NAME": "",
            NAME: "Subtract [-]\nMinutes",
            COLOR: "#242325",
            "HELP": ""
        },
        "Type Time Amount": {
            "ICON": "src/resources/setTime.png",
            "NAME": "",
            
            "HELP": ""
        }
    }

    category = [
            {
                TABNAME: "Time Based Buttons",
                COMPONENT: timeComponent
            },
            {
                TABNAME: "Hello",
                COMPONENT: timeComponent
            }
        ]