
class CompAttr:
    TABNAME = "TABNAME"
    COMPONENT = "COMPONENT"
    ICON = "ICON"
    NAME = "NAME"
    COLOR = "COLOR"
    PROPERTY = ""

    defaultButtonProp = [
            {
                "TABNAME": "General Properties",
                "PROPERTIES": [
                    ["Component Name:", "TEXTEDIT"],
                    ["Width:", "TEXTEDIT"],
                    ["Height:", "TEXTEDIT"]
                ]
            },
            {
                "TABNAME": "Button Properties",
                "PROPERTIES": [
                    ["Text Info:", "TEXTEDIT"],
                    ["Text Font:", "TEXTEDIT"]
                ]
            }
        ]

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
        "Reset": {
            "ICON": "src/resources/rstButton.png",
            NAME: "Reset",
            COLOR: "#4357ad",
            "HELP": ""
        },
        "Add Seconds": {
            "ICON": "src/resources/addSec.png",
            NAME: "Add [+]\nSeconds",
            COLOR: "#242325",
            "HELP": ""
        },
        "Subtract Seconds": {
            "ICON": "src/resources/subSec.png",
            NAME: "Subtract [+]\nSeconds",
            COLOR: "#242325",
            "HELP": ""
        },
        "Add Minutes": {
            "ICON": "src/resources/addMin.png",
            NAME: "Add [-]\nMinutes",
            COLOR: "#242325",
            "HELP": ""
        },
        "Subtract Minutes": {
            "ICON": "src/resources/subMin.png",
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
            }
        ]