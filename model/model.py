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

    def getInfoConnessa(self, idInput):
        source = self._idMap[idInput]
        # Modo 1: contare i successori
        succ = nx.dfs_successors(self._graph, source).values()
        result = []
        for s in succ:
            result.extend(s)
        print(f"Size connessa con modo 1: {len(result)}") # --> non contiene il nodo source
        # Modo 2: contare i predecessori
        pred = nx.dfs_predecessors(self._graph, source)
        print(f"Size connessa con modo 2: {len(pred.values())}") # --> non contiene il nodo source
        # Modo 3: contare i nodi dell'albero di visita
        dfsTree = nx.dfs_tree(self._graph, source)
        print(f"Size connessa con modo 3: {len(dfsTree.nodes())-1}") # --> contiene il nodo source
        # Modo 4: utilizza il metodo nodes_connected_components di networkx
        connComp = nx.node_connected_component(self._graph, source)
        print(f"Size connessa con modo 4: {len(connComp)}")
        return len(connComp)

    def hasNode(self, idInput):
        return idInput in self._idMap # se l'id fa parte della mappa, allora fa parte anche dei nodi del grafo
        # (da cui deriva la creazione della mappa)

    def getObjectFromId(self, id):
        return self._idMap[id]
