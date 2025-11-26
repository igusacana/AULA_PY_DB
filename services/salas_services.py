from config.db import criar_conexao

def insert_salas(numero_sala: int, capacidade: int):
    try:
        con = criar_conexao()
        cursor = con.cursor()
        sql = "INSERT INTO salas(numero, capacidade) VALUES (%s, %s)"
        cursor.execute(sql, (numero_sala, capacidade))
        con.commit()
        print("SALA cadastrado com sucesso!\n")

    except Exception as e:
        print(f"erro ao cadastrar SALA {e}")
    finally:
        cursor.close()
        con.close()

def listar_salas():
    """Lista todas as salas cadastradas"""
    try:
        con = criar_conexao()
        cursor = con.cursor()
        sql = "SELECT * FROM salas ORDER BY numero"
        cursor.execute(sql)
        salas = cursor.fetchall()
        return salas
    except Exception as e:
        print(f"❌ Erro ao listar salas: {e}")
    finally:
        cursor.close()
        con.close()