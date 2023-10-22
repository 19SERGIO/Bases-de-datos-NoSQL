import pymongo
conexion = pymongo.MongoClient("mongodb://localhost:27017")
bd = conexion["Sena"]
instructores = bd["instructores"]
instructores.insert_one({"nombre": "Wuakypandy", "area":"Programacion","regional":"Tolima"})