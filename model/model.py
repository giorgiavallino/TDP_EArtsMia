import networkx as nx
from database.DAO import DAO

class Model:

    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = DAO.getAllNodes()
        self._idMap = {}
        for node in self._nodes:
            self._idMap[node.object_id] = node

    def buildGraph(self):
        self._graph.add_nodes_from(self._nodes)
        self.addEdges_02()

    def addEdges_01(self):
        for u in self._nodes:
            for v in self._nodes:
                peso = DAO.getPeso(u, v)
                if peso != None:
                    self._graph.add_edge(u, v, weight=peso)
    # Questo metodo è funzionante, però impiega molto tempo

    def addEdges_02(self):
        allEdges = DAO.getAllEdges(self._idMap)
        for edge in allEdges:
            self._graph.add_edge(edge.o1, edge.o2, weight=edge.peso)

    def getNumNodes(self):
        return len(self._graph.nodes)

    def getNumEdges(self):
        return len(self._graph.edges)

    def getIdMap(self):
        return self._idMap
