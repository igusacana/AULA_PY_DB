from config.db import criar_conexao
from funcoes_uteis import hash_senha

def insert_user(email: str, password: str):
    password_hash = hash_senha(password)

    try:
        con = criar_conexao() #cria uma "ponte" para conexão com BD
        cursor = con.cursor() # é o "veiculo" que leva e traz informações do BD
        sql = "INSERT INTO usuarios(email , password) VALUES (%s , %s)"
        cursor.execute(sql, (email, password_hash)) #executa os comandos no BD
        con.commit() #envia a conexão para o BANCO (BD) // só deve ser usado quando houver modificações no BD (INSERT, DELETE e etc)
        print("Usuário cadastrado com sucesso!")

    except Exception as e:
        print(f"conection error {e}") 
    finally:
        #close
        cursor.close() # fecha o cursor (conexão direta pro BD)
        con.close() #evita criar conexões indejesadas no BD


def login(email: str, password: str): ## VERIFICAR SE CLIENTE JÁ POSSUI CADASTRO
    try:
        con = criar_conexao()
        cursor = con.cursor()
        sql = "SELECT * FROM usuarios WHERE email=%s and password=%s"
        cursor.execute(sql, (email, password))
        user = cursor.fetchone()
        return user
    except Exception as e:
        print(f"erro no login {e}")
    finally:
        cursor.close()
        con.close()


