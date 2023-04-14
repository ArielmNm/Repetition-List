print("Nome Usuário:")
nomeUsuario = input()

print("Senha Usuário:")
SenhaUsuario = input()

while nomeUsuario == SenhaUsuario:
    print("Acesso Permitido")
    print(input(nomeUsuario))
else:
    print("Senha Incorreta")
    print("Nome Usuário:")
    nomeUsuario = input()
    print("Senha Usuário:")
    SenhaUsuario = input()