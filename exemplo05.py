print(' *** Cálculo de Produtividade ***')

try:
    tp = float(input('Valor total da venda:  '))
    funcio = int(input('Total de Funcionário :'))
    mépfuncio = tp / funcio
    
except Exception as e:
    print(f'Ops! Erro nos valores de entrada {e}.')   
except ZeroDivisionError:
    print('Não pode ser número zero') 
except KeyboardInterrupt:
    print('Operação cancelado pelo usuário.')
else:
    print(f'Média por funcionário {mépfuncio: .2f}')

# Executa sempre. Com erro ou não, o bloco sempre irá executar
finally:
    print('Programa encerrada!')

