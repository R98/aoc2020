f = open("input.txt", "r")
input = f.readlines()
f.close()

for place,line in enumerate(input):
    input[place]=int(line.rstrip())

highest = max(input)
input.extend((0,highest+3))
input.sort()
def task1(start, ones, threes):
    if start == highest:
        threes+=1
        return ones*threes
    if start+1 in input:
        return task1(start + 1, ones + 1, threes)
    elif start+2 in input:
        return task1(start + 2, ones, threes)
    else:
        return task1(start + 3, ones, threes + 1)
print("Task 1: ", task1(0, 0, 0))

def get_possibilities(i):
    if i == 0:
        return 0
    if i < 3:
        return 1
    possibilities = 0
    possibilities += get_possibilities(i - 1)
    possibilities += get_possibilities(i - 2)
    possibilities += get_possibilities(i - 3)
    return possibilities

def task2(input):
    start = 0
    prev = 0
    p = 1
    for i in range(len(input)):
        x = input[i]
        if prev + 3 == x:
            p *= get_possibilities(i-start)
            start = i
        prev = input[i]
    return  p

print("Task 2: ",task2(input))