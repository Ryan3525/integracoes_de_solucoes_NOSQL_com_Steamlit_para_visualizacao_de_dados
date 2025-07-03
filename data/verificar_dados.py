from pymongo import MongoClient

# Conexão com o MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["eshop"]
colecao = db["clientes"]

# Contar documentos
total = colecao.count_documents({})
print(f"Total de clientes cadastrados: {total}")