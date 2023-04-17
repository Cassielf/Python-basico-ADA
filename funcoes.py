"""
funcoes sao trechos de codigos reutilizaveis que realizam determinadas acoes quando invocados
exemplos de funcoes - print, len, max, min, input

"""

def mensagem1():
    print('domingo tem live do super junior')


def mensagem(bias, elf = 'Byanca'):
    print(f'olá {elf} elf, domingo será um dia especial!')
    print(f'domingo tem live do super junior, e {bias} estará lá')

mensagem('Hyukjae')

def soma (num1, num2):
    resultado = num1 + num2
    return resultado

resultado = soma(27,14)

print (resultado)

def calculadora (num1, num2, operador = '+'):
    if operador == '+':
        return num1+num2
    elif operador == '-':
        return num1-num2
    elif operador == '*':
        return num1*num2
    else:
        num1/num2

resultado = calculadora(1,100,'+')

print (resultado)

