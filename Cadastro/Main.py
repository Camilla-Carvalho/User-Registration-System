def header(txt):
    print('==' * 23)
    print(f' {txt:^46} ')
    print('==' * 23)


def lin():
    print('--' * 23)


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
            dados['idade'] = input(
                'ERRO!(Digite um valor válido).\nIdade:')

    else:
        if dados['idade'] <= 0:
            dados['idade'] = input('Digite uma idade válida: ')

    try:
        dados['sexo'] = input('Sexo[F/M]: ').strip().upper()[0]
        if dados not in 'FM':
            pass
    except:
        while dados['sexo'] not in 'FM':
            print('Opção inválida! ', end='')
            dados['sexo'] = input('Sexo[F/M]: ').strip().upper()[0]
    finally:
        ficha.append(dados.copy())

    option = input('Deseja continuar?[S/N]: ').strip().upper()[0]
    while option not in 'SN':
        if option not in 'SN':
            print('OPÇÃO INVÁLIDA! ', end='')
        option = input('Deseja continuar?[S/N]: \n\n').strip().upper()[0]
    lin()
    if option in 'N':
        break

header('F O R M U L Á R I O')
for i in enumerate(ficha):
    for key, value in dados.items():
        print(f'{key}: {value}')
    lin()
