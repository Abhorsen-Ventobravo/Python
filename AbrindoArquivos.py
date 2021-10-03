#Nome do Arquivo
nomeArq = "ArquivoTeste.txt"

#Gerador de arquivo de texto
# arq = open("<local do arquivo>", <modo>)
diretorio = "C:\Python"
arquivo = open(diretorio + "/" + nomeArq, "x")

#fechando arquivos
arquivo.close()

##########
print("Fim do Programa")