#Software para demonstração da utilização de dicionarios em python
#variavel = {
#  "chave1" : valor1
#  "chave2" : valor2
#  ....     }
def exibir(a):
    print(tabela[a])
    print("---------------\n")
tabela = {
    "Alface" : 2.50,
    "Batata" : 1.50,
    "Tomate" : 3.50,
    "Feijão" : 9.20,
}
exibir("Alface")

#Quando se atribui um valor a uma chave ja existente o valor sera subistituido
tabela["Alface"] = 1.25
exibir("Alface")

#É necessario sempre verificar se uma chave existe antes de chama-la
#Caso contrario o programa retornara erro e sera encerrado
if("Batata" in tabela): exibir("Batata")

#<dicionario>.keys() retorna as chaves que pertence ao dicionario
#<dicionario>.values() retorna os valoress que pertence ao dicionario
print(tabela.keys())
print(tabela.values())
print("\n-----------------")

#Para acessar os elementos de um dicionario de um dicionario podemos utilizar um comando de repetição for
for  x in tabela:
    print(x)
print("\n------------------")

#Para acessar os elementos de um dicionario podemos utilizarum comando associado ao método items()
for x,y in tabela.items():
    print(x,":",y)
print("\n---------------------")

#Para apagar um item do dicionario utiliza-se o comando del
del tabela["Alface"]
for x,y in tabela.items():
    print(x,":",y)
print("\n---------------------")

#Em python é possivel associar cada chave de um dicionario a uma lista
estoque = {
"caneta": [5000,1.5,1.1],
"lapis": [2000,1,0.8],
"borracha": [500,0.8,0.4]
}
print(estoque["caneta"])
print(estoque["lapis"])
print(estoque["borracha"])

