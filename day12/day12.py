f = open("input.txt", "r")
input = f.readlines()
f.close()

for place,line in enumerate(input):
    input[place]=line.strip()

pos = [0,0]
direction = 0

for i in input:
    com = i[:1]
    val = int(i[1:])
    if com == "N":
        pos[0] += val
    elif com == "S":
        pos[0] -= val
    elif com == "W":
        pos[1]+= val
    elif com == "E":
        pos[1] -= val
    elif com == "R":
        val = val/90
        direction = (direction+val)%4
    elif com == "L":
        val = val / 90
        direction = (direction - val) % 4
    elif com == "F":
        if direction == 0:
            pos[1]-=val
        if direction == 1:
            pos[0]-= val
        if direction == 2:
            pos[1]+= val
        if direction == 3:
            pos[0]+= val

print("Task 1: ",abs(pos[0])+abs(pos[1]))

pos = [0,0]
wp = [1,-10]

for i in input:
    com = i[:1]
    val = int(i[1:])
    if com == "N":
        wp[0] += val
    elif com == "S":
        wp[0] -= val
    elif com == "W":
        wp[1]+= val
    elif com == "E":
        wp[1] -= val
    elif com == "R":
        val = int(val / 90)
        for i in range(0,val):
            tmp=wp[0]
            wp[0]=wp[1]
            wp[1]=-tmp
    elif com == "L":
        val = int(val / 90)
        for i in range(0,val):
            tmp=wp[0]
            wp[0]=-wp[1]
            wp[1]=tmp
    elif com == "F":
        pos[0]+=wp[0]*val
        pos[1]+=wp[1]*val

print("Task 2: ",abs(pos[0])+abs(pos[1]))