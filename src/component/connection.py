class Connection:
    COMP = 0
    TYPE = 1
    EXTRA = 2

    def __init__(self, layoutWidget):
        self.transmitSignal = {}   # Contains all the components that will receive
        self.receiveType = {} # Contain callbacks to the 
        self.parent = layoutWidget

    def appendSignalType(self, name):
        self.transmitSignal[name] = {}

    def appendSignal(self, signal, component):
        self.transmitSignal[signal][component.objectName()] = component.getConnection()

    def appendReceiverType(self, name, callback):
        self.receiveType[name] = callback

    def checkDeletion(self, objectName):
        """
        This method is called whenever there is a component
        that is deleted from the layout. 
        It checks to see whether this component is connected
        to the deleted component, if so, it is removed.

        :param objectName: name of the component
        :return: none
        """
        for i in self.transmitSignal:
            if (objectName in self.transmitSignal[i]):
                self.transmitSignal[i].pop(objectName)

    def emitSignal(self, name):
        for i in self.transmitSignal[name]:
            comp = i[0]
            type = i[1]
            extra = i[2]

            comp.received(type, extra)

    def received(self, signal, extra):
        callback = self.receivers[signal]
        callback(extra)

    def getSignalTypes(self) -> list:
        types = []
        for i in self.transmitSignal:
            types.append(i)
        return types

    def getRecvTypes(self) -> list:
        types = []
        for i in self.receiveType:
            types.append(i)
        return types
