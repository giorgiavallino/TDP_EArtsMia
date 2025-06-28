from model import model

myModel = model.Model()
myModel.buildGraph()
print(f"Numero nodi: {myModel.getNumNodes()}")
print(f"Numero archi: {myModel.getNumEdges()}")