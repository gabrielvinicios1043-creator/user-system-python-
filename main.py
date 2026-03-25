print("\n=== SISTEMA DE USUÁRIOS ===")
usuarios = []
logados = []
while True:
    acao = input("1 - Registrar usúario: \n"
                 "2 - Login.\n"
                 "3 - Lista de Usúarios.\n"
                 "4 - Logout.\n"
                 "5 - Remover usúario.\n"
                 "6 - Sair\n"
                 "Escolha: ")
    if acao == "1":
        nome = input("Novo Usúario: ").strip().lower()
        if not nome:
            print("Nome inválido!")
            continue
        if nome in usuarios:
            print("Usúario já existe!")
            continue
        usuarios.append(nome)
        print("Registrado com sucesso!")
    elif acao == "2":
        nome = input("Usúario: ").strip().lower()
        if nome not in usuarios:
            print("Usúario não existe!")
            continue
        if nome in logados:
            print("Usúario já está logado!")
            continue
        logados.append(nome)
        print("Login realizado!")
    elif acao == "3":
        print("\nUsuários registrados:")
        for u in usuarios:
            print(u)

        print("\nUsuários logados:")
        for l in logados:
            print(l)
    elif acao == "4":
        print("\nUsuários logados:")
        for l in logados:
            print(l)
        nome = input("Qual usúario deseja remover?").strip().lower()
        if nome in logados:
            logados.remove(nome)
            print("Logout realizado!")
        else:
            print("Usúario não esta logado!")
            continue
    elif acao == "5":
        print("\nUsúarios logados: ")
        for i in logados:
            print(i)
        nome = input("Qual usúario deseja remover? ")
        if nome in logados:
            logados.remove(nome)
            if nome in logados:
                logados.remove(nome)
                print("Usúario removido!")
            else:
                print("Usúario não encontrado!")
    elif acao == "6":
        print("Encerrando o programa...")
        break
