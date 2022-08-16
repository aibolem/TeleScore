from copy import copy

class Connection:
    COMP = 0
    TYPE = 1
    EXTRA = 2

    HELLO_PKT = -1
    BYEA2B_PKT = -2
    BYEB2A_PKT = -3

    """
    A2Bconnection dictionary format:
        { 
            TypeName1: [component1, component2],
            TypeName2: [component3, component4]
        }

    A2Bcallback dictionary format:
        {
            TypeName1: callbackFunc
        }
    
    B2Aconnection dictionary format:
        {
            component1: TypeName
        }
    """

    def __init__(self, comp):
        self.A2Bconnection = {} # Contains the type of the connection and the list of components assigned
        self.A2Bcallback = {} # Contains callback when the appended connection type is received

        self.B2Aconnection = [] # Contains components (A2B) that are connected to this component
        self.selfComponent = comp

    def appendConnType(self, typeName):
        self.A2Bconnection[typeName] = []

    def appendConn(self, typeName, component):
        """
        
        """
        if (component not in self.A2Bconnection[typeName]):
            self.A2Bconnection[typeName].append(component)
            component.getConnection().received(self.HELLO_PKT, (self.selfComponent, typeName))

    def removeConn(self, typeName, component):
        self.A2Bconnection[typeName].remove(component)
        component.getConnection().received(self.BYEA2B_PKT, (self.selfComponent, typeName))

    def removeB2AConn(self, typeName, component):
        component.getConnection().received(self.BYEB2A_PKT, (self.selfComponent, typeName))
        self.B2Aconnection.remove((component, typeName))
            
    def appendCallBack(self, name, callback):
        self.A2Bcallback[name] = callback

    def checkDeletion(self, component):
        """
        This method is called whenever there is a component
        that is deleted from the layout. 
        It checks to see whether this component is connected
        to the deleted component, if so, it is removed.

        :param objectName: name of the component
        :return: none
        """
        # Check for outgoing connection
        for i in self.A2Bconnection:
            if (component in self.A2Bconnection[i]):
                self.A2Bconnection[i].remove(component)

        # Check for incoming connection
        for i in self.B2Aconnection:
            if (component in i):
                self.B2Aconnection.remove(i)

    def emitSignal(self, typeName, extra=None):
        list = self.A2Bconnection[typeName]
        for i in list:
            i.getConnection().received(typeName, extra)
        
    def received(self, typeName, extra):
        """
        This is called when a transmitting component emits a signal

        :param:
        """
        match typeName:
            case self.HELLO_PKT:
                self.B2Aconnection.append((extra[0], extra[1]))
            case self.BYEA2B_PKT:
                self.B2Aconnection.remove((extra[0], extra[1]))
            case self.BYEB2A_PKT:
                self.A2Bconnection[extra[1]].remove(extra[0])
            case _:
                if (extra != None):
                    self.A2Bcallback[typeName](extra)
                else:
                    self.A2Bcallback[typeName]()

    def getData(self) -> tuple:
        """
        
        """
        self.aA2Bconnection = {}
        for type in self.A2Bconnection:
            self.aA2Bconnection[type] = copy(self.A2Bconnection[type])
        self.aB2Aconnection = copy(self.B2Aconnection)
        return (self.aA2Bconnection, self.aB2Aconnection)

    def dataChanged(self):
        for type in self.A2Bconnection:    # Usually going to be n=1
            for component in self.A2Bconnection[type]:
                if (component not in self.aA2Bconnection[type]):
                    self.removeConn(type, component)

        # Add the new connections
        for type in self.A2Bconnection:
            for component in self.aA2Bconnection[type]:
                self.appendConn(type, component)

        for tuple in self.B2Aconnection:
            if (tuple not in self.aB2Aconnection):
                self.removeB2AConn(tuple[1], tuple[0])
        

    def getSignalTypes(self) -> list:
        types = []
        for i in self.A2Bconnection:
            types.append(i)
        return types

    def getRecvTypes(self) -> list:
        types = []
        for i in self.A2Bcallback:
            types.append(i)
        return types
