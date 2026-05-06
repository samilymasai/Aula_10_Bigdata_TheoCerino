#Cálculo média de nota 
# Não sabemos quantos alunos , mas todos terão 4 notas sempre 
def  calcula_média(n):
    tota = sum(n)
    media = tota / len(n)
    return media, tota


contador =  1
#resposta = 'S' 
while True:
    print(f"Aluno{contador}")
    aluno = input('Nome do aluno:')

    notas = []
    try:
        for i in range(4):
            nota = float(input("Informe o número da nota :"))
            notas.append(nota)

    except ValueError:
        print('Erro: Informe apenas valores válidos!')
    else:
        total, média = calcula_média(notas) 


        print(f'\nResultado      \n Aluno {aluno}') 
        print(f"Total de Pontos: {total}")
        print(f"Média: {média:.2f}")

    
    finally:
        print('Processo encerrado para o aluno.')

    opcao = input('Deseja calcular para outro aluno ?')

    resposta = input('Continuar? ').upper().strip()
    if resposta != 'S':
        break


    contador += 1


print("Programa encerrado.")    