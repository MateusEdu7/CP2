# Você foi contratado para criar um sistema de RH que calcula o salário final de um
# funcionário com base em diversos fatores: cargo, horas extras, faltas, bônus e
# descontos.
# Requisitos:
# 1. O programa deve solicitar:
# o Nome do funcionário
# o Cargo (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário)
# o Salário base (float)
# o Total de horas extras trabalhadas
# o Total de faltas no mês
# o Se recebeu bônus por desempenho (s ou n)
# 2. Regras de cálculo:
# o Valor da hora extra:
# ▪ 1.5% do salário base por hora extra
# o Desconto por falta:
# ▪ 2% do salário base por falta
# o Bônus (se aplicável):
# ▪ Gerente: R$ 1000
# ▪ Analista: R$ 500
# ▪ Assistente: R$ 300
# ▪ Estagiário: R$ 100
# 3. O sistema deve:
# o Calcular e mostrar:
# ▪ Salário bruto
# ▪ Total de acréscimos (horas extras + bônus)
# ▪ Total de descontos (faltas)
# ▪ Salário final
# Regras de Implementação:
# * Crie funções como:
# o def calcular_horas_extras(salario_base, horas):
# o def calcular_descontos_faltas(salario_base, faltas):
# o def calcular_bonus(cargo, recebeu_bonus): 

nome = input("Digite o nome do funcionário: ")
cargo = int(input("Digite o cargo (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário): "))
salario_base = float(input("Digite o salário base: "))
horas_extras = float(input("Digite o total de horas extras: "))
faltas = int(input("Digite o total de faltas: "))
bonus_desempenho = input("Recebeu bônus? (s/n): ").lower() #utilizar o lower para ter a respotsa em letras minusculas 


def calcular_descontos_faltas(salario_base, faltas):
    desconto_falta = salario_base * 0.02
    return desconto_falta * faltas 
def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus == 's':
        if cargo == 1:
            return 1000
        elif cargo == 2:
            return 500
        elif cargo == 3:
            return 300
        elif cargo == 4:
            return 100
    return 0 

def calcular_horas_extras(salario_base, horas): 
    valor_hora_extra = salario_base * 0.015
    return valor_hora_extra * horas


desconto_faltas = calcular_descontos_faltas(salario_base, faltas)
bonus = calcular_bonus(cargo, bonus_desempenho)
hora_extra = calcular_horas_extras(salario_base, horas_extras)

salario_bruto = salario_base + hora_extra + bonus 
salario_final = salario_bruto - desconto_faltas

print(f"\n--- Resumo do pagamento de {nome} ---")
print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Total de acréscimos: R$ {hora_extra + bonus:.2f}")
print(f"Total de descontos: R$ {desconto_faltas:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")
