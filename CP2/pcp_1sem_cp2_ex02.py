# Faça um programa que leia 3 valores que representam os lados de um triângulo A,
# B e C e ordene-os em ordem decrescente, de modo que o lado A representa o
# maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados
# formam, com base nos seguintes casos:
# Se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO;
# Se A² = B² + C², apresente a mensagem: TRIANGULO RETANGULO;
# Se A² > B² + C², apresente a mensagem: TRIANGULO OBTUSANGULO;
# Se A² < B² + C², apresente a mensagem: TRIANGULO ACUTANGULO;
# Se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO;
# Se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO
# ISÓSCELES;

A = float(input("Digite o valor A: "))
B = float(input("Digite o valor B  "))
C = float(input("Digite o valor C: "))

#lado A representa o maior dos 3 lados
lados = sorted([A, B, C], reverse=True)
A,B,C = lados 

if A >= B+C:
 print("NAO FORMA TRIANGULO")
elif A**2 == B**2 + C**2:
 print("TRIANGULO RETANGULO")
elif A** 2 > B** 2 + C**2:
 print("TRIANGULO OBTUSANGULO")
elif A**2 < B**2 + C**2:
 print("TRIANGULO ACUTANGULO")

# A classificação por ângulos e por lados são independentes
# Um triângulo pode ser, por exemplo:
# RETANGULO + ISOSCELES ao mesmo tempo
 
if A == B == C:
 print("TRIANGULO EQUILATERO")
elif A == B or A == C or B == C:
  print("TRIANGULO ISOSCELES")