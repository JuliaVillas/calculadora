'''
CALCULADORA EM PYTHON

- O que faz uma calcudora?
- O que tem uma calculadora?
    -sinais
    -memória
    -números
'''

n1 = float(input('digite um número: '))
sinal = input('selecione o sinal da operação "+", "-", "*", "/" e "**": ' )
n2 = float(input('digite outro número: '))
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
divi = n1 / n2
quad = n1 ** n2

if sinal == '+':
    print(f'O resultado da adição é: {soma}.')
elif sinal == '-':
    print(f'O resultado da subtração é: {sub}.')
elif sinal == '*':
    print(f'O resultado da multiplicação é: {mult}')
elif sinal == '/':
    print(f'O resultado da divisão é: {divi}')
elif sinal == '**':
    print(f'O resultado da divisão é: {quad}')
else:
    print('Sinal inválido!')

