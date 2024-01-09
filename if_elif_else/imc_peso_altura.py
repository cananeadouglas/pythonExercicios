peso = float(input('digite seu peso '))
altura = float(input('digite sua altura '))

imc = peso / (altura*altura)

print(imc)

if imc < 18.5:
    print('vc está abaixo do Peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade mórbida')
