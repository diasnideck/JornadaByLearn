def imc(peso, altura):
  altura_quadrada = altura ** 2
  meu_imc = peso / altura_quadrada
  return meu_imc

meu_imc = imc(90, 1.80)
print(f' O meu imc é {meu_imc:.2f}')