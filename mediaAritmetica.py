# Programa lerá vários números e retornará a média entre eles
import testeNumeral
notas = []

while True:
    valor = input('Digite a nota do aluno: ')  # Recebe os números digitados
    print('(Para encerrar a inclusão de notas basta digitar uma letra)')

    if testeNumeral.numero_ou(valor):  # Usa um módulo para verificar se é um numeral
        notas.append(float(valor))
    else:
        break

if not notas:
    print('Nenhuma nota foi adicionada!')
else:
    print(f'A média dessas notas é {sum(notas) / len(notas)}')  # Retorna a média de todas as notas
#                                                                              adicionadas na lista
