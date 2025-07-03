import streamlit as st
from db import get_db
from bson.objectid import ObjectId
colecao = get_db()

st.title("Cadastro de Clientes - E-Shop Brasil")

menu = st.sidebar.selectbox("Menu", ["Listar", "Cadastrar", "Atualizar", "Excluir"])

if menu == "Listar":
    st.subheader("Lista de Clientes")
    clientes = list(colecao.find().limit(100))
    for c in clientes:
        st.write(f"**Nome:** {c['nome']}")
        st.write(f"**Email:** {c['email']}")
        st.write(f"**Telefone:** {c['telefone']}")
        st.write("---")

elif menu == "Cadastrar":
    st.subheader("Novo Cliente")
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    telefone = st.text_input("Telefone")
    endereco = st.text_area("Endereço")
    cpf = st.text_input("CPF")

    if st.button("Salvar"):
        novo_cliente = {
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "endereco": endereco,
            "cpf": cpf
        }
        colecao.insert_one(novo_cliente)
        st.success("Cliente cadastrado com sucesso!")

elif menu == "Atualizar":
    st.subheader("Atualizar Cliente")

    clientes = list(colecao.find().limit(100))
    nomes = [f"{c['nome']} ({c['_id']})" for c in clientes]
    escolhido = st.selectbox("Escolha um cliente", nomes)

    if escolhido:
        cliente_id = escolhido.split("(")[-1][:-1]  # extrai o ID
        cliente = colecao.find_one({"_id": ObjectId(cliente_id)})

        nome = st.text_input("Nome", cliente["nome"])
        email = st.text_input("Email", cliente["email"])
        telefone = st.text_input("Telefone", cliente["telefone"])
        endereco = st.text_area("Endereço", cliente["endereco"])
        cpf = st.text_input("CPF", cliente["cpf"])

        if st.button("Atualizar"):
            colecao.update_one(
                {"_id": ObjectId(cliente_id)},
                {"$set": {
                    "nome": nome,
                    "email": email,
                    "telefone": telefone,
                    "endereco": endereco,
                    "cpf": cpf
                }}
            )
            st.success("Cliente atualizado com sucesso!")

elif menu == "Excluir":
    st.subheader("Excluir Cliente")

    clientes = list(colecao.find().limit(100))
    nomes = [f"{c['nome']} ({c['_id']})" for c in clientes]
    escolhido = st.selectbox("Escolha um cliente para excluir", nomes)

    if escolhido:
        cliente_id = escolhido.split("(")[-1][:-1]
        if st.button("Excluir"):
            colecao.delete_one({"_id": ObjectId(cliente_id)})
            st.success("Cliente excluído com sucesso!")