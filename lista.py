#Programa para demonstração da utilização de listas
def exibir(a,b):
 for x in range(a,b):
  print(lst2[x], lst1[x])    
 print("\n----------------------------")

lst1 = ["Daniel Cristian Gomes", 23, 'M', 1.73, 65, "Solteiro"]
lst2 = ["Nome:", "Idade:", "Sexo:", "Altura:", "Peso:", "Estado Civil:"]
exibir(0,6)

#copy() retorna uma copia da lista
lista1 = lst1.copy()
lista2 = lst2.copy()

#append(valor) adiciona um elemento ao final da lista
lista1.append("22/05/1998")
lista2.append("Data de Nascimento:")
exibir(0,6)

#clear() remove todos os elementos de uma lista
lista1.clear()
lista2.clear()

print(lista1)
print(lista2)
print("\n----------------------------")

#extend() adiciona ao final de uma lista os elementos de outra lista um a um
lista1 = ["Itapeva", "São Paulo", "18407070"]
lista2 = ["Cidade:", "Estado:", "CEP:"]
lst1.extend(lista1)
lst2.extend(lista2)
exibir(0,9)

#count() retorna o numero de elementos que são iguais ao valor especificado
print(lst2.count("Nome:"))
print("\n----------------------------")

#index() retorna o indice do primeiro elemnto encontrado com o valor especificado
if("Idade:" in lst2): 
 print(lst2.index("Idade:"))

#insert(posição, valor) adiciona um elemento na posição pretendida

lst2.insert(0,"Id:")
lst1.insert(0,1)
exibir(0,9)

#pop() ou pop(posicao) remove o ultimo elemento da lista ou o da posição pretendida
lst1.pop(0)
lst2.pop(0)
exibir(0,8)

#remove() remove o item com o valor especificado apenas o primeiro que encontrar
lst1.remove("18407070")
lst2.remove("CEP:")
exibir(0,8)

#reverse() inverte a ordem dos valores da lista
lst2.reverse()
lst1.reverse()
exibir(0,8)

#sort() ordena os valores da lista em ordem alfabetica numerica
lista1.clear()
lista2.clear()
lista1 = [5, 8, 14, 3, 98, 7]
lista2 = ["Daniel", "Maria", "João", "Pedro", "Carlos"]
lista1.sort()
lista2.sort()
print(lista1)
print(lista2)

