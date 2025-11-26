from services.session_services import listar_sessoes_disponiveis
from services.ingresso_service import comprar_ingresso, listar_ingressos_usuario

def ver_filmes_cartaz():
    print("== FILMES EM CARTAZ ==\n")
    sessoes = listar_sessoes_disponiveis()
    if sessoes:
        for sessao in sessoes:
            print(f"ID: {sessao[0]} | {sessao[1]} | Sala {sessao[2]} | {sessao[3]} às {sessao[4]}")
    else:
        print("Nenhuma sessão disponível.")

def realizar_compra(usuario_id):
    print("== COMPRAR INGRESSO ==\n")
    ver_filmes_cartaz()
    
    try:
        sessao_id = int(input("\nDigite o ID da sessão: "))
        comprar_ingresso(usuario_id, sessao_id)
    except ValueError:
        print(" ❌ ID inválido ")
    except Exception as e:
        print(f"Erro ao comprar o ingresso {e}")
    
def ver_meus_ingressos(usuario_id):
    #Exibe todos os ingressos do usuário
    print("\n--- MEUS INGRESSOS ---")
    ingressos = listar_ingressos_usuario(usuario_id)
    if ingressos: # busca os dados se a lista não estiver vazia
        for ingresso in ingressos:
            print(f"🎫 {ingresso[1]} | Sala {ingresso[2]} | {ingresso[3]} às {ingresso[4]} | Comprado em: {ingresso[5]}") ## dados em tuplas
    else:
        print("Você ainda não comprou nenhum ingresso.")



