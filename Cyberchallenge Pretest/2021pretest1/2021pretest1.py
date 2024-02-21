with open('input6.txt', 'r') as file :
    lines=file.readlines()
n,m,k=map(int,lines[0].split())
print(n,m,k)

matrice = [list(line.strip()) for line in lines[1:]]
newmatrice = [list(line.strip()) for line in lines[1:]]

for row in matrice:
    print(row)
     

def neighborhood(matrice, riga, colonna):
    count = 0

    for i in range(max(0, riga - 1), min(n, riga + 2)):
        for j in range(max(0, colonna - 1), min(m, colonna + 2)):
            if i != riga or j != colonna:  
                if matrice[i][j] != '.':
                    count += 1
   # print(count, i,j)

    return count


for z in range (k):
    for i in range (n):
        for j in range (m):
            print(k, matrice[i][j], i, j , neighborhood(matrice,i,j))
            
            if matrice [i][j]=='.'and neighborhood(matrice,i,j)>4:
                newmatrice[i][j]='+'   
            elif matrice [i][j]=='+':
                if neighborhood(matrice,i,j)>4:
                    newmatrice[i][j]='*'
                if neighborhood(matrice,i,j)<4:
                    newmatrice[i][j]='.'
            else:
                if neighborhood(matrice,i,j)>4:
                    newmatrice[i][j]='+'
                if neighborhood(matrice,i,j)<4:
                    newmatrice[i][j]='.'
    matrice=newmatrice
    print('\n')               
    for row in matrice:
        print(row)
                

            