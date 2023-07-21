import mysql.connector as mc

conexao = mc.connect(
    host="localhost",
    user="thiago",
    password="123",
    database="nfse"
)
try:
    if conexao.is_connected():
        print("Conexão com o banco estabelecida!")
except mc.Error as e:
    print(f"Erro ao conectar ao banco de dados {e}")

