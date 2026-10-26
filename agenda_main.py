from agenda_func import addcomp, listar, remover, carregar

def menu():
    print("\n==============================")
    print("📅 Agenda de Compromissos (CLI)")
    print("==============================")
    print("1) Adicionar compromisso")
    print("2) Listar compromissos (todos)")
    print("3) Listar compromissos (apenas futuros)")
    print("4) Remover compromisso")
    print("0) Sair")

def main():
    compromissos = carregar()
    idantigo = {c["id"] for c in compromissos}

    while True:
        menu()
        opcao = input('Escolha uma opção: ').strip()

        if opcao == '1':
            addcomp(compromissos, idantigo)

        elif opcao == '2':
            listar(compromissos, apenasf = False)

        elif opcao == '3':
            listar(compromissos, apenasf = True)

        elif opcao == '4':
            remover(compromissos, idantigo)

        elif opcao == '0':
            print("Saindo do programa")
            break

        else:
            print("Número Inválido! Tente novamente...")
            continue

if __name__ == "__main__":
    main()
