from config.db import criar_conexao

def insert_sessao(filme_id: int, sala_id: int, data_sessao: str, horario: str):
    # """Cria uma nova sessão de filme"""
    try:
        con = criar_conexao()
        cursor = con.cursor()
        sql = "INSERT INTO sessoes(filmes_id, sala_id, data_sessao, horario) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (filme_id, sala_id, data_sessao, horario))
        con.commit()
        print("✅ Sessão criada com sucesso!")
        return True  
    except Exception as e:
        print(f"❌ Erro ao criar sessão: {e}")
        return False
    finally:
        cursor.close()
        con.close()

def listar_sessoes_disponiveis():
    # """Lista todas as sessões com informações de filme e sala"""
    try:
        con = criar_conexao()
        cursor = con.cursor()
        sql = """
            SELECT s.id, f.titulo, sa.numero, s.data_sessao, s.horario, sa.capacidade
            FROM sessoes s
            JOIN filmes f ON s.filmes_id = f.id
            JOIN salas sa ON s.sala_id = sa.id
            WHERE s.data_sessao >= CURRENT_DATE
            ORDER BY s.data_sessao, s.horario
        """
        cursor.execute(sql)
        sessoes = cursor.fetchall()
        return sessoes
    except Exception as e:
        print(f"❌ Erro ao listar sessões: {e}")
        return [] # retorna uma lista vazia se der erro
    finally:
        cursor.close()
        con.close()