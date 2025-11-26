from config.db import criar_conexao


def insert_filmes(title_filme: str, duracao: int, classificacao: str):
    # cadastrando filmes
    try:
        con = criar_conexao()
        cursor = con.cursor()
        sql = "INSERT INTO filmes(titulo, duracao, classificacao) VALUES (%s, %s, %s)"
        cursor.execute(sql, (title_filme, duracao, classificacao))
        con.commit()
        print("filme cadastrado com sucesso!\n")

    except Exception as e:
        print(f"erro ao cadastrar o filme {e}")
    finally:
        cursor.close()
        con.close()

def listar_filmes():
    #Listar os filmes cadastrados
    try:
        con = criar_conexao()
        cursor = con.cursor()
        sql = "SELECT * FROM filmes ORDER BY titulo"
        cursor.execute(sql)
        filmes = cursor.fetchall()
        return filmes
        

    except Exception as e:
        print(f"erro ao listar os filmes {e}")
    finally:
        cursor.close()
        con.close()