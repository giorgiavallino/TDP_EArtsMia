from database.DB_connect import DBConnect
from model.arco import Arco
from model.artObject import ArtObject

class DAO():

    def __ini__(self):
        pass

    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """SELECT *
        FROM objects"""
        cursor.execute(query,)
        for row in cursor:
            result.append(ArtObject(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(u, v):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """SELECT eo1.object_id, eo2.object_id, COUNT(*) AS peso
        FROM exhibition_objects eo1, exhibition_objects eo2 
        WHERE eo1.exhibition_id = eo2.exhibition_id AND eo1.object_id < eo2.object_id 
        AND eo1.object_id = %s and eo2.object_id = %s
        GROUP BY eo1.object_id, eo2.object_id """
        cursor.execute(query, (u.object_id, v.object_id))
        for row in cursor:
            result.append(row["peso"])
        cursor.close()
        conn.close()
        if len(result) == 0:
            return None
        return result

    @staticmethod
    def getAllEdges(idMap):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """SELECT eo1.object_id AS o1, eo2.object_id AS o2, COUNT(*) AS peso
                FROM exhibition_objects eo1, exhibition_objects eo2 
                WHERE eo1.exhibition_id = eo2.exhibition_id AND eo1.object_id < eo2.object_id
                GROUP BY eo1.object_id, eo2.object_id """
        cursor.execute(query,)
        for row in cursor:
            result.append(Arco(idMap[row["o1"]], idMap[row["o2"]], row["peso"]))
        cursor.close()
        conn.close()
        return result