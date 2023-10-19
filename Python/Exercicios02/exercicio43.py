# O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

print('''
=================================
| COD |     PRODUTO     | VALOR | 
| 100 | Cachorro quente |R$ 1,20|
| 101 | Bauru Simples   |R$ 1,30|
| 102 | Bauru com ovo   |R$ 1,50|
| 103 | Hamburguer      |R$ 1,20|
| 104 | Chessburguer    |R$ 1,70|
| 105 | Suco            |R$ 2,20|
| 106 | Refrigerante    |R$ 1,00|
=================================
Para sair digite 0''')

menu = {
    '100': ['Cachorro quente', 1.20],
    '101': ['Bauru Simples', 1.30],
    '102': ['Bauru com ovo', 1.50],
    '103': ['Hamburguer', 1.20],
    '104': ['Chessburguer', 1.70],
    '105': ['Suco', 2.20],
    '106': ['Refrigerante', 1.00]
}
pedido = {}
while True:
    codigo = input('Informe o codigo: ')
    if (codigo == '0'):
        break
    if codigo in menu:
        quantidade = int(input('Informe a quantidade: '))
        if quantidade > 0:
            valorItem = menu.get(codigo)
            pedido.update({codigo: (valorItem, quantidade)})
valorDoPedido = 0
for linha in pedido.items():
    valorDoPedido += linha[1][0][1] * linha[1][1]  # Preço * Quantidade

print('\nSEU PEDIDO: ')

for linha in pedido.items():
    print(str(linha[1][1]) + ' x ' + 'R$ ' + str(round(linha[1][0][1], 2)) + ' --- ' + str(linha[1][0][0]))

print('\nTOTAL DO PEDIDO: R$ ' + str(round(valorDoPedido, 2)))