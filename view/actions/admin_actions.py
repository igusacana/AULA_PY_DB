from services.filmes_services import listar_filmes, insert_filmes
from services.salas_services import insert_salas, listar_salas
from services.session_services import insert_sessao, listar_sessoes_disponiveis



def cadastrar_filme():
    print("== CADASTRE O FILME ==\n") 
    titulo = input(" Digite o titulo do Filme: ")
    duracao = input(" Digite a duração do Filme (em minutos): ")
    classificacao = input(" Qual a classificação do filme? ('Livre', 'maior', '12', 14, 16, 18):  ")
    insert_filmes(titulo, duracao, classificacao)

def mostrar_filmes():
    filmes = listar_filmes()
    if filmes:
        for filme in filmes:
           print(f"ID: {filme[0]} | {filme[1]} | {filme[2]}min | {filme[3]}")
    else:
        print("Nenhum filme em cartaz!!")

def cadastrar_salas():
    print("== CADASTRAR SALAS ==\n") 
    num_sala = int(input(" Digite o número da sala: "))
    capacidade = int(input(" Qual a capacidade total da sala? "))
    insert_salas(num_sala, capacidade)

def mostrar_salas():
    salas = listar_salas()
    if salas:
        for sala in salas:
            print(f"ID: {sala[0]} | {sala[1]} | {sala[2]} pessoas")
    else:
        print(" Nenhuma sala cadastrada até o momento!! ")

def cadastrar_sessao():
    print("== CADASTRAR SESSÕES ==\n") #(filme_id: int, sala_id: int, data_sessao: str, horario: str):
    mostrar_filmes()
    filme_id = int(input("\nID do Filme: "))
    mostrar_salas()
    sala_id = int(input("\nID da Sala: "))
    data = input("DATA (DD-MM-ANO): ")
    hora = input("Horário (HH:MM): ")
    insert_sessao(filme_id, sala_id, data, hora)

def mostrar_sessoes():
    """Exibe todas as sessões disponíveis"""
    print("\n--- SESSÕES DISPONÍVEIS ---")
    sessoes = listar_sessoes_disponiveis()
    if sessoes:
        for sessao in sessoes:
            print(f"ID: {sessao[0]} | {sessao[1]} | Sala {sessao[2]} | {sessao[3]} às {sessao[4]}") # dados em tuplas
    else:
        print("Nenhuma sessão disponível.")