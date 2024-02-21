with open('input2.txt', 'r') as file:
    lines = file.readlines()

n = int(lines[0].strip())  # Numero di password

passwords = []
hashes = []

for i in range(1, 2 * n+1):
    if i % 2 == 1:
        current_password = lines[i].strip()
        password_dict = {}
        for char in current_password:
            password_dict[char] = password_dict.get(char, 0) + 1
        passwords.append(password_dict)
    else:
        current_hash = lines[i].strip()
        hashes.append(current_hash)
print(passwords)
print(hashes)


for j in range (len(hashes)):
    current_hash = hashes[j]
    current_password=passwords[j]
    hash_diz={}
    correct=0
    for i in current_hash:
        letter=i
        if letter in current_password: # if letter belong to password
            if letter in hash_diz: #create dictionary                
                if hash_diz[letter]+1 > current_password[letter]: #if the number of recurrence of that letter is correct
                    hash_diz[letter] = 1
                else:
                    hash_diz[letter] += 1            

            else:
                hash_diz[letter] = 1   
                

            if hash_diz == current_password: #check if you're done
                correct=1 
                #print(hash_diz,current_password)           
        else:
            hash_diz={} #restart because youvare still in salt1
    print(correct)
    '''with open('output.txt', 'w') as file:
            print(correct, file=file)'''

   
