f = open("input.txt", "r")
input = f.read()
f.close()

input = input.split("\n\n")

task1 = 0
task2 = 0
for x in input:
    x.replace("\n", "")
    i = ''.join(set(x))
    task1+= len(i)

print("Task 1: " + str(task1))

for x in input:
    a = ""
    y=x.split("\n")

    for z in y[0]:
        a+=z
        for line in y:
            if z not in line:
                a=a.replace(z,"")
    task2+= len(a)
print("Task 2: "+str(task2))





