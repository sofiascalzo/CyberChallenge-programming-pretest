import math

with open('input-2-1.txt', 'r') as file:
    lines = file.readlines()
N, T = map(int, lines[0].split())  # N: number of tasks, T: number of a round
tasks = list(map(int, lines[1].split()))  # time of each task
#print (N)

TotalT = sum(tasks)
minW = math.ceil(TotalT / T)         # initial minimum number of workers
#print(minW)                   (input-1-0/1-9)

TimeW = [] # Time taken by each worker
for i in range(minW):
    TimeW.append(tasks[i]) # initial time of each worker

def is_worker_enough(tasks, T, num_workers):
    TimeW = tasks[:num_workers]
    i = num_workers

    while i < len(tasks):
        firstW = min(TimeW)
        min_index = TimeW.index(firstW)

        if TimeW[min_index] + tasks[i] <= T:
            TimeW[min_index] += tasks[i]
            i += 1
        else:
            return False

    return True

def find_min_workers(tasks, T):
    left, right = 1, len(tasks)

    while left < right:
        mid = (left + right) // 2

        if is_worker_enough(tasks, T, mid):
            right = mid
        else:
            left = mid + 1

    return left
       
min_workers = find_min_workers(tasks, T)
print(min_workers)  # Output the minimum number of workers needed (input-2-0/2-9)

'''with open('output-2-0.txt', 'w') as output_file:
    output_file.write('minW+j')'''
        




'''while i < N:
    firstW = min(TimeW)
    min_index = TimeW.index(firstW)

    if TimeW[min_index] + tasks[i] <= T:
        TimeW[min_index] += tasks[i]
        i += 1
    else:
        j += 1
        i=minW+j
        TimeW = tasks[0:i]
       
print(minW+j)  # Output the minimum number of workers needed (input-2-0/2-9)

    firstW and min_index are calculated to find the worker with the minimum completion time.
    It is checked whether assigning the task tasks[i] to the identified worker would violate the time constraint T. If it doesn't violate the constraint, the task is assigned to that worker, otherwise, the process moves to the next step.

If the task cannot be assigned to the current worker without violating the time constraint:

    j is incremented by 1, indicating the need to add a new worker.
    The list TimeW is emptied.
    The completion times of the newly added workers are initialized.
    i is set to minW+j to indicate from which task to resume the assignment in the main loop'''


