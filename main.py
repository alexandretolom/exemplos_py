'''
Exemplo de algoritmo devolve troco.
O programa pede o preço a pagar e o dinheiro que recebeu. A partir dos valores ele calcula o troco a ser devolvido e suas respectivas unidades em notas/moedas.
'''

def troco():
    dinheiro_total = float(input("Preço a pagar R$:"))
    dinheiro_recebido = float(input("Dinheiro recebido R$:"))
    troco = dinheiro_recebido-dinheiro_total
    sim = False
    while sim==False:
        if dinheiro_recebido < dinheiro_total:
            print("Dinheiro recebido é menor que o dinheiro total, digite novamente")
            dinheiro_total = float(input("Preço a pagar R$:"))
            dinheiro_recebido = float(input("Dinheiro recebido R$:"))
            troco = dinheiro_recebido-dinheiro_total
        elif dinheiro_recebido == dinheiro_total:
            print("Dinheiro recebido igual ao valor total. Não há troco")
            break
        else:
            troco_formatado = "{:.2f}".format(troco)
            print("Troco a devolver: R$", troco_formatado)


            #reais em notas
            print(int(troco//100), "notas de 100 reais")
            troco = troco%100
            print(int(troco//50), "notas de 50 reais")
            troco = troco%50
            print(int(troco//20), "notas de 20 reais")
            troco = troco%20
            print(int(troco//10), "notas de 10 reais")
            troco = troco%10
            print(int(troco//5), "notas de 5 reais")
            troco = troco%5
            print(int(troco//2), "notas de 2 reais")
            troco = troco%2


            #moedas    
            moedas_1real = 0
            for x in range(0, int(troco), 1):
                troco -= 1
                moedas_1real += 1
            print(moedas_1real, "moedas de 1 real")
            print(int(troco//.50), "moedas de 50 centavos")
            troco = troco%.50
            print(int(troco//.25), "moedas de 25 centavos")
            troco = troco%.25
            print(int(troco//.10), "moedas de 10 centavos")
            troco = troco%.10
            print(int(troco//.05), "moedas de 5 centavos")
            troco = troco%.05
            print(int(troco//.01), "moedas de 1 centavo")
            troco = troco%.01
            sim = True
troco()