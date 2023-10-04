#  Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
# tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

tipoCarne = input("Informe o corte de carne: ")
quantCarne = input("Informe a quantidade de quilos de carne: ")
formPag = input("Informe a forma de pagamento: ")

valorTotal = 0
desc = 0

if formPag.lower() == 'cartao tabajara':
    desc = quantCarne * 0.05
    if tipoCarne.lower() == 'file duplo':
        if quantCarne <= 5:
            valorTotal = (quantCarne * 4.9) - desc
        else:
            valorTotal = (quantCarne * 5.8) - desc
    if tipoCarne.lower() == 'alcatra':
        if quantCarne <= 5:
            valorTotal = (quantCarne * 5.9) - desc
        else:
            valorTotal = (quantCarne * 6.8) - desc
    if tipoCarne.lower() == 'picanha':
        if quantCarne <= 5:
            valorTotal = (quantCarne * 6.9) - desc
        else:
            valorTotal = (quantCarne * 7.8) - desc
elif formPag.lower() in ('dinheiro', 'pix', 'transferencia'):
    if tipoCarne.lower() == 'file duplo':
        if quantCarne <= 5:
            valorTotal = quantCarne * 4.9
        else:
            valorTotal = quantCarne * 5.8
    if tipoCarne.lower() == 'Alcatra':
        if quantCarne <= 5:
            valorTotal = quantCarne * 5.9
        else:
            valorTotal = quantCarne * 6.8
    if tipoCarne.lower() == 'picanha':
        if quantCarne <= 5:
            valorTotal = quantCarne * 6.9
        else:
            valorTotal = quantCarne * 7.8
else:
    print("Forma de pagamento inválida!")

print(f'Tipo de carne e: {tipoCarne} {quantCarne} Kg')
print(f'Preço total: R${valorTotal:.2f}')
print(f'Tipo de pagamento: {formPag}')
if desc > 0:
    print(f'Valor do desconto: R${desc:.2f}')
else:
    print('Não houve desconto')
print(f'Valor a pagar: R${valorTotal:.2f}')

