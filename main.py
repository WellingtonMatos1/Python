def alunos_cadastro():
    global todos_alunos
    todos_alunos = list()
    alunos = dict()
    while True:
        alunos.clear()
        alunos['nome'] = str(input('Digite o nome: '))
        alunos['RA'] = input('Digite o RA: ')
        alunos['Nota'] = float(input('Digite a nota: '))
        alunos['Disciplina'] = str(input('Digite a Disciplina: '))
        todos_alunos.append(alunos.copy())
        while True:
            contador = str(input('Deseja inserir mais um aluno? [S/N]')). upper()[0]
            if contador in 'SN':
                break
            print('Responda apenas com S para Sim ou N para não.')
        if contador == 'N':
            menu()


def alunos_lista():
    print(todos_alunos)
    menu()


def encontra_aluno(RA):
    for aluno in todos_alunos:
        if RA == aluno['RA']:
            return 1
    return 0

def alunos_deletar():
    RA = str(input('### DELETAR ### \n Digite o RA do aluno: '))
    i = 0
    if encontra_aluno(RA):
        for aluno in todos_alunos:
            if RA == aluno['RA']:
                del todos_alunos[i]

        i += 1

        while True:
            contador = str(input('Deseja excluir mais um aluno? [S/N]')).upper()[0]
            if contador in 'SN':
                break
            print('Responda apenas com S para Sim ou N para não.')
        if contador == 'N':
            menu()
        else:
            alunos_deletar()

def menu():
    print('### MENU ### \n',
          '# 1 - CADASTRAR # \n',
          '# 2 - REMOVER # \n',
          '# 3 - LISTAR # \n',
          '# 4 - ATUALIZAR # \n',
          '# 5 - FECHAR # \n',
          '### ----- ###')
    valor = int(input('Digite a operação desejada: '))

    if valor == 1:
        return print('Opção cadastro selecionada: ', alunos_cadastro())
    elif valor == 2:
        return print(alunos_deletar())
    elif valor == 3:
        return print('### Listagem ###', alunos_lista())
    elif valor == 5:
        return exit()

if __name__ == "__main__":
    menu()





