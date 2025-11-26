from view.actions.admin_actions import cadastrar_filme, mostrar_filmes, cadastrar_salas, mostrar_salas, cadastrar_sessao, mostrar_sessoes
from funcoes_uteis import limpar_terminal
def menu_admin():
   while True:
        limpar_terminal()

        print("\n" + "="*30)
        print("🎬 ÁREA ADMINISTRATIVA DO CINEMA")
        print("="*30)
        print("[1] - Cadastrar filme")
        print("[2] - Listar filmes")
        print("[3] - Cadastrar sala")
        print("[4] - Listar salas")
        print("[5] - Criar sessão")
        print("[6] - Listar sessões")
        print("[7] - Voltar")
        print("="*30)

        opcao = int(input("Digite sua opção: "))

        if opcao == 1:
            limpar_terminal()
            cadastrar_filme()
            input("\nPressione ENTER para continuar...")
        elif opcao == 2:
            limpar_terminal()
            mostrar_filmes()
            input("\nPressione ENTER para continuar...")
        elif opcao == 3:
            limpar_terminal()
            cadastrar_salas()
            input("\nPressione ENTER para continuar...")
        elif opcao == 4:
            limpar_terminal()
            mostrar_salas()
            input("\nPressione ENTER para continuar...")
        elif opcao == 5:
            limpar_terminal()
            cadastrar_sessao()
            input("\nPressione ENTER para continuar...")
        elif opcao == 6:
            limpar_terminal()
            mostrar_sessoes()
            input("\nPressione ENTER para continuar...")
        elif opcao == 7:
            limpar_terminal()
            print("👋 Voltando ao menu principal...")
            input("\nPressione ENTER para continuar...")
            break
        else:
            print("opção inválida!!")
            input("\nPressione ENTER para continuar...")



    

