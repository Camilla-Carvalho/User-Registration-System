def header():
    print('==' * 26)
    print(f' {"C A D A S T R O":^52} ')
    print('==' * 26)


def lin():
    print('--' * 26)
dados = {}
ficha = []

header()
while True:
    dados.clear()
    dados['nome'] = input('Nome: ').capitalize()
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
        option = input('Deseja continuar?[S/N]: \033[0m').strip().upper()[0]
    if option in 'N':
        break

print(ficha)