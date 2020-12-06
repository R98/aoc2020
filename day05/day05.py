f = open("input.txt", "r")
input = f.readlines()
f.close()

for place,line in enumerate(input):
    input[place]=line.rstrip().replace("L","0").replace("F","0").replace("B","1").replace("R","1")

id = 0
seatlist = []
lowest = 0
for x in input:
    row = int(x[:-3],2)
    column = int(x[-3:],2)
    i = row*8+column
    if i > id:
        id = i
    seatlist.append(i)
    if i < lowest or not lowest:
        lowest = i
print("Task 1: ",id)

j=1
for s in seatlist:
    if lowest + j not in seatlist:
        print("Task 2: ",lowest+j)
    j+=1

