# Você foi contratado para desenvolver um sistema simples de um banco que
# analisa e calcula um financiamento com parcelas fixas.
# Requisitos:
# 1. O programa deve solicitar:
# o Nome do cliente
# o Idade
# o Renda mensal
# o Valor desejado do empréstimo
# o Número de parcelas (3 até 24)
# 2. Regras para aprovação:
# o O cliente só será aprovado se:
# ▪ Ter mais de 18 anos
# ▪ O valor do financiamento for de no máximo 20 vezes a renda
# mensal
# 3. Taxa de juros:
# o até 6 parcelas → 5% ao mês
# o de 7 até 12 parcelas → 8% ao mês
# o de 13 até 24 parcelas → 10% ao mês
# 4. Cálculo do financiamento (parcelas fixas):
# o Para calcular o valor da parcela, utilize a fórmula:
# 𝑖(1+𝑖)𝑛
# ▪ 𝑃𝑀𝑇 = 𝑃𝑉 ⋅
# (1+𝑖)𝑛−1
# ▪ PMT → valor da parcela (PMT significa Payment/Pagamento)
# ▪ PV → valor financiado (PV significa Present Value, valor inicial
# da dívida)
# ▪ i → taxa de juros (em decimal de 0 até 1)
# ▪ n → número de parcelas
# 5. O sistema deve:
# o Informar se o empréstimo foi aprovado ou negado
# o Se aprovado:
# ▪ Nome do cliente
# ▪ Valor financiado
# ▪ Taxa de juros aplicada
# ▪ Valor da parcela
# ▪ Valor total pago
# ▪ Total de juros pagos
# 6. Cálculos adicionais:
# o Total pago:
# ▪ 𝑡𝑜𝑡𝑎𝑙 = 𝑃𝑀𝑇 ⋅ 𝑛
# o Juros pagos:
# ▪ 𝑗𝑢𝑟𝑜𝑠 = 𝑡𝑜𝑡𝑎𝑙 − 𝑃𝑉
# Regras de Implementação:
# * Crie funções como:
# o def pode_aprovar(idade, renda, valor):
# o def definir_taxa(parcelas):
# o def calcular_parcela(valor, taxa, parcelas):
# o def calcular_total(parcela, parcelas):
# o def calcular_juros(total, valor): 

def dados_cliente():
    nome = input("Nome do cliente: ")
    idade = int(input("Idade: "))
    renda = float(input("Renda mensal: "))
    valor_emprestimo = float(input("Valor desejado do empréstimo: "))
    parcelas = int(input("Número de parcelas (3 até 24): "))
    return nome, idade, renda, valor_emprestimo, parcelas

def pode_aprovar(idade, renda, valor):
    if idade > 18 and valor <= (renda * 20):
        return True
    return False

def definir_taxa(parcelas):
    if parcelas < 3 or parcelas > 24:
        return 0 
    elif parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    else:
        return 0.10
    
def calcular_parcela(valor, taxa, parcelas):
    i = taxa
    n = parcelas
    pv = valor
    pmt = pv * (i * (1 + i)**n) / ((1 + i)**n - 1)
    return pmt 


def calcular_total(parcela, parcelas):
    return parcela * parcelas
def calcular_juros(total, valor):
    return total - valor 


nome, idade, renda, valor, parcelas = dados_cliente()

if pode_aprovar(idade, renda, valor):

    taxa = definir_taxa(parcelas)

    if taxa == 0:
        print(" Número de parcelas inválido!")
    else:
        parcela = calcular_parcela(valor, taxa, parcelas)
        total = calcular_total(parcela, parcelas)
        juros = calcular_juros(total, valor)

        print("\n===== EMPRÉSTIMO APROVADO =====")
        print(f"Cliente: {nome}")
        print(f"Valor financiado: R$ {valor:.2f}")
        print(f"Taxa: {taxa*100:.0f}% ao mês")
        print(f"Parcela: R$ {parcela:.2f}")
        print(f"Total pago: R$ {total:.2f}")
        print(f"Juros pagos: R$ {juros:.2f}")

else:
    print("\n Empréstimo NEGADO!")

    