# Faça um programa que recebe:
# * o código do estado de origem da carga de um caminhão, supondo que é um
# número inteiro de 1 a 5
# * o peso da carga do caminhão em toneladas
# * o código da carga, supondo que é um número inteiro de 10 e 40
# Seu programa deve calcular:
# * o peso da carga do caminhão convertido em quilos
# * o preço da carga do caminhão
# * valor do imposto que é cobrado com base no preço da carga e do estado de
# origem
# * o valor total transportado pelo caminhão (carga + impostos)
# Utilize as tabelas abaixo:
# Obs.: considere que o usuário irá digitar tudo corretamente 

def estado_origem_caminhao(): 
    origem_codigo = int(input("Digite o código do estado (1-5): "))
    carga_toneladas = float(input("Digite o peso da carga em toneladas: "))
    codigo_carga = int(input("Digite o código da carga (10-40): "))
    return origem_codigo, carga_toneladas, codigo_carga


origem_codigo, carga_toneladas, codigo_carga = estado_origem_caminhao()


peso_kg = carga_toneladas * 1000


if 10 <= codigo_carga <= 20:
    preco_carga = peso_kg * 100
elif 21 <= codigo_carga <= 30:
    preco_carga = peso_kg * 250
elif 31 <= codigo_carga <= 40:
    preco_carga = peso_kg * 340
else:
    print("Código de carga inválido!")
    preco_carga = 0


if origem_codigo == 1:
    imposto = preco_carga * 0.35
elif origem_codigo == 2:
    imposto = preco_carga * 0.25
elif origem_codigo == 3:
    imposto = preco_carga * 0.15
elif origem_codigo == 4:
    imposto = preco_carga * 0.05
elif origem_codigo == 5:
    imposto = 0
else:
    print("Código de estado inválido!")
    imposto = 0


valor_total = preco_carga + imposto

print(f"\nPeso da carga em quilos: {peso_kg} kg")
print(f"Preço da carga: R$ {preco_carga:.2f}")
print(f"Imposto: R$ {imposto:.2f}")
print(f"Valor total: R$ {valor_total:.2f}")