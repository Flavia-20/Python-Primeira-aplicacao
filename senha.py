usuario = str(input("Digite seu usuário: "))
senha = int(input("Digite sua senha: "))

if senha == 123456 and usuario == 'entrei':
    print("Usuário validado!")
else:
    print("Usuário ou senha incorretos")
