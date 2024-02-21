import os

folder = "2024-pattern-dataset"

try:
    files = os.listdir(f"./{folder}/script-outputs")
    for file in files:
        os.remove(f"./{folder}/script-outputs/{file}")
except:
    os.mkdir(f"./{folder}/script-outputs")

inputs = os.listdir(f"./{folder}/input")

def readline(txt):
    return txt.pop(0).strip(), txt

def find_patterns(string):
    patterns = []
    for i in range(1, len(string) + 1):
        pattern = string[:i]
        if all(string[j:j + len(pattern)] == pattern for j in range(0, len(string), len(pattern))) or (string == pattern*(len(string)//len(pattern)) + pattern[-(len(string)-(len(pattern)*(len(string)//len(pattern)))):] and string.endswith(pattern)):
            patterns.append(pattern)
    return patterns

def solve(file):
    test = open(file, "r").read().splitlines()
    first_line, test = readline(test)
    T = int(first_line)
    out = open(f"./{folder}/script-outputs/output-{os.path.basename(file).split('.')[0]}.txt", "a")
    for _ in range(T):
        line, test = readline(test)
        N, M = map(int, line.strip().split())
        alphabet, test = readline(test)
        S, test = readline(test)
        patterns = find_patterns(S)
        out.write(str(len(patterns))+"\n")
    out.close()

for inputFile in inputs:
    solve(f"./{folder}/input/{inputFile}")
    