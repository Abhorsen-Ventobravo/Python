class Candidate :
    def __init__(self,nome,curso,idade,estado) :
      self.nome = nome
      self.curso = curso
      self.idade = idade 
      self.estado = estado   
    
    def to_string(self):
        print(self.nome)
        print(self.curso)
        print(self.idade)
        print(self.estado)  
        
def read_file(fileName):
    file =  open(fileName, "r", encoding="utf-8")
    lines = file.readlines()
    file.close()
    return lines

def lines_to_list(data):
    candidates = []     
    for fastData in data:
        list = fastData.split(";")
        if list[0] != "Nome" and list[1] != "Vaga" and list[2] != "Idade" and list[3] != "Estado":
            candidate = Candidate(list[0],list[1],list[2],list[3])    
            candidates.append(candidate)
    return candidates    

def nunbers_courses(candidates): 
    courses  = [0,0,0]
    for candidate in candidates:
        if candidate.curso == "API .NET":
            courses[0] +=1
        if candidate.curso == "QA":
            courses[1] +=1    
        if candidate.curso == "iOS":
            courses[2] +=1
    total = (courses[0]+courses[1]+courses[2])/100        
    courses[0] = courses[0]/total
    courses[1] = courses[1]/total
    courses[2] = courses[2]/total
    
    return courses

def average_age_qa(candidates):
    
    numCand,total = 0,0
    for  candidate in candidates:
        if candidate.curso == "QA":
            total += int(candidate.idade[0:2])
            numCand +=1
    return total/numCand

def best_year_ios(candidates):
    num1,num2 = 0,0
    for candidate in candidates:
        if candidate.curso == "iOS":
            num1 = int(candidate.idade[0:2])
            if num1 > num2:
               num2 = num1 
    return num2    

def small_year_api_net(candidates):
    num1,num2 = 0,0
    for candidate in candidates:
        if candidate.curso == "API .NET":
            num1 = int(candidate.idade[0:2])
            if num1 < num2 or num2 == 0:
               num2 = num1 
    return num2    

def sum_ages_api_net(candidates):
    total = 0
    for candidate in candidates:
      if candidate.curso == "API .NET":
          total += int(candidate.idade[0:2])
    return total

def count_countries(candidates):
     estado =[]
     for candidate in candidates:
         estado.append(candidate.estado)  
     return len(set(estado))

def save_order_by_name(candidates):
    candidates.sort()
    file = open("Sorted_AppAcademy_Candidates.csv","w",encoding="utf-8")
    for candidate in candidates:
            file.writelines(candidate)
    file.close()

def find_intructor_api_net(candidates):
    for candidate in candidates:
        nomeSeparado = candidate.nome.split(" ")
        if nomeSeparado[1][-1] == "k":
            if candidate.idade[0:2] == "21" or candidate.idade[0:2] == "23" or candidate.idade[0:2] == "25" or candidate.idade[0:2] == "27":
                print("\nO instrutor de API .NET é:",candidate.nome)
                

data = read_file("AppAcademy_Candidates.csv")
candidates = lines_to_list(data)
numc = nunbers_courses(candidates)

print("Porcentagem de Candidatos em cada área\n")
print("Candidatos de API_NET {0:.0f}%".format(numc[0]))
print("Candidatos de QA {0:.0f}%".format(numc[1]))
print("Candidatos de iOS {0:.0f}%".format(numc[2]))
print("\nMédia de idade dos candidatos de QA {:.0f} anos".format(average_age_qa(candidates)))
print("\nCandidato mais velho de iOS:",best_year_ios(candidates)," anos")
print("\nCandidato mais novo de API_NET:",small_year_api_net(candidates)," anos")
print("\nSoma das idades dos candidatos API_NET:",sum_ages_api_net(candidates))
print("\nExistem ",count_countries(candidates)," estados distintos ")
save_order_by_name(data)
find_intructor_api_net(candidates)