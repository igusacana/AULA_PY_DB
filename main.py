from services.user_service import insert_user, login
from view.menus.menu_admin import menu_admin
from view.menus.menu_cliente import menu_cliente
from funcoes_uteis import limpar_terminal  
from funcoes_uteis import hash_senha
import getpass

def main():
    """Menu principal do sistema"""
    while True:
        limpar_terminal()  # ← Limpa antes de mostrar o menu
        
        print("\n" + "="*50)
        print("🎬 SISTEMA DE CINEMA")
        print("="*50)
        print("[1] - Cadastrar-se")
        print("[2] - Login (Cliente)")
        print("[3] - Área Administrativa")
        print("[4] - Sair")
        print("="*50)
        
        opcao = input("Digite sua escolha: ")
        
        if opcao == "1":
            limpar_terminal()  # ← Limpa antes de mostrar o formulário
            email = input("Digite seu email: ")
            password = getpass.getpass("Digite sua senha: ")
            insert_user(email, password)
            input("\nPressione ENTER para continuar...")  # ← Pausa para ler a mensagem
            
        elif opcao == "2":
            limpar_terminal()
            email = input("Digite seu email: ")
            password = getpass.getpass("Digite sua senha: ")
            user_logged = login(email, password)
            
            if user_logged:
                print("✅ Login realizado com sucesso!")
                input("\nPressione ENTER para continuar...")
                menu_cliente(user_logged)
            else:
                print("❌ Login inválido!")
                input("\nPressione ENTER para continuar...")
                
        elif opcao == "3":
            limpar_terminal()
            senha_admin = getpass.getpass("Digite a senha de administrador: ")
            if senha_admin == "admin123":
                menu_admin()
            else:
                print("❌ Senha incorreta!")
                input("\nPressione ENTER para continuar...")
                
        elif opcao == "4":
            limpar_terminal()
            print("👋 Até logo!")
            break
        else:
            print("❌ Digite uma opção válida!")
            input("\nPressione ENTER para continuar...")


main()