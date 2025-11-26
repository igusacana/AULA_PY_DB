import psycopg2

def criar_conexao():
    try:
        conn = psycopg2.connect(
            dbname = 'auladb',
            user = 'postgres',
            password = 'igoralves25',
            host = 'localhost',
            port = '5432'
        )
        # print("conexão foi um sucesso!!")
        return conn
    except Exception as e:
        print(f"Erro de conexão: {e}")