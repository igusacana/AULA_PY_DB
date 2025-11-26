from config.db import criar_conexao

def comprar_ingresso(usuario_id: int, sessao_id: int):
    # """Registra a compra de um ingresso"""
    try:
        con = criar_conexao()
        cursor = con.cursor()
        sql = "INSERT INTO ingressos(usuario_id, sessao_id) VALUES (%s, %s)"
        cursor.execute(sql, (usuario_id, sessao_id))
        con.commit()
        print("✅ Ingresso comprado com sucesso!")
        return True
    except Exception as e:
        print(f"❌ Erro ao comprar ingresso: {e}")
        return False
    finally:
        cursor.close()
        con.close()

def listar_ingressos_usuario(usuario_id: int):
    # """Lista todos os ingressos de um usuário"""
    try:
        con = criar_conexao()
        cursor = con.cursor()
        sql = """
            SELECT i.id, f.titulo, sa.numero, s.data_sessao, s.horario, i.data_compra 
            FROM ingressos i
            JOIN sessoes s ON i.sessao_id = s.id
            JOIN filmes f ON sessoes.f_id = f.id
            JOIN salas sa ON sessoes.sa_id = sa.id
            WHERE i.usuario_id = %s
            ORDER BY i.data_compra DESC 
        """                             ### DESC = valores maior para menor

        cursor.execute(sql, (usuario_id,))
        ingressos = cursor.fetchall() # o FETCHALL busca e traz TODAS as informações do Banco
        return ingressos
    except Exception as e:
        return [] #retorna uma lista vazia
    finally:
        cursor.close()
        con.close()