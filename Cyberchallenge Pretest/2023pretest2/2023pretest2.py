with open('input-2-9.txt', 'r') as file:
    lines = file.readlines()
M, N, S = map(int, lines[0].split())    # M: number of players, N: number of tasks, S: number of submissions
tasks = {}
for line in lines[1 : N+1]:
    values = line.split()
    correctflag = values[1]
    points = int(values[2])
    tasks[correctflag] = points
taskslist = list(tasks.keys())  # correct flag list

scoreboard = {key: (key, 0, int('0')) for key in range(1, M+1)}  # initial scoreboard {player:{score:time}}
solved_flags = {key: set() for key in range(1, M+1)} #player: {'flag1', 'flag3', ...},
submissions = []

for line in lines[N+1 : N+S+1]:
    values = line.split()
    player = int(values[0])
    taskid = int(values[1])
    flag = values[2]
    time = int(values[3])
    
    submission = {
        "player": player,
        "taskid": taskid,
        "flag": flag,
        "time": time
    }
    submissions.append(submission)


submissions.sort(key=lambda x: x['time']) # sort submissions by time

for submission in submissions:
    player = submission["player"]
    taskid = submission["taskid"]
    flag = submission["flag"]
    time = submission["time"]

    if flag in tasks and taskid == taskslist.index(flag) + 1: # is a valid flag
            if flag not in solved_flags[player]:
                scoreboard[player] = (player, scoreboard[player][1] + tasks[flag], time) # update score scoreboard
                solved_flags[player].add(flag) 

#print(scoreboard)

sorted_scoreboard = sorted(scoreboard.values(), key=lambda x: (-x[1], x[2])) # sort scoreboard by score and time

for player_data in sorted_scoreboard:
    print(f"{player_data[0]} {player_data[1]}")
    #print(f"{player_data[0]} {player_data[1]} {player_data[2]}")


'''with open('output-2-9.txt', 'w') as output_file:
    for player_info in sorted_scoreboard:
        output_line = f"{position[0]} {position[1]}"
        output_file.write(output_line + "\n")'''
