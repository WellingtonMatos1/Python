todos_alunos = list()
alunos = dict()

def alunos_cadastro():
    while True:
        alunos.clear()
        alunos['RA'] = leia_int('Digite o RA: ')
        verifica_cadastro()
        alunos['nome'] = str(input('Digite o Nome: '))
        alunos['Nota'] = leia_float('Digite a Nota: ')
        alunos['Disciplina'] = str(input('Digite a Disciplina: '))
        todos_alunos.append(alunos.copy())
        while True:
            contador = str(input('Deseja inserir mais um aluno? [S/N]')).strip().upper()[0]
            if contador in 'SN':
                break
            print('Responda apenas com S para Sim ou N para não.')
        if contador == 'N':
            menu()

def leia_float(msg):
    ok = False
    valor = 0
    while True:
        alunos['Nota'] = str(input(msg))
        if alunos['Nota'].isnumeric():
            valor = float(alunos['Nota'])
            ok = True
        else:
            print('Digite um valor numérico válido')
        if ok:
            break
    return valor

def leia_int(msg):
    ok = False
    valor = 0
    while True:
        alunos['RA'] = str(input(msg))
        if alunos['RA'].isnumeric():
            valor = float(alunos['RA'])
            ok = True
        else:
            print('Digite um valor numérico válido')
        if ok:
            break
    return valor


def verifica_cadastro():
    for aluno in todos_alunos:
        if aluno['RA'] == alunos['RA']:
            print('RA já cadastrado!!')
            alunos_cadastro()

def alunos_lista():
    i = 0
    print('### LISTAGEM ###')
    for aluno in todos_alunos:
        print('Nome: ' + str(aluno['nome']) + ' RA: ' + str(aluno['RA']) + ' Nota: ' + str(aluno['Nota']) + ' Disciplina: ' + str(aluno['Disciplina']))
    i += 1
    contador = input('Quando quiser voltar para o Menu digite [S]: ').strip().upper()[0]
    if contador == 'S':
        menu()
    else:
        print('Responda apenas com S para sim')
        alunos_lista()



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
            contador = str(input('Deseja excluir mais um aluno? [S/N]')).strip().upper()[0]
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
            alunos['RA'] = leia_int('Digite o RA: ')
            alunos['nome'] = str(input('Digite o nome: '))
            alunos['Nota'] = leia_float('Digite a nota: ')
            alunos['Disciplina'] = str(input('Digite a Disciplina: '))
            todos_alunos.append(alunos.copy())
            while True:
                contador = str(input('Deseja atualizar outro aluno? [S/N]')).strip().upper()[0]
                if contador in 'SN':
                    break
                print('Responda apenas com S para Sim ou N para não.')
            if contador == 'N':
                menu()
            else:
                alunos_atualizar()
    else:
        print('RA não encontrado')
        return alunos_atualizar()

def menu():
    print(' ╔═══════════════════╗\n',
          '║   ### MENU ###    ║\n',
          '║ # 1 - CADASTRAR # ║ \n',
          '║ # 2 - REMOVER #   ║ \n',
          '║ # 3 - LISTAR #    ║ \n',
          '║ # 4 - ATUALIZAR # ║ \n',
          '║ # 5 - FECHAR #    ║\n',
          '║   ### ----- ###   ║\n',
          '╚═══════════════════╝')
    valor = int(input('Digite a operação desejada: '))

    if valor == 1:
        return print('### CADASTRO ###', alunos_cadastro())
    elif valor == 2:
        return print(alunos_deletar())
    elif valor == 3:
        return print(alunos_lista())
    elif valor == 4:
        return print('### ATUALIZAR ###', alunos_atualizar())
    elif valor == 5:
        return exit()
    else:
        print('Digite um valor válido')
        menu()
if __name__ == "__main__":
    menu()





