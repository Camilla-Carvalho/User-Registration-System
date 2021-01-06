def header(txt):
    print('==' * 23)
    print(f' {txt:^46} ')
    print('==' * 23)


def lin():
    print('--' * 26)

    
dados = {}
ficha = []

header('C A D A S T R O')
while True:
    dados.clear()
    try:
        dados['nome'] = input('Nome: ').capitalize()
    except:
        while dados['nome'].isnumeric():
            dados['nome'] = input('Digite somente letras: ').capitalize()
    else:
        while dados['nome'] == '':
            dados['nome'] = input('Digite um nome válido: ').capitalize()
            if dados['nome'].isnumeric():
                dados['nome'] = input('Digite somente letras: ').capitalize()

    dados['email'] = input('Email: ')


    try:
        dados['idade'] = int(input('Idade: '))
    except Exception as error:
        while ValueError:
            dados['idade'] = input('\033[31mERRO!(Digite um valor válido).\033[0m\nIdade:')

    else:
        if dados['idade'] <= 0:
            dados['idade'] = input('\033[31mDigite uma idade válida: ')

    try:
        dados['sexo'] = input('Sexo[F/M]: \033[0m').strip().upper()[0]
        if dados not in 'FM':
            pass
    except:
        while dados['sexo'] not in 'FM':
            print('\033[31mOpção inválida! ', end='')
            dados['sexo'] = input('Sexo[F/M]: \033[0m').strip().upper()[0]
    finally:
        ficha.append(dados.copy())

    option = input('Deseja continuar?[S/N]: ').strip().upper()[0]
    while option not in 'SN':
        if option not in 'SN':
            print('\033[31mOPÇÃO INVÁLIDA! ', end='')
        option = input('Deseja continuar?[S/N]: \033[0m\n\n').strip().upper()[0]
    if option in 'N':
        break

header('F O R M U L Á R I O')
for i in enumerate(ficha):
    for key, value in dados.items():
        print(f'{key}: {value}')
    print('--' * 23)
