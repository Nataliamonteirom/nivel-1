historico_compras = []

while True:
    valor_da_compra = float(input("Digite o valor da compra (0 para encerrar): "))

    if valor_da_compra == 0:
        break

    if valor_da_compra < 0:
         print("Valor inválido! Digite um valor positivo.")
         continue

    desconto = 0.0
    desconto_extra = 0.0

    idade_do_cliente = int(input("Digite a idade do cliente: "))

    if idade_do_cliente >= 65:
        desconto = valor_da_compra * 0.20
        print(f"Desconto aplicado: R$ {desconto:.2f}")
    else:
        print("Nenhum desconto por idade aplicado.")

    if (valor_da_compra - desconto) > 100:
        desconto_extra = (valor_da_compra - desconto) * 0.10
        print(f"Desconto extra aplicado: R$ {desconto_extra:.2f}")
    else:
        print("Nenhum desconto extra aplicado.")

    valor_final = valor_da_compra - desconto - desconto_extra
    print(f"Valor final da compra: R$ {valor_final:.2f}")

    historico_compras.append({
        "valor_da_compra": valor_da_compra,
        "desconto": desconto,
        "desconto_extra": desconto_extra,
        "valor_final": valor_final
    })

quantidade_compras = len(historico_compras)
print(f"Quantidade de compras: {quantidade_compras}")

total_bruto = sum(
    compra["valor_da_compra"] for compra in historico_compras
)

print(f"Total bruto: R$ {total_bruto:.2f}")