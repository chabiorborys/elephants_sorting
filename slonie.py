import sys
#Seperating data needed from User inputs
user_input = []

for line in sys.stdin:
    user_input.append(line.rstrip())
#Converting User data
user_input[1] = [int(i) for i in user_input[1].split()]
user_input[2] = [int(i) for i in user_input[2].split()]
user_input[3] = [int(i) for i in user_input[3].split()]
#Applying User data
number_of_elephants = int(user_input[0])
weight_of_elephants = user_input[1]
source = user_input[2]
target = user_input[3]
#Saving minimum weight of all elephants for later usage
min_weight = min(weight_of_elephants)
#Setting each elephant to False in order to seperate cycles later
found = []
for el in range(number_of_elephants):
    found.append(False)

# Creating a function that finds and returns a cycle
def findCycle(first): 
    cycle = []    
    x = first

    while True:
        cycle.append(x)
        found[source.index(x)] = True
        target_idx = target.index(x)
        next_x = source[target_idx]
        if next_x == first:
            break
        else:
            x = next_x
    return cycle
#Colecting all cycles and setting data for findCycle
cc = []
for idx in range(len(found)):
    if found[idx]:
        continue
    else:
        cc.append(findCycle(source[idx]))
#Replacing elephants with their weight
for cycle in cc:
    for idx in range(len(cycle)):
        cycle[idx] = weight_of_elephants[cycle[idx] - 1]

total_sum = 0
#Calculating final effort
for cycle in cc:
    cycle_mass1 = sum(cycle) + (len(cycle) - 2) * min(cycle)
    cycle_mass2 = sum(cycle) + min(cycle) + (len(cycle) + 1) * min_weight
    total_sum += min(cycle_mass1, cycle_mass2)
print(total_sum)