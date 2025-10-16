#senha correta

senha_padrao = '123456'
senha_inserida = input('Insira uma senha: ')

if senha_inserida == senha_padrao:
    print('Senha correta, efetuando login...')
else:
    print('Senha incorreta, tente novamente')