from faker import Faker
from pymongo import MongoClient
from tqdm import tqdm

# Conectar ao MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["eshop"]
colecao = db["clientes"]

# Gerador de dados falsos
fake = Faker('pt_BR')

# Limpar dados antigos (opcional)
colecao.delete_many({})

# Gerar 1 milhão de registros (cuidado: leva tempo)
TOTAL = 1000

for _ in tqdm(range(TOTAL)):
    cliente = {
        "nome": fake.name(),
        "email": fake.email(),
        "telefone": fake.phone_number(),
        "endereco": fake.address(),
        "cpf": fake.cpf()
    }
    colecao.insert_one(cliente)

print("Inserção concluída.")