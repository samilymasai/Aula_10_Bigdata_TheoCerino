# Cálculo de produtividade
#--------------

print(' *** Cálculo de Produtividade ***')

try:
    tp = float(input('Valor total da venda:  '))
    funcio = int(input('Total de Funcionário :'))
    mépfuncio = tp / funcio
    print(f'Média por funcionário {mépfuncio: .2f}')
except ValueError:
    print('Informe um número. ')
except ZeroDivisionError:
    print('Não pode ser número zero')


