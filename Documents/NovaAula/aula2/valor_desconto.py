valor_compra = float(input("Informe o valor da sua compra para verificar elegibilidade para desconto: "))

if valor_compra >= 250.00:
    print("PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00")
    print(f"O SEU DESCONTO É DE {valor_compra*(10/100):.2f} REAIS")
elif valor_compra > 500.00:
    print("PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%")
    print(f"O SEU DESCONTO É DE {valor_compra*(30/100):.2f} REAIS")
else:
    print("POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA.")