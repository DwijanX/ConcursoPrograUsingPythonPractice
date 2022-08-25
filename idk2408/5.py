import sys
from xml.sax.xmlreader import InputSource

class node:
    def __init__(self,val):
        self.Value=val
        self.Aristas=set()
        pass
    def addAnEdge(self,destino):
        self.Aristas.add(destino)
    def deleteAnEdge(self,destino):
        self.Aristas.remove(destino)
    def getEdges(self):
        return self.Aristas

def addNode(value,graph):
    graph[value]=node(val=value)
def addEdgeToGraph(Val1,Val2,graph):
    graph[Val1].addAnEdge(Val2)
    graph[Val2].addAnEdge(Val1)
def deleteEdge(Val1,Val2,graph):
    graph[Val1].deleteAnEdge(Val2)
    graph[Val2].deleteAnEdge(Val1)

def findConnections(initNode,graph,connectedNodes:set,CitiesNodes:set,lowLimPowerSupply):

    for i in graph[initNode].getEdges():
        if i not in connectedNodes:
            connectedNodes.add(i)
            if i <lowLimPowerSupply:
                CitiesNodes.add(i)
            findConnections(i,graph,connectedNodes,CitiesNodes,lowLimPowerSupply)
        

def GetNodesConnectedToPowerPlant(graph,lowLimPowerSupply,TopLimPowerSupply):
    MaxCities=lowLimPowerSupply-1
    CitiesNodes=set()
    connectedNodes=set()
    for i in range(lowLimPowerSupply,TopLimPowerSupply+1):
        findConnections(i,graph,connectedNodes,CitiesNodes,lowLimPowerSupply)
        if len(CitiesNodes)==MaxCities:
            break
    return len(CitiesNodes)
            


def main():
    graph={}
    N,M,E=map(int,sys.stdin.readline().split(" "))
    Connections=[list(map(int, input().split())) for _ in range(E)] 
    Q=int(sys.stdin.readline())
    Eventos=[int(sys.stdin.readline()) for _ in range(Q)]
    for i in range(1,N+M+1):
        addNode(i,graph)
    for i in Connections:
        addEdgeToGraph(i[0],i[1],graph)

    for i in Eventos:
        deleteEdge(Connections[i-1][0],Connections[i-1][1],graph)
        print(GetNodesConnectedToPowerPlant(graph,N+1,N+M))


main()
