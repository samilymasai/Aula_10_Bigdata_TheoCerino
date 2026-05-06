try:
   saldo =  1000
   print(f" valor da sua conta R${saldo}")

   sacar = int(input('Saque o Dinheiro: '))
   print(f" O seu saque foi R${sacar}.")

   res = saldo - sacar
   

except Exception as e:
    print(f'Houve erro devido a "{e}".Tente com número.')
else:
    print(f'O que foi sobrado após do saque foi R${res}.')