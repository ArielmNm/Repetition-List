print("Nome Usuário:")
nomeUsuario = input()

print("Senha Usuário:")
SenhaUsuario = input()

while nomeUsuario == SenhaUsuario:
    print("Acesso Negado")
    print(input(nomeUsuario))
else:
    print("Acesso Permitido:", nomeUsuario)