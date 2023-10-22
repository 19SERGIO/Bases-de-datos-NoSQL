import pymongo
conexion = pymongo.MongoClient("mongodb://localhost:27017")
bd = conexion["Sena"]
instructores = bd["instructores"]
nuevos =[
    {"nombre":"David", "area":"Programacion", "regional":"Antioquia"},
    {"nombre":"Kevin Atehortua", "area":"Analisis", "regional":"Caldas"}
    # se puede poner los que unos desea
]
instructores.insert_many(nuevos)