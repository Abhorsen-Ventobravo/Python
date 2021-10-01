#Nome do Arquivo
from os import write


nomeArq = "ArquivoTeste.txt"
diretorio = "C:\Python"
#Gerador de arquivo de texto
# arq = open("<local do arquivo>", <modo>)
#encoding="utf-8" garante a correta conversao de carcteres 
arquivo = open(diretorio + "/" + nomeArq, "a", encoding="utf-8")

#arquivo.write("Texto03\n")
for x in range(4,11):
    arquivo.write("Texto0" + str(x) + "\n")

#fechando arquivos
arquivo.close()

##########
print("Fim do Programa")