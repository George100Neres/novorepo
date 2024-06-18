

nome = input("Informe o seu nome ")
not1 = float(input("Digite o valor da 1 nota "))
not2 = float(input("Digite o valor da 2 nota "))
not3 = float(input("Digite o valor da 3 nota "))
not4 = float(input("Digite o valor da 4 nota "))

somanot =  float(not1 + not2 + not3 + not4) / 4

print(f"Well Done! {nome}", "A soma das 4 notas e", f" {somanot:.2f} pontos")