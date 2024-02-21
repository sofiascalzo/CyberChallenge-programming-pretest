with open('input-1-0.txt', 'r') as file:
    lines = file.readlines()
T = int(lines[0]) #T: number of test cases
N, M, S = list(map(int, lines[1].split()))  # N: number of candidates, M: number of selected, S: number of skills per player

OptimalTeam={}
for skill in lines[2].split():
    if skill in OptimalTeam:
        OptimalTeam[skill] += 1
    else:
        OptimalTeam[skill] = 1

CandidatesSkills={}              # {skills: [score,score...]} of N candidates
for i in range(4, len(lines), 2):
    category = lines[i].strip().split()[0]
    #print(category)
    values = lines[i].strip().split()

    if category in CandidatesSkills:
        CandidatesSkills[category].extend(map(int, values[1:]))
    else:
        CandidatesSkills[category] = list(map(int, values[1:]))

for category, scores in CandidatesSkills.items():
    CandidatesSkills[category] = sorted(scores, reverse=True)

#print (T,N,M,S)
        
#for key, value in OptimalTeam.items():
#    print(f"{key}: {value}")

#for key, value in CandidatesSkills.items():
 #   print(f"{key}: {value}")

TotalScore=0
for key, value in OptimalTeam.items():
    if key in CandidatesSkills:
        selected_scores = CandidatesSkills[key][:value]   #select the top value scores of the corrisponding skill (with the same key in the dictionary)
        TotalScore += sum(selected_scores)
    else:
        TotalScore += 0   #add 0 if no one has that skill

print(TotalScore)

'''
with open('output-1-0.txt', 'w') as output_file:
    output_file.write('TotalScore')
'''
