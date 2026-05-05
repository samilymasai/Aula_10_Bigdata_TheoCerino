
#for i in range(5):
    
#        tp = float(input('Valor total da venda:  '))
#        funcio = int(input('Total de Funcionário :'))
#
#        mépfuncio = tp / funcio
#        print(f'Média por funcionário {mépfuncio: .2f}')
    



#-----------------------
# for com try : Não para de executar , se lança um erro
for i in range(5):
    try:
        tp = float(input('Valor total da venda:  '))
        funcio = int(input('Total de Funcionário :'))
        mépfuncio = tp / funcio
        print(f'Média por funcionário {mépfuncio: .2f}')
    except ValueError:
        print('Informe um número. ')
    except ZeroDivisionError:
        print('Não pode ser número zero')



