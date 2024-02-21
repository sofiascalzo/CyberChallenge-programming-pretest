a, b, c, d, e, f = 0, 0, 0, 0, 0, 0

N = int(input())

functions = ""

for i in range(N):
    functions += input().strip() + "\n"

lines = functions.splitlines()

i = 0

while i<len(lines):
    line = lines[i].split()
    # print(i, line, "|", a, b, c, d, e, f)
    if line[0] == "add":
        if line[1] == "a":
            a += int(line[2])
        elif line[1] == "b":
            b += int(line[2])
        elif line[1] == "c":
            c += int(line[2])
        elif line[1] == "d":
            d += int(line[2])
        elif line[1] == "e":
            e += int(line[2])
        elif line[1] == "f":
            f += int(line[2])
    elif line[0] == "sub":
        if line[1] == "a":
            a -= int(line[2])
        elif line[1] == "b":
            b -= int(line[2])
        elif line[1] == "c":
            c -= int(line[2])
        elif line[1] == "d":
            d -= int(line[2])
        elif line[1] == "e":
            e -= int(line[2])
        elif line[1] == "f":
            f -= int(line[2])
    elif line[0] == "mul":
        if line[1] == "a":
            a *= int(line[2])
        elif line[1] == "b":
            b *= int(line[2])
        elif line[1] == "c":
            c *= int(line[2])
        elif line[1] == "d":
            d *= int(line[2])
        elif line[1] == "e":
            e *= int(line[2])
        elif line[1] == "f":
            f *= int(line[2])
    elif line[0] == "jmp":
        if line[1] == "a":
            if a == int(line[2]):
                i = lines.index(f"lab {line[3]}")
        elif line[1] == "b":
            if b == int(line[2]):
                i = lines.index(f"lab {line[3]}")
        elif line[1] == "c":
            if c == int(line[2]):
                i = lines.index(f"lab {line[3]}")
        elif line[1] == "d":
            if d == int(line[2]):
                i = lines.index(f"lab {line[3]}")
        elif line[1] == "e":
            if e == int(line[2]):
                i = lines.index(f"lab {line[3]}")
        elif line[1] == "f":
            if f == int(line[2]):
                i = lines.index(f"lab {line[3]}")
    i+=1
print(a+b+c+d+e+f)

'''
test case 1

with open('input.txt', 'r') as file:
    lines = file.readlines()

n = int(lines[0].strip()) 
print(n)

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

for i in lines[1:n+1]:
    istruction = i.split()[0]
    var = i.split()[1]
    num = int(i.split()[2])  # Converto num in un intero per poter eseguire operazioni matematiche
    
    # Dizionario che associa le lettere ai loro incrementi/decrementi/moltiplicazioni
    switch = {
        "a": lambda x, y: x - y,
        "b": lambda x, y: x - y,
        "c": lambda x, y: x - y,
        "d": lambda x, y: x - y,
        "e": lambda x, y: x - y,
        "f": lambda x, y: x - y,
        "add": lambda x, y: x + y,
        "mul": lambda x, y: x * y,
        "sub": lambda x, y: x - y,
    }
    

    if istruction in switch:
        if istruction == "mul":
            switch[var] = lambda x, y: x * y 
        globals()[var] = switch[istruction](globals()[var], num)
        print(istruction, var, num)
    else:
        print("Istruzione non valida:", istruction)

result=a+b+c+d+e+f
with open('output.txt', 'w') as file:
        print(result, file=file)'''