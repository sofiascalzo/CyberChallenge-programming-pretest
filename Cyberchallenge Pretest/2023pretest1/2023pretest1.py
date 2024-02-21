with open('input.txt', 'r') as file:
    lines = file.readlines()
Q, N = map(int, lines[0].split())  
solution = lines[1].strip()
data = [line.strip() for line in lines[2:]]

#Stampa
print("Q:", Q)
print("N:", N)
print("solution:", solution)
print("Data:")
for d in data:
    print(d)

def confronta_stringhe(s1,s2):
    if len(s1)!= len(s2):
        return -1
    
    count = 0
    for i in range(len(s1)):
        if s1[1] != '?' and s1[i] == s2[i]:
            count +=1
    
    return count


risposte_corrette = [confronta_stringhe(solution, row) for row in data if confronta_stringhe(solution,row) != -1]

# Stampa
print("Numero di risposte corrette per ogni riga:")
for num_risposte in risposte_corrette:
    print(num_risposte)

# Salvataggio su file
with open('output.txt', 'w') as file:
    for num_risposte in num_risposte_corrette:
        file.write(f"{num_risposte}\n")
print("Il risultato è stato salvato nel file 'output.txt'.")
