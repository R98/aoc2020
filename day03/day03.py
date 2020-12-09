f = open("input.txt", "r")
input = f.readlines()

for place,line in enumerate(input):
    input[place]=line.rstrip()

def slope(right,down):
    i=0
    position=0
    trees=0
    while i < len(input):
        if(input[i][position%len(input[i])]=="#"):
            trees+=1
        position+=right
        i+=down
    return trees
print("Task 1; ", slope(3,1))
print("Task 2: ", slope(1,1)*slope(3,1)*slope(5,1)*slope(7,1)*slope(1,2))



