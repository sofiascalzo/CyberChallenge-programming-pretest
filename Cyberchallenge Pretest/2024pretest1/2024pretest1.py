with open('input.txt', 'r') as file :
    lines=file.readlines()
n,m,=map(int,lines[0].split())
print(n,m)

def substring(main_string, sub_string):
    return sub_string in main_string


bannedWords=[]
for i in lines[1:m+1]:
    bannedWords.append(i.strip())
#print(bannedWords)


words=[]
for i in lines[m+1:n+m+1]:
    words.append(i.strip())
#print(words)

with open("output.txt", "w") as output_file:

    for word in words:
        for banned in bannedWords:
            if substring(word, banned):
                print("BANNED", file=output_file)
            else:
                print("SAFE", file=output_file)


