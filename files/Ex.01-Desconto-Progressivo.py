'''
 *  Exercício: Desconto progressivo
 *  Repositório: Lógica de Programação e Algoritmos em Python
 *  GitHub: @michelelozada


Para este exercício, procurei os preços de uma loja de produtos do ramo de lembrancinhas/souvenirs, que trabalhasse com
o chamado desconto progressivo à medida que a quantidade encomendada aumenta (atacado). Uma das promoções encontradas foi
a seguinte:

-------------------------------
  ITEM - COD. 3021
  Preço unitário: R$ 1,25

  Tabela de preços - Atacado*:
  Quantidade (un.)  Desconto
  de 60 a 99            -
  de 100 a 249         4%
  de 250 a 499        12%
  de 500 a 749        20%
  de 750 a 999        28%
  acima de 1000       32%

  * Pedido mínimo de 60 unidades
-------------------------------

O algoritmo abaixo é para registro do vendedor da encomenda feita pelo cliente.
'''

while True:
    item = "Souvenir Código 3021"
    print('\nPRODUTO: ' + item)
    try:
        quantidade = int(input('  Qual a quantidade deste produto a ser encomendada (em unidades)? '))
        # definição dos intervalos
        if (quantidade < 60):
            print(f'\n> Aviso: Vendas somente acima de 60 unidades. Por favor, comece novamente.\n')
            continue;
        elif (quantidade >= 60 and quantidade <= 99):
            percentual = 0
        elif (quantidade >= 100 and quantidade <= 249):
            percentual = 4
        elif (quantidade >= 250 and quantidade <= 499):
            percentual = 12
        elif (quantidade >= 500 and quantidade <= 749):
            percentual = 20
        elif (quantidade >= 750 and quantidade <= 999):
            percentual = 28
        elif (quantidade >= 1000):
            percentual = 32
        # atribuição e cálculo dos valores
        preco = 1.25
        abatimento = quantidade * preco * (percentual / 100)
        total = quantidade * preco - abatimento
        print(
            f'\nREGISTRO DA ENCOMENDA \n  Item escolhido: {item} \n  Quantidade encomendada: {quantidade} unidades \n  Valor do pedido: R$ {quantidade * preco:.2f} \n  Desconto promocional: R$ {abatimento:.2f}\n  Total a pagar: R$ {total:.2f}\n')

        # tratamento de exceções
    except ValueError:
        print('\n> Aviso: O valor digitado precisa ser um número. Por gentileza, tente novamente.\n')
        continue

    sair = input('Deseja encerrar o programa? Digite S para sair e qualquer outra tecla para continuar. ')
    if(sair.upper() == 'S' or sair=='sim'):
        print('Programa encerrado...')
        break
    else:
        continue


"""
PRODUTO: Souvenir Código 3021
  Qual a quantidade deste produto a ser encomendada (em unidades)? 350

REGISTRO DA ENCOMENDA 
  Item escolhido: Souvenir Código 3021 
  Quantidade encomendada: 350 unidades 
  Valor do pedido: R$ 437.50 
  Desconto promocional: R$ 52.50
  Total a pagar: R$ 385.00

Deseja encerrar o programa? Digite S para sair e qualquer outra tecla para continuar. s
Programa encerrado...
"""