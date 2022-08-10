
class Connection:
    COMP = 0
    TYPE = 1
    EXTRA = 2

    HELLO_PKT = -1

    def __init__(self, comp):
        self.A2Bconnection = {} # Contains the type of the connection and the list of components assigned
        self.A2Bcallback = {} # Contains callback when the appended connection type is received

        self.B2Aconnection = {} # Contains components (A2B) that are connected to this component
        self.selfComponent = comp

    def appendConnType(self, name):
        self.A2Bconnection[name] = {}

    def appendConn(self, signal, component):
        # 
        self.A2Bconnection[signal][component] = component.getConnection()

        component.getConnection().received(self.HELLO_PKT, [self.selfComponent, self, signal])

    def clearConn(self):
        for i in self.A2Bconnection:
            self.A2Bconnection[i] = {}
        self.B2Aconnection.clear()
            
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
        for i in self.A2Bconnection:
            if (component in self.A2Bconnection[i]):
                self.A2Bconnection[i].pop(component)

    def emitSignal(self, name):
        list = self.A2Bconnection[name]
        for i in list:
            list[i].received(name, None)

    def setConnList(self, list):
        self.clearConn()
        print(list)
        for i in list[0]:
            self.appendConn(i[1], i[0])
        for i in list[1]:
            self.B2Aconnection[i[1]] = (i[1].getConnection(), i[0])
        

    def received(self, signal, extra):
        if (signal == self.HELLO_PKT):
            object = extra[0]
            conn = extra[1]
            type = extra[2]

            self.B2Aconnection[object] = (conn, type)
        else:  
            callback = self.A2Bcallback[signal]
            callback()

    def getData(self) -> list: # Should change this and make it reference not sending back all the data
        transSig = []
        for i in self.A2Bconnection:
            for j in self.A2Bconnection[i]:
                transSig.append((i, j))

        recvSig = []
        for i in self.B2Aconnection:
            recvSig.append((self.B2Aconnection[i][1], i))

        return (transSig, recvSig)

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
