# calculadora de IMC (Indice de masa corporal)

peso = int(input("Ingresa tu peso: "))
altura = float(input("Ingresa tu altura en mts: "))

imc = peso / altura ** 2

print("Tu IMC es: " "{0:.2f}".format(imc))
if imc < 18.5:
    print("Estas bajo de peso")
elif imc > 18.5 and imc < 25:
    print("Tu peso es saludable")
elif imc > 25 and imc < 30:
    print("Estas en sobrepeso, debes empezar con el ejercicio")
else:
    print("Consulta a tu medico")

