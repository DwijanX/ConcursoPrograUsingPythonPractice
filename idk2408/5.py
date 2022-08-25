

from asyncio.windows_events import NULL
from configparser import InterpolationMissingOptionError
from contextlib import nullcontext
from mimetypes import init


class node:
    def __init__(self,val):
        self.Value=val
        self.Aristas=[]
        pass
    def addAnEdge(self,destino):
        self.Aristas.append(destino)
    def getEdges(self):
        return self.Aristas


def addNode(value,graph):
    graph[value]=node(val=value)
def addEdgeToGraph(Val1,Val2,graph):
    graph[Val1].addAnEdge(Val2)
    graph[Val2].addAnEdge(Val1)

def findConnections(initNode,graph,connectedNodes:set):
    for i in graph[initNode].getEdges():
        if i not in connectedNodes:
            connectedNodes.add(i)
            findConnections(i,graph,connectedNodes)
        

def GetNodesConnectedToPowerPlant(graph):
    connectedNodes=set()

def main():
    graph={}
    addNode(3,graph)
    addNode(4,graph)
    addNode(5,graph)
    addNode(6,graph)
    addEdgeToGraph(3,4,graph)
    addEdgeToGraph(4,5,graph)
    connectedNodes=set()
    findConnections(3,graph,connectedNodes)
    print(connectedNodes)
    
main()