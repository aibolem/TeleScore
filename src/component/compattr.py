
class CompAttr:
    TABNAME = "TABNAME"
    COMPONENT = "COMPONENT"
    ICON = "ICON"
    HELP = "HELP"
    NAME = "NAME"
    COLOR = "COLOR"
    TYPE = "TYPE"
    VALUE = "VALUE"
    TEXTEDIT = "TEXTEDIT"
    FONTEDIT = "FONTEDIT"
    NUMEDIT = "NUMEDIT"
    TABNAME = "TABNAME"
    PROPERTY = "PROPERTY"
    PROPERTIES = "PROPERTIES"

    defaultProp = {
        "Make a burger": {
            PROPERTIES: {
                "Bun": {
                    TYPE: TEXTEDIT,
                    VALUE: "Delicious"
                },
                "Cheese": {
                    TYPE: NUMEDIT,
                    VALUE: "Marvelous"
                },
                "Meat": {
                    TYPE: NUMEDIT,
                    VALUE: "Extraordinary"
                }
            }
        }
    }

    genProperty = {
        "Component Name": {
            TYPE: TEXTEDIT,
            VALUE: ""
        },
        "X": {
            TYPE: NUMEDIT,
            VALUE: ""
        },
        "Y": {
            TYPE: NUMEDIT,
            VALUE: ""
        },
        "Width": {
            TYPE: NUMEDIT,
            VALUE: "53"
        },
        "Height": {
            TYPE: NUMEDIT,
            VALUE: "21"
        }
    }

    appearProperty = {
        "Display Text": {
            TYPE: TEXTEDIT,
            VALUE: ""
        },
        "Display Font": {
            TYPE: FONTEDIT,
            VALUE: ""
        },
        "Font Size": {
            TYPE: NUMEDIT,
            VALUE: ""
        }
    }

    defaultButtonProp = {
        "General Properties": {
            PROPERTIES: None
        },
        "Appearance Properties": {
            PROPERTIES: None
        }
    }

    #---------------------------------

    timeComponent = {
        "Time Display": {
            ICON: "src/resources/tdisp.png",
            TYPE: "Display",
            HELP: ""
        },
        "Start Time": {
            ICON: "src/resources/startButton.png",
            NAME: "Start",
            COLOR: "#439a86",
            TYPE: "BUTTON",
            HELP: ""
        },
        "Stop Time": {
            ICON: "src/resources/stopButton.png",
            NAME: "Stop",
            COLOR: "#e15554",
            TYPE: "BUTTON",
            HELP: ""
        },
        "Reset": {
            ICON: "src/resources/rstButton.png",
            NAME: "Reset",
            COLOR: "#4357ad",
            TYPE: "BUTTON",
            HELP: ""
        },
        "Add Seconds": {
            ICON: "src/resources/addSec.png",
            NAME: "Add [+]\nSeconds",
            COLOR: "#242325",
            TYPE: "BUTTON",
            HELP: ""
        },
        "Subtract Seconds": {
            ICON: "src/resources/subSec.png",
            NAME: "Subtract [+]\nSeconds",
            COLOR: "#242325",
            TYPE: "BUTTON",
            HELP: ""
        },
        "Add Minutes": {
            ICON: "src/resources/addMin.png",
            NAME: "Add [-]\nMinutes",
            COLOR: "#242325",
            TYPE: "BUTTON",
            HELP: ""
        },
        "Subtract Minutes": {
            ICON: "src/resources/subMin.png",
            NAME: "Subtract [-]\nMinutes",
            COLOR: "#242325",
            TYPE: "BUTTON",
            HELP: ""
        },
        "Type Time Amount": {
            ICON: "src/resources/setTime.png",
            NAME: "",
            TYPE: "BUTTON",
            HELP: ""
        }
    }

    scoreComponent = {
        "Add Points / Stats Amount": {
            ICON: "src/resources/addButton.png",
            TYPE: "DISPLAY",
            HELP: ""
        }
    }

    category = [
            {
                TABNAME: "Time Based Buttons",
                COMPONENT: timeComponent
            },
            {
                TABNAME: "Points and Stats",
                COMPONENT: scoreComponent
            }
        ]