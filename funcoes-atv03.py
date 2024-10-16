# Crie duas funções:
# - calcular_area_base, que recebe o raio de um círculo e retorna sua área.
# - calcular_volume_cilindro, que utiliza a função calcular_area_base para calcular o volume de um cilindro dado o raio e a altura.

def calcular_area_base():
    area = (raio*raio) * 3.14
    return f"A área do circulo é: {area}"

print("Digite o raio para calcular a área do círculo e do cilindro.")
raio = float(input("Digite o raio: "))

areadocirculo = calcular_area_base()
print(areadocirculo)

def calcular_volume_cilindro():
    altura = float(input("Digite a altura do cilindro: "))
    volume = 3.14 * altura * (raio * raio)
    return f"O volume do cilindro é {volume}"


print("Digite a altura do cilindro para calcular o volume desse cilindro.")
volumetotal = calcular_volume_cilindro()
print(volumetotal)

