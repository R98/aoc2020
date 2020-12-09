import re
f = open("input.txt", "r")
input = f.readlines()
f.close()

for place,line in enumerate(input):
    input[place]=line.rstrip().replace("bags","bag")

r= re.compile("\w+\s\w+\sbag")
ra = re.compile("(\d)\s\w+\s\w+\sbag")

cancontain = []
length = -1
while len(cancontain) != length:
    length = len(cancontain)
    for x in input:
        x = x.split(" contain")
        if x[0] not in cancontain:
            if "shiny gold bag" in x[1]:
                cancontain.append(x[0])
            else:
                for y in r.findall(x[1]):
                    if y in cancontain:
                        cancontain.append(x[0])
                        break

print("Task 1: ", len(cancontain))
inside=[]
l=-1
for x in input:
    x = x.split(" contain")
    if "shiny gold bag" in x[0]:
        for y in zip(ra.findall(x[1]),r.findall(x[1])):
            inside.append((x[0],*y))

while len(inside) != l:
    l= len(inside)
    for x in input:
        x = x.split(" contain")
        if [item for item in inside if item[2] == x[0]]:
            for y in zip(ra.findall(x[1]),r.findall(x[1])):
                if (x[0],*y) not in inside:
                    inside.append((x[0],*y))
                else:
                    break

total = 0
def countbags(colour):
    if [item for item in inside if item[0] == colour]:
        t=1
        for i in [item for item in inside if item[0] == colour]:
            t+=int(i[1])*countbags(i[2])
        return t
    else:
        return 1

print("Task 2: ",countbags("shiny gold bag")-1)
