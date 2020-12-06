f = open("input.txt", "r")
input = f.readlines()

counter = 0
for x in input:
    x = x[:-1]
    x = x.split(": ")
    pw = x[1]
    min = x[0].split("-")[0]
    max = x[0].split("-")[1].split(" ")[0]
    letter = x[0].split("-")[1].split(" ")[1]


    c = pw.count(letter)
    if (c >= int(min) and c <= int(max)):
        counter+=1

print("Task 1: " ,counter)
counter = 0;

for x in input:
    x = x[:-1]
    x = x.split(": ")
    pw = x[1]
    min = x[0].split("-")[0]
    max = x[0].split("-")[1].split(" ")[0]
    letter = x[0].split("-")[1].split(" ")[1]

    if(pw[int(min)-1]==letter):
        if(pw[int(max)-1]!=letter):
            counter+=1
    elif pw[int(max)-1]==letter:
        counter+=1
print("Task 2: ",counter)
