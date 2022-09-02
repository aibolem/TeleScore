class CompAttr:
    TABNAME = "TABNAME"
    COMPONENT = "COMPONENT"
    ICON = "ICON"
    HELP = "HELP"
    TEXT = "TEXT"
    COLOR = "COLOR"
    TYPE = "TYPE"
    SIGNAL = "SIGNAL"
    VALUE = "VALUE"
    TEXTEDIT = "TEXTEDIT"
    FONTEDIT = "FONTEDIT"
    NUMEDIT = "NUMEDIT"
    CONNEDIT = "CONNEDIT"
    CHECKBOX = "CHECKBOX"
    FILESCT = "FILESCT"
    TABNAME = "TABNAME"
    PROPERTY = "PROPERTY"
    PROPERTIES = "PROPERTIES"
    HEADER = "HEADER"

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
            TYPE: FILESCT,
            VALUE: "./Output/{}.{}"
        }
    }

    #---------------------------------
    """
    Component dictionary will have a format:
    {
        Component Type Name: {
            ICON: (REQUIRED) loc to icon file
            TYPE: (REQUIRED) type of a component -> Currently DISPLAY, BUTTON
            COLOR: (REQUIRED FOR TYPE BUTTON) Color of the button
            SIGNAL: (REQUIRED FOR TYPE BUTTON) Name of the transmit type name
            HELP: (OPTIONAL BUT RECOMM) Helpful tip of the component
            More can be added in the future
        }
    }
    """

    timeComponent = {
        "Time Display": {
            ICON: "src/resources/tdisp.png",
            TYPE: "Display",
            HELP: ""
        },
        "Start Time": {
            ICON: "src/resources/startButton.png",
            TEXT: "Start",
            COLOR: "#439a86",
            TYPE: "BUTTON",
            SIGNAL: "Start",
            HELP: ""
        },
        "Stop Time": {
            ICON: "src/resources/stopButton.png",
            TEXT: "Stop",
            COLOR: "#e15554",
            TYPE: "BUTTON",
            SIGNAL: "Stop",
            HELP: ""
        },
        "Reset": {
            ICON: "src/resources/rstButton.png",
            TEXT: "Reset",
            COLOR: "#4357ad",
            TYPE: "BUTTON",
            SIGNAL: "Reset",
            HELP: ""
        },
        "Add Seconds": {
            ICON: "src/resources/addSec.png",
            TEXT: "Add [+]\nSeconds",
            COLOR: "#242325",
            TYPE: "BUTTON",
            SIGNAL: "ADDS",
            HELP: ""
        },
        "Subtract Seconds": {
            ICON: "src/resources/subSec.png",
            TEXT: "Subtract [-]\nSeconds",
            COLOR: "#242325",
            TYPE: "BUTTON",
            SIGNAL: "SUBS",
            HELP: ""
        },
        "Add Minutes": {
            ICON: "src/resources/addMin.png",
            TEXT: "Add [-]\nMinutes",
            COLOR: "#242325",
            TYPE: "BUTTON",
            SIGNAL: "ADDM",
            HELP: ""
        },
        "Subtract Minutes": {
            ICON: "src/resources/subMin.png",
            TEXT: "Subtract [-]\nMinutes",
            COLOR: "#242325",
            TYPE: "BUTTON",
            SIGNAL: "SUBM",
            HELP: ""
        },
        "Type Time Amount": {
            ICON: "src/resources/setTime.png",
            TEXT: "",
            TYPE: "DISPLAY",
            HELP: ""
        }
    }

    scoreComponent = {
        "Score Display": {
            ICON: "src/resources/scoreDisplay.png",
            TEXT: "Score Display",
            TYPE: "DISPLAY"
        },
        "Add Points": {
            ICON: "src/resources/addPtButton.png",
            TEXT: "Add Points",
            TYPE: "CUST_BUTTON",
            HELP: ""
        },
        "Sub Points": {
            ICON: "src/resources/subPtButton.png",
            TEXT: "Sub Points",
            TYPE: "CUST_BUTTON",
            HELP: ""
        }, 
        "Score Set": {
            ICON: "src/resources/scoreSet.png",
            TEXT: "Score Set",
            TYPE: "DISPLAY",
            HELP: ""
        }
    }

    teamCompoonent = {
        "Team Attribute": {
            ICON: "src/resources/teamComp.png",
            TEXT: "Team Attribute",
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
            },
            {
                TABNAME: "Team Component",
                COMPONENT: teamCompoonent
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

    header = {
        "Width": 1,
        "Height": 1
    }