valor_da_compra = float(input("Digite o valor da compra: "))

idade_do_cliente = int(input("Digite a idade do cliente: "))

if idade_do_cliente >= 65:
    desconto = valor_da_compra * 0.20
    print(f"Desconto aplicado: R${desconto:.2f}")
else:
    print("Nenhum desconto aplicado.")