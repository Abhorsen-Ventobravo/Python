from os import write


class Candidate :
    def __init__(self,nome,curso,idade,estado) :
      self.nome = nome
      self.curso = curso
      self.idade = idade 
      self.estado = estado   
    
    def toString(self):
        print(self.nome)
        print(self.curso)
        print(self.idade)
        print(self.estado)  

def readFile(fileName):
    file =  open(fileName, "r", encoding="utf-8")
    lines = file.readlines()
    file.close()
    return lines

def linesToList(dados):
    candidates = []     
    for dado in dados:
        list = dado.split(";")
        if list[0] != "Nome" and list[1] != "Vaga" and list[2] != "Idade" and list[3] != "Estado":
            candidate = Candidate(list[0],list[1],list[2],list[3])    
            candidates.append(candidate)
    return candidates    

def numCourses(dadosPorcent): 
    courses  = [0,0,0]
    for candidate in dadosPorcent:
        if candidate.curso == "Android":
            courses[0] +=1
        if candidate.curso == "QA":
            courses[1] +=1    
        if candidate.curso == "iOS":
            courses[2] +=1
  
    return courses

def averageAgeQA(candidates):
    numCand,total = 0,0
    for  candidate in candidates:
        if candidate.curso == "QA":
            total += int(candidate.idade[0:2])
            numCand +=1
    return total/numCand

def bestYearsIos(candidates):
    num1,num2 = 0,0
    for candidate in candidates:
        if candidate.curso == "iOS":
            num1 = int(candidate.idade[0:2])
            if num1 > num2:
               num2 = num1 
    return num2    

def smallYearsAndroid(candidates):
    num1,num2 = 0,0
    for candidate in candidates:
        if candidate.curso == "Android":
            num1 = int(candidate.idade[0:2])
            if num1 < num2 or num2 == 0:
               num2 = num1 
    return num2    

def somaIdadesAndroid(candidates):
    total = 0
    for candidate in candidates:
      if candidate.curso == "Android":
          total += int(candidate.idade[0:2])
    return total

def countDistintictCountries(candidates):
     estado =[]
     for candidate in candidates:
         estado.append(candidate.estado)    
     return len(set(estado))

def saveOrderByName(candidates):
    candidates.sort()
    file = open("Sorted_AppAcademy_Candidates.csv","w",encoding="utf-8")
    for candidate in candidates:
            file.writelines(candidate)
    file.close()

dados = readFile("AppAcademy_Candidates.csv")
candidates = linesToList(dados)
numc = numCourses(candidates)
numTotal = numc[0]+numc[1]+numc[2]
print("Porcentagem de Candidatos em cada área\n")
print("Candidatos de Android {0:.0%}".format(numc[0]/numTotal))
print("Candidatos de QA {0:.0%}".format(numc[1]/numTotal))
print("Candidatos de iOS {0:.0%}".format(numc[2]/numTotal))
print("\nMédia de idade dos candidatos de QA {:.0f} anos".format(averageAgeQA(candidates)))
print("\nCandidato mais velho de iOS:",bestYearsIos(candidates)," anos")
print("\nCandidato mais novo de Android:",smallYearsAndroid(candidates)," anos")
print("\nSoma das idades dos candidatos Android:",somaIdadesAndroid(candidates))
print("\nExistem ",countDistintictCountries(candidates)," estados distintos ")

saveOrderByName(dados)