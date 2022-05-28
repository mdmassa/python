from time import sleep

cadastro = 0
code = 0
tentativas = 0

print('BEM-VINDO A PÁGINA DE CADASTRO.')
sleep(1)

while cadastro == 0:

    print('Digite seu login: ')
    login_sistema = input()
    sleep(1)
    print('Digite sua senha: ')
    senha_sistema = input()

    if len(senha_sistema) >= 8:
        print('CADASTRO FEITO COM SUCESSO.')
        cadastro += 1

    else:
        sleep(1)
        print('SUA SENHA DEVE CONTER PELO MENOS 8 CARACTERES.')


if cadastro == 1:

    sleep(1.5)

    print('AGORA FAÇA LOGIN COM SUAS CREDENCIAIS.')
    sleep(1)

    while code == 0:
        print('Digite seu login: ')
        login = input()
        sleep(1)
        print('Digite sua senha: ')
        senha = input()

        if login == login_sistema:
            if senha == senha_sistema:
                sleep(1)
                print('ACESSO CONCEDIDO')
                code += 1
            else:
                tentativas += 1
                sleep(1)
                print('SENHA INCORRETA')
            if tentativas == 3:
                code += 1
                print('ACESSO NEGADO.')

        else:
            sleep(1)
            print('ACESSO NEGADO. LOGIN INCORRETO')
