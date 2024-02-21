import re

with open('input29.txt', 'r') as file:
    lines = file.readlines()
N = int(lines[0]) #N: number of passowrds
old=[]
new=[]
for i in range(1,N+1):
    new.append(lines[i].split()[0])
    old.append(lines[i].split()[1])
    #print(lines[i].split()[0],lines[i].split()[1],'\n')

    

def check(a,b):
    bool=0
    if ((len(a)>=8) and (len(a)<=16) and (re.search(r'[A-Z]', a)) and (re.search(r'[a-z]', a)) and (re.search(r'\d', a)) and (re.search(r'[^a-zA-Z0-9]', a)) and (a!=b)):
        for i in range(len(a) - 1): #check for consecutive characters    
            if a[i] == a[i + 1]:
                bool=0
                break
            else:
                bool=1 
        
        if bool==1:
            for i in range (min(len(a), len(b))-1):
                bool=0
                if a[i]!=b[i]: #found a difference

                    if a[i]==b[i+1]: #delete?  bca, bbca
                        for j in range (i+1,(min(len(a), len(b)))-1):
                            if a[j]==b[j+1]:
                                bool=0
                            else:
                                bool=1 #more than one difference
                                break  
                        
                    elif a[i+1]==b[i]: #addition?  bbca, bca
                        for j in range (i,(min(len(a), len(b)))-1):
                            if a[j+1]==b[j]:
                                bool=0
                            else:
                                bool=1 #more than one difference
                                break 
                
                    elif a[i+1]==b[i+1]: #substition?  bbca, ebca
                        for j in range (i+1,(min(len(a), len(b)))):
                            if a[j]==b[j]:
                                bool=0
                            else:
                                bool=1 #more than one difference
                                break
                    else: #no operation executed
                        bool=1
                        break
                    break
                
                         
                                    
    return bool

    
for i in range (len(new)):
    print(check((new[i]),(old[i])))

'''with open('output.txt', 'w') as output_file:
    for i in range(len(new)):
        output_file.write(check(new[i]))'''


'''print()
print(check(("q/0O:mKT0Q'uD"), ("q0O:mKT0Q'uD")))  #aggiunta
print(check(("123456aB£"),("123456aB$")))  #sostituzione
print(check(("&4A}@kf;z7.]Hn"), ("&4A}@kf6;z7.]Hn")))  #rimozione

print(check(("tutteminuscole2?"), ("bho"))) # manca minuscole
print(check(("MAIUSC2?"), ("bho")))    # manca maiuscole
print(check(("noNumeri?"), ("bho")))  # manca numeri
print(check(("noSpecial2"), ("bho")))  # manca speciali
print(check(("mancaroba"), ("bho")))   # tanti errori
print(check(("tutoOK2?yuj"), ("tutoOK2?yuj")))  # uguale alla precedente  
print(check(("tuttoOK2?"), ("bho")))    # caratteri consecutivi
print(check(("tutoOK2?"), ("bho")))   #è giusto'''
