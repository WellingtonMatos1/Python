todos_alunos = list()
alunos = dict()

def alunos_cadastro():
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
        """elif contador == 'S':
            verifica_cadastro()
            alunos_cadastro()"""

def verifica_cadastro():
    for aluno in todos_alunos:
        if alunos['RA'] == alunos['RA']:
            print('RA já cadastrado!!')
            alunos_cadastro()

def alunos_lista():
    i = 0

    for aluno in todos_alunos:
        print('Nome: ' + str(aluno['nome']) + ' RA: ' + str(aluno['RA']) + ' Nota: ' + str(aluno['Nota']) + ' Disciplina: ' + str(aluno['Disciplina']))
    i += 1
    menu()


def encontra_aluno(RA):
    for aluno in todos_alunos:
        if RA == aluno['RA']:
            return 1
    return 0

def alunos_deletar():
    RA = input('### DELETAR ### \n Digite o RA do aluno: ')
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
        elif len(todos_alunos) == 0:
            print('Não há alunos na lista')
            menu()
        else:
            alunos_deletar()
    else:
        print('RA não encontrado')
        return alunos_deletar()

def alunos_atualizar():
    RA = str(input('### ATUALIZAR ### \n Digite o RA do aluno: '))
    i = 0
    if encontra_aluno(RA):
        for aluno in todos_alunos:
            if RA == aluno['RA']:
                del todos_alunos[i]

            i += 1

        while True:
            print('Digite os novos valores')
            alunos['nome'] = str(input('Digite o nome: '))
            alunos['RA'] = input('Digite o RA: ')
            alunos['Nota'] = float(input('Digite a nota: '))
            alunos['Disciplina'] = str(input('Digite a Disciplina: '))
            todos_alunos.append(alunos.copy())
            while True:
                contador = str(input('Deseja atualizar outro aluno? [S/N]')). upper()[0]
                if contador in 'SN':
                    break
                print('Responda apenas com S para Sim ou N para não.')
            if contador == 'N':
                menu()
            else:
                alunos_atualizar()


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
        return print('### CADASTRO ###', alunos_cadastro())
    elif valor == 2:
        return print(alunos_deletar())
    elif valor == 3:
        return print('### LISTAGEM ###', alunos_lista())
    elif valor == 4:
        return print('### ATUALIZAR ###', alunos_atualizar())
    elif valor == 5:
        return exit()
    else:
        print('Digite um valor válido')
        menu()
if __name__ == "__main__":
    menu()





