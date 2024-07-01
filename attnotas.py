# Lista para armazenar informações dos alunos
alunos = []

# No primeiro momento vamos fazer uma função para adicionar aluno
def adicionar_aluno():
    ra = input("Digite o RA (5 caracteres): ").strip().ljust(5, ' ')[:5]
    nome = input("Digite o nome (até 27 caracteres): ").strip().ljust(27, ' ')[:27]
    nota_b1 = float(input("Digite a nota B1 (0 a 10): ").strip())
    nota_b2 = float(input("Digite a nota B2 (0 a 10): ").strip())
    alunos.append({"ra": ra, "nome": nome, "nota_b1": nota_b1, "nota_b2": nota_b2})

# a função é a seguinte: 
def listar_alunos():
    for aluno in alunos:
        print(f"RA: {aluno['ra']} | Nome: {aluno['nome']} | Nota B1: {aluno['nota_b1']} | Nota B2: {aluno['nota_b2']}")

# No segundo momento vamos fazer uma função para adicionar aluno
def remover_aluno():
    ra = input("Digite o RA do aluno a ser removido: ").strip().ljust(5, ' ')[:5]
    global alunos
    alunos = [aluno for aluno in alunos if aluno['ra'] != ra]

# Agora faremos uma funcao para procurar o aluno pelo RA
def procurar_aluno():
    ra = input("Digite o RA do aluno: ").strip().ljust(5, ' ')[:5]
    for aluno in alunos:
        if aluno['ra'] == ra:
            print(f"RA: {aluno['ra']} | Nome: {aluno['nome']} | Nota B1: {aluno['nota_b1']} | Nota B2: {aluno['nota_b2']}")
            return
    print("Aluno não encontrado.")

# Faremos uma função neste momento para listar alunos aprovados
def listar_aprovados():
    for aluno in alunos:
        media = (aluno['nota_b1'] + aluno['nota_b2']) / 2
        if media >= 7:
            print(f"RA: {aluno['ra']} | Nome: {aluno['nome']} | Média: {media:.2f}")

# Faremos uma função neste momento para listar alunos reprovados
def listar_reprovados():
    for aluno in alunos:
        media = (aluno['nota_b1'] + aluno['nota_b2']) / 2
        if media < 7:
            print(f"RA: {aluno['ra']} | Nome: {aluno['nome']} | Média: {media:.2f}")

# Faremos uma função neste momento para procurar o aluno pelo RA
def procurar_pelo_nome():
    nome = input("Digite o nome do aluno: ").strip().ljust(27, ' ')[:27]
    for aluno in alunos:
        if aluno['nome'].strip() == nome.strip():
            print(f"RA: {aluno['ra']} | Nome: {aluno['nome']} | Nota B1: {aluno['nota_b1']} | Nota B2: {aluno['nota_b2']}")
            return
    print("Aluno não encontrado.")

# Faremos uma função neste momento para calcular a média da turma B1
def media_turma_b1():
    if alunos:
        media_b1 = sum(aluno['nota_b1'] for aluno in alunos) / len(alunos)
        print(f"Média da turma B1: {media_b1:.2f}")

# Função para calcular a média da turma B2
def media_turma_b2():
    if alunos:
        media_b2 = sum(aluno['nota_b2'] for aluno in alunos) / len(alunos)
        print(f"Média da turma B2: {media_b2:.2f}")

# Função para calcular a média geral da turma
def media_turma_geral():
    if alunos:
        media_geral = sum((aluno['nota_b1'] + aluno['nota_b2']) / 2 for aluno in alunos) / len(alunos)
        print(f"Média geral da turma: {media_geral:.2f}")

# Função para exibir o diário da turma
def diario_turma():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("--------------------------------------------------------")
    print("                   Diário da turma                      ")
    print("--------------------------------------------------------")
    print("RA    Nome                      Nota B1  Nota B2   Média")
    print("--------------------------------------------------------")
    
    total_b1 = total_b2 = 0
    
    for aluno in alunos:
        media = (aluno['nota_b1'] + aluno['nota_b2']) / 2
        total_b1 += aluno['nota_b1']
        total_b2 += aluno['nota_b2']
        print(f"{aluno['ra'].ljust(5)} {aluno['nome'].ljust(27)} {str(aluno['nota_b1']).rjust(7)} {str(aluno['nota_b2']).rjust(7)} {str(media).rjust(7)}")
    
    media_b1 = total_b1 / len(alunos)
    media_b2 = total_b2 / len(alunos)
    media_geral = (media_b1 + media_b2) / 2
    
    print("--------------------------------------------------------")
    print(f"{'Médias da Turma'.ljust(30)} {str(media_b1).rjust(7)} {str(media_b2).rjust(7)} {str(media_geral).rjust(7)}")
    print("--------------------------------------------------------")

# Menu interativo
def menu():
    while True:
        print("\nMenu:")
        print("1 - Adicionar aluno")
        print("2 - Listar alunos")
        print("3 - Remover aluno")
        print("4 - Procurar aluno")
        print("5 - Listar aprovados")
        print("6 - Listar reprovados")
        print("7 - Procurar pelo nome do aluno")
        print("8 - Média da turma B1")
        print("9 - Média da turma B2")
        print("10 - Média da turma geral")
        print("11 - Diário da turma")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            adicionar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            remover_aluno()
        elif opcao == "4":
            procurar_aluno()
        elif opcao == "5":
            listar_aprovados()
        elif opcao == "6":
            listar_reprovados()
        elif opcao == "7":
            procurar_pelo_nome()
        elif opcao == "8":
            media_turma_b1()
        elif opcao == "9":
            media_turma_b2()
        elif opcao == "10":
            media_turma_geral()
        elif opcao == "11":
            diario_turma()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção negad. Tente novamente.")

if __name__ == "__main__":
    menu()