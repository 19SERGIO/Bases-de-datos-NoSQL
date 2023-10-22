import pymongo
conexion=pymongo.MongoClient("mongo://localhost:21017")
bd = conexion["Sena"]
instructores =bd["instructores"]