class CompAttr:
    TABNAME = "TABNAME"
    COMPONENT = "COMPONENT"
    ICON = "ICON"
    HELP = "HELP"
    NAME = "NAME"
    COLOR = "COLOR"
    TYPE = "TYPE"
    SIGNAL = "SIGNAL"
    VALUE = "VALUE"
    TEXTEDIT = "TEXTEDIT"
    FONTEDIT = "FONTEDIT"
    NUMEDIT = "NUMEDIT"
    CONNEDIT = "CONNEDIT"
    CHECKBOX = "CHECKBOX"
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
            VALUE: 1
        },
        "Y": {
            TYPE: NUMEDIT,
            VALUE: 1
        },
        "Width": {
            TYPE: NUMEDIT,
            VALUE: 0
        },
        "Height": {
            TYPE: NUMEDIT,
            VALUE: 0
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

    connProperty = {
        "Connection": {
            TYPE: CONNEDIT,
            VALUE: []
        }
    }

    fileProperty = {
        "File Output Location": {
            TYPE: TEXTEDIT,
            VALUE: "./Output/{}.txt"
        }
    }

    scoreDispProperty = {
        "Suffix (st, nd, rd, th)": {
            TYPE: CHECKBOX,
            VALUE: 0
        }
    }

    scoreSetProperty = {
        "Set Amount": {
            TYPE: NUMEDIT,
            VALUE: 0
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
            SIGNAL: "Start",
            HELP: ""
        },
        "Stop Time": {
            ICON: "src/resources/stopButton.png",
            NAME: "Stop",
            COLOR: "#e15554",
            TYPE: "BUTTON",
            SIGNAL: "Stop",
            HELP: ""
        },
        "Reset": {
            ICON: "src/resources/rstButton.png",
            NAME: "Reset",
            COLOR: "#4357ad",
            TYPE: "BUTTON",
            SIGNAL: "Reset",
            HELP: ""
        },
        "Add Seconds": {
            ICON: "src/resources/addSec.png",
            NAME: "Add [+]\nSeconds",
            COLOR: "#242325",
            TYPE: "BUTTON",
            SIGNAL: "ADDS",
            HELP: ""
        },
        "Subtract Seconds": {
            ICON: "src/resources/subSec.png",
            NAME: "Subtract [+]\nSeconds",
            COLOR: "#242325",
            TYPE: "BUTTON",
            SIGNAL: "SUBS",
            HELP: ""
        },
        "Add Minutes": {
            ICON: "src/resources/addMin.png",
            NAME: "Add [-]\nMinutes",
            COLOR: "#242325",
            TYPE: "BUTTON",
            SIGNAL: "ADDM",
            HELP: ""
        },
        "Subtract Minutes": {
            ICON: "src/resources/subMin.png",
            NAME: "Subtract [-]\nMinutes",
            COLOR: "#242325",
            TYPE: "BUTTON",
            SIGNAL: "SUBM",
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
        "Score Display": {
            ICON: "src/resources/scoreDisplay.png",
            NAME: "Score Display",
            TYPE: "DISPLAY"
        },
        "Add Points": {
            ICON: "src/resources/addPtButton.png",
            NAME: "Add Points",
            TYPE: "CUST_BUTTON",
            HELP: ""
        },
        "Sub Points": {
            ICON: "src/resources/subPtButton.png",
            NAME: "Sub Points",
            TYPE: "CUST_BUTTON",
            HELP: ""
        }, 
        "Score Set": {
            ICON: "src/resources/scoreSet.png",
            NAME: "Score Set",
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

    @classmethod
    def getAllCategory(self):
        # terrible code replace this in memory
        largeDict = {}
        for i in self.category:
            dict = i[self.COMPONENT]
            largeDict.update(dict)
        return largeDict