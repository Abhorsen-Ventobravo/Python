class Candidate :
    def __init__(self,name,course,age,state) :
      self.name = name
      self.course = course
      self.age = age 
      self.state = state   
    
    def to_string(self):
        print(f"{self.name}\n{self.course}\n{self.age}\n{self.state}\n")
        
def read_file(fileName):
    file =  open(fileName, "r", encoding="utf-8")
    contents = file.readlines()
    file.close()
    return contents

def get_candidates(datas):
    candidates = []
    header = datas[0]     
    for data in datas:
        if data == header:
            continue
        candidate_array = data.split(";")
        candidate = Candidate(candidate_array[0],candidate_array[1],candidate_array[2],candidate_array[3])    
        candidates.append(candidate)
    return candidates    

def get_candidates_of_course(candidates,courseName):
    return list(filter(lambda candidate: candidate.course == courseName,candidates))

def count_courses(candidates): 
    totalDotNet = len(get_candidates_of_course(candidates,"API .NET"))
    totalQA = len(get_candidates_of_course(candidates,"QA"))
    totalIOS = len(get_candidates_of_course(candidates,"iOS"))
    courses  = [0,0,0]
    
    total = (totalDotNet+totalIOS+totalQA)/100        
    courses[0] = totalDotNet/total
    courses[1] = totalIOS/total
    courses[2] = totalQA/total
    
    return courses
def sum_age_of_candidates_of_course(candidates,courseName):
    courseCandidates = get_candidates_of_course(candidates,courseName)
    return sum(map(lambda candidate: int(candidate.age.split(" ")[0]),courseCandidates))

def average_age(candidates,courseName):
    totalCandidates = len(get_candidates_of_course(candidates,courseName))
    totalAgeCandidates = sum_age_of_candidates_of_course(candidates,courseName)
    avarageAge = totalAgeCandidates/totalCandidates

    return avarageAge

def get_oldest_candidate(candidates,courseName):
    courseCandidates = get_candidates_of_course(candidates,courseName)
    oldest = max(map(lambda candidate: int(candidate.age.split(" ")[0]),courseCandidates))
    return oldest    

def get_youngest_candidate(candidates,courseName):
    courseCandidate = get_candidates_of_course(candidates,courseName)
    youngest = min(map(lambda candidate: int(candidate.age.split(" ")[0]),courseCandidate))
    return youngest    

def total_states(candidates):
     
     return len(set(list(map(lambda candidate: candidate.state,candidates))))
def save_order_by_name(candidates):
    candidates.sort()
    file = open("Sorted_AppAcadememy_Candidates.csv","w",encoding="utf-8")
    for candidate in candidates:
            file.writelines(candidate)
    file.close()

def find_intructor_api_net(candidates):
    for candidate in candidates:
        nameSeparado = candidate.name.split(" ")
        if nameSeparado[1][-1] == "k" and nameSeparado[0]:
            if candidate.age[0:2] == "21" or candidate.age[0:2] == "23" or candidate.age[0:2] == "25" or candidate.age[0:2] == "27":
               
                print("\nO instrutor de API .NET é:",candidate.name)
                

data = read_file("AppAcademy_Candidates.csv")
candidates = get_candidates(data)
numc = count_courses(candidates)

print("Porcentagem de Candidatos em cada área\n")
print("Candidatos de API_NET {0:.0f}%".format(numc[0]))
print("Candidatos de QA {0:.0f}%".format(numc[1]))
print("Candidatos de iOS {0:.0f}%".format(numc[2]))
print("\nMédia de idade dos candidatos de QA {:.0f} anos".format(average_age(candidates,"QA")))
print("\nCandidato mais velho de iOS:",get_oldest_candidate(candidates,"iOS")," anos")
print("\nCandidato mais novo de API_NET:",get_youngest_candidate(candidates,"API .NET")," anos")
print("\nSoma das ages dos candidatos API_NET:",sum_age_of_candidates_of_course(candidates,"API .NET"))
print("\nExistem ",total_states(candidates)," estados distintos ")
save_order_by_name(data)
find_intructor_api_net(candidates)