from json import *
import os, sys

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from attr import CompAttr
from layout.ctrllayout import CtrlLayout
from component.compfactory import CompFactory
from proginterface import ProgInterface

class LayoutFile:
    def __init__(self, fileName: str, layout: CtrlLayout):
        self.fileName = fileName
        self.ctrlLayout = layout

    def save(self):
        components = self.ctrlLayout.getComponents()
        jsonFormattedDict = {CompAttr.HEADER: CompAttr.header}
        for name in components:
            compObj = components[name]
            compType = compObj.getName()
            outProperty = {}
            compProperty = compObj.getSaveProp()
            for i in compProperty:  # Change this in the future so the code isn't O(n*m)
                if (i != "Connection"):
                    outProperty[i] = compProperty[i][CompAttr.VALUE]

            compConnection = compObj.getConnection().getData()[0]
            self.convConnection(compConnection)

            jsonFormattedDict[name] = { 
                                        CompAttr.TYPE: compType,
                                        CompAttr.PROPERTIES: outProperty,
                                        CompAttr.CONNEDIT: compConnection 
                                    }

        with open(self.fileName, 'w') as wstream:
            dump(jsonFormattedDict, wstream)

    def convConnection(self, conn):
        for typeName in conn:
            newList = []
            connCompList = conn[typeName]
            for comp in connCompList:
                name = comp.objectName()
                newList.append(name)
            conn[typeName] = newList

    def load(self, edit=False):
        dataDict = {}
        with open(self.fileName, 'r') as rstream:
            dataDict = load(rstream)
        
        for element in dataDict:
            if (element != CompAttr.HEADER):
                compElement = dataDict[element]
                compProperty = compElement[CompAttr.PROPERTIES]
                component = CompFactory.makeComponent(compElement[CompAttr.TYPE], element, edit, self.ctrlLayout)
                for i in compProperty:
                    component.setOneProp(i, compProperty[i])
                
                self.ctrlLayout.addComponent(component)
                component.propChanged()
                component.insertCalc(self.ctrlLayout.size())

        intf = ProgInterface()

        for component in self.ctrlLayout.getComponents().values():
            conn = component.getConnection()

            componentConn = dataDict[component.objectName()][CompAttr.CONNEDIT]
            for i in componentConn:
                conn.appendConnType(i)
                for j in componentConn[i]:
                    conn.appendConn(i, intf.getComponent(j))
        

        
