import os #operation system
import bcrypt


def limpar_terminal():
    """Limpa o terminal independente do sistema operacional"""
    os.system('cls' if os.name == 'nt' else 'clear')

    ## os.name == nt = verifica se o sistema é windows

def hash_senha(senha: str):
    hashed = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    return hashed.decode('utf-8')

# Exemplo de uso:
# senha_hash = hash_senha("minhasenha123")
# print(senha_hash) # Ex: $2b$12$