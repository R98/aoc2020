f = open("input.txt", "r")
input = f.readlines()
f.close()

for place,line in enumerate(input):
    input[place]=int(line.rstrip())

i=25
while i<len(input):
    possible = False
    try:
        for x in input[i-25:i]:
            for y in input[i - 25:i]:
                if x != y:
                    if x+y==input[i]:
                        possible = True
                        raise StopIteration
    except StopIteration:
        pass
    if not possible:
        break
    i+=1

print("Task 1: ",input[i])

for j in range(i):
    x=0
    for y in range(j,i):
        x+=input[y]
        if(x>input[i]):
            break
        if(x==input[i]):
            print("Task 2: ",min(input[j:y])+max(input[j:y]))