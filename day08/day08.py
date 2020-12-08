f = open("input.txt", "r")
input = f.readlines()
f.close()

for place,line in enumerate(input):
    input[place]=line.rstrip()

accumulator = 0
i=0
visited=[]

while i<len(input):
    if i in visited:
        break
    visited.append(i)
    if input[i][:3] == "jmp":
        i+=int(input[i][5:]) if input[i][4:5] == "+" else -int(input[i][5:])
    else:
        if input[i][:3] == "acc":
            accumulator += int(input[i][5:]) if input[i][4:5] == "+" else -int(input[i][5:])
        i+=1
print("Task 1: ", accumulator)

changed = []
terminated = False
j = 0

while j<len(input):
    if (input[j][:3] == "jmp" or input[j][:3] == "nop") and j not in changed:
        changed.append(j)
        input[j] = "nop" + input[j][3:] if input[j][:3] == "jmp" else "jmp" + input[j][3:]
        terminated = True
        accumulator = 0
        i = 0
        visited = []
        while i<len(input):
            if i in visited:
                terminated = False
                input[j] = "nop" + input[j][3:] if input[j][:3] == "jmp" else "jmp" + input[j][3:]
                break
            visited.append(i)
            if input[i][:3] == "jmp":
                i+=int(input[i][5:]) if input[i][4:5] == "+" else -int(input[i][5:])
            else:
                if input[i][:3] == "acc":
                    accumulator += int(input[i][5:]) if input[i][4:5] == "+" else -int(input[i][5:])
                i+=1
    if terminated:
        break
    j+=1

print("Task 2: ", accumulator)


