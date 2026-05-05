
print(' *** Cálculo de Produtividade ***')

try:
    tp = float(input('Valor total da venda:  '))
    funcio = int(input('Total de Funcionário :'))
    mépfuncio = tp / funcio
    
except (ValueError, TypeError):
    print('Informe um número. ')
except ZeroDivisionError:
    print('Não pode ser número zero')
else:
    print(f'Média por funcionário {mépfuncio: .2f}')



