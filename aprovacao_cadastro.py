primeiro_nome = str(input('Primeiro nome: '))
sobrenome = str(input('Sobrenome: '))
idade = int(input('Idade: '))

print('Informações do cadastrado: ', primeiro_nome, sobrenome, idade, 'anos')

if idade >= 18:
    print(primeiro_nome, ', você foi selecionado.')
else:
    print(primeiro_nome, ', você não foi selecionado.')

print('Fim.')
