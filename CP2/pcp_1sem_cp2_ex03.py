# 1. O programa deve solicitar:
# Nota do Checkpoint 1 (cp1)
#  Nota do Checkpoint 2 (cp2)
# Nota do Checkpoint 3 (cp3)
#  Nota da Sprint 1 (sp1)
#  Nota da Sprint 2 (sp2)
#  Nota da Global Solution (gs)
# 2. O programa deve solicitar:
#  Todas as notas variam de 0 a 10 e podem ser decimais
#  O sistema deve identificar a menor nota entre os três checkpoints
#  A menor nota deve ser desconsiderada no cálculo
# 3. A composição da média segue os seguintes pesos:
#  40% → média dos 2 maiores Checkpoints + 2 Sprints
#  60% → nota da Global Solution
#  40% → média do 1º semestre
# 4. Cálculo da média:
#  A média do semestre deve ser calculada utilizando:
# ▪ As duas maiores notas dos checkpoints
# ▪ As duas notas das sprints
# ▪ A nota da Global Solution
# 5. O sistema deve:
#  Mostrar:
# ▪ Média do semestre (sem peso)
# ▪ Média do semestre com peso
# 6. Regras de implementação:
#  Utilizar estruturas condicionais
#  Não utilizar funções prontas como min()
#  Trabalhar com valores decimais
#  Implementar manualmente a lógica para encontrar a menor nota
# 7. Dica:
#  Primeiro encontre a menor nota entre os checkpoints
#  Depois aplique a fórmula removendo essa nota
#  Por fim, calcule as médias e exiba com 1 casa decimal

def solicitar_notas():
    """Solicita todas as notas necessárias do usuário"""
    cp1 = float(input("Digite a nota do Checkpoint 1 (0-10): "))
    cp2 = float(input("Digite a nota do Checkpoint 2 (0-10): "))
    cp3 = float(input("Digite a nota do Checkpoint 3 (0-10): "))
    sp1 = float(input("Digite a nota da Sprint 1 (0-10): "))
    sp2 = float(input("Digite a nota da Sprint 2 (0-10): "))
    gs = float(input("Digite a nota da Global Solution (0-10): "))
    return cp1, cp2, cp3, sp1, sp2, gs

def encontrar_menor_checkpoint(cp1, cp2, cp3):
    """Encontra a menor nota entre os três checkpoints"""
    menor = cp1
    if cp2 < menor:
        menor = cp2
    if cp3 < menor:
        menor = cp3
    return menor


def calcular_media(cp1, cp2, cp3, sp1, sp2, gs):
    """Calcula as médias do semestre"""
    menor = encontrar_menor_checkpoint(cp1, cp2, cp3)
   
    soma_cp = cp1 + cp2 + cp3 - menor
    media_cp = soma_cp / 2

    # Média do semestre (sem peso)
    media_semestre = (media_cp + sp1 + sp2 + gs) / 4

    # Média ponderada
    media_ponderada = ((media_cp + sp1 + sp2) / 3) * 0.4 + (gs * 0.6)

    return media_semestre, media_ponderada


def main():
    cp1, cp2, cp3, sp1, sp2, gs = solicitar_notas()

    media_semestre, media_ponderada = calcular_media(cp1, cp2, cp3, sp1, sp2, gs)

    print("\nRESULTADOS:")
    print(f"Média do semestre (sem peso): {media_semestre:.1f}")
    print(f"Média do semestre (com peso): {media_ponderada:.1f}")

main()