n,k = map(int, input().split(' '))
events = []
for i in range(n):
    a,b = map(int, input().split(' '))
    events.append((a, 0))
    events.append((b+1, 1))#in b sono ancora validi, molto più comodo cosi se un evento è (2,5) nell'array so che in 6 devo fare --, dato che in 5 è ancora valido(range inclusi)

events.sort()
print(events)
curr = 0
res = 0
last_event = -1
for i in range(len(events)):
    if i != 0 and events[i][0] != events[i-1][0]: #appena finisce la sequenza di eventi uguali (tipo 2,2,2,3)
        if curr == k:
            res += events[i][0] - last_event #2,2,2,2,5 = 5-2 = 3 numeri coperti con #curr invervalli
    
    if events[i][1] == 0:#apertura
        curr += 1
    else:
        curr -= 1#chiusura

    last_event = events[i][0] 

print(res)