todos_alunos = list()
alunos = dict()

def alunos_cadastro():
    while True:
        alunos.clear()
        alunos['RA'] = valid_int('Digite o RA: ')
        verifica_cadastro()
        alunos['nome'] =  input('Digite o Nome: ').title()
        alunos['Nota'] = valid_float('Digite a Nota: ')
        alunos['Disciplina'] = input('Digite a Disciplina: ').title()
        todos_alunos.append(alunos.copy())
        while True:
            contador = str(input('Deseja inserir mais um aluno? [S/N]')).strip().upper()[0]
            if contador in 'SN':
                break
            print('Responda apenas com S para Sim ou N para não.')
        if contador == 'N':
            menu()

def valid_float(msg):
    ok = False
    valor = 0
    while True:
        alunos['Nota'] = str(input(msg)).strip()
        if alunos['Nota'].isnumeric():
            valor = float(alunos['Nota'])
            ok = True
        else:
            print('Digite um valor numérico válido')
        if ok:
            break
    return valor

def valid_int(msg):
    ok = False
    valor = 0
    while True:
        alunos['RA'] = str(input(msg)).strip()
        if alunos['RA'].isnumeric():
            valor = int(alunos['RA'])
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
    print('### LISTAGEM ###')
    for aluno in todos_alunos:
        #key = lambda(função para receber cada um dos itens da lista) valor(valor utilizado para ordenar)
        todos_alunos.sort(key=lambda valor: valor['RA'])
        print('RA: ' + str(aluno['RA']) + ' Nome: ' + str(aluno['nome']) + ' Nota: ' + str(aluno['Nota']) + ' Disciplina: ' + str(aluno['Disciplina']))
    contador = input('Gostaria de voltar ao Menu? Digite [S]: ').strip().upper()[0]
    if contador == 'S':
        menu()
    else:
        print('Responda apenas com S ou Sim')
        alunos_lista()



def encontra_aluno(RA):
    for aluno in todos_alunos:
        if RA == aluno['RA']:
            return 1
    return 0

def alunos_deletar():
    RA = int(input('### DELETAR ### \n Digite o RA do aluno: '))
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
    RA = int(input('### ATUALIZAR ### \n Digite o RA do aluno: '))
    i = 0
    if encontra_aluno(RA):
        for aluno in todos_alunos:
            if RA == aluno['RA']:
                del todos_alunos[i]

            i += 1

        while True:
            print('Digite os novos valores')
            alunos['RA'] = valid_int('Digite o RA: ')
            alunos['nome'] = str(input('Digite o nome: ')).title()
            alunos['Nota'] = valid_float('Digite a nota: ')
            alunos['Disciplina'] = str(input('Digite a Disciplina: ')).title()
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
          '║ # 2 - REMOVER   # ║ \n',
          '║ # 3 - LISTAR    # ║ \n',
          '║ # 4 - ATUALIZAR # ║ \n',
          '║ # 5 - FECHAR    # ║\n',
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





