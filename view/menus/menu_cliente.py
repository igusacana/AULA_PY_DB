from view.actions.cliente_actions import ver_filmes_cartaz, realizar_compra, ver_meus_ingressos
from funcoes_uteis import limpar_terminal 


def menu_cliente(user_logged):
    usu_id = user_logged[0]
    email_usu = user_logged[1]  

    while True:
        limpar_terminal()  
            
        print("\n" + "="*50)
        print(f"🎟️ BEM-VINDO, {email_usu}!")
        print("="*50)
        print("[1] - Ver filmes em cartaz")
        print("[2] - Comprar ingresso")
        print("[3] - Meus ingressos")
        print("[4] - Sair")
        print("="*50)
            
        opcao = input("Digite sua escolha: ")
            
        if opcao == "1":
            limpar_terminal()
            ver_filmes_cartaz()
            input("\nPressione ENTER para continuar...")
        elif opcao == "2":
            limpar_terminal()
            realizar_compra(usu_id)
            input("\nPressione ENTER para continuar...")
        elif opcao == "3":
            limpar_terminal()
            ver_meus_ingressos(usu_id)
            input("\nPressione ENTER para continuar...")
        elif opcao == "4":
            print("👋 Até logo!")
            input("\nPressione ENTER para continuar...")
            break
        else:
            print(" Opção inválida!")
            input("\nPressione ENTER para continuar...")