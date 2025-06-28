from database.DAO import DAO
from model.model import Model

listObjects = DAO.getAllNodes()
print(len(listObjects))

myModel = Model()
edges = DAO.getAllEdges(myModel.getIdMap())
print(len(edges))