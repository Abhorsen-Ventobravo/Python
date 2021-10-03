#Nome do Arquivo
from os import write


nomeArq = "ArquivoTeste.txt"
diretorio = "C:\Python"
#Gerador de arquivo de texto
# arq = open("<local do arquivo>", <modo>)
#encoding="utf-8" garante a correta conversao de carcteres 
arquivo = open(diretorio + "/" + nomeArq, "r", encoding="utf-8")

linhas = arquivo.read()
#linhas = arquivo.readlines()
#arquivo.write("Texto03\n")
#for x in range(4,11):
#arquivo.write("Texto0" + str(x) + "\n")
matriz = linhas.split("\n")#split - Trasforma a lista segundo uma referencia
#fechando arquivos
arquivo.close()

print(linhas)
#for x in linhas:
 #   print(x)
##########
