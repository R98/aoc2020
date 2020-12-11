f = open("input.txt", "r")
input = f.readlines()
f.close()

for place,line in enumerate(input):
    input[place]=line.rstrip()

def seats(inp):
    output = []
    for i in range(len(inp)):
        output.append("")
        for j in range(len(inp[i])):
            count = 0

            leni = len(input)
            lenj = len(input[i])
            if i-1>=0:
                if j-1>=0 :
                    if inp[i-1][j-1]=="#":count+=1
            if i-1>=0:
                if inp[i-1][j]=="#":count+=1
            if i-1>=0:
                if j+1<lenj:
                    if inp[i-1][j+1]=="#":count+=1
            if j-1>=0:
                if inp[i][j-1]=="#":count+=1
            if j+1<lenj:
                if inp[i][j+1]=="#":count+=1
            if i+1<leni:
                if j-1>=0:
                    if inp[i+1][j-1]=="#":count+=1
            if i+1<leni:
                if inp[i + 1][j] == "#": count += 1
                if j+1<lenj:
                    if inp[i+1][j+1]=="#":count+=1

            if inp[i][j] == "L" and count ==0:
                output[i]+="#"
            elif inp[i][j] == ".":
                output[i]+="."
            elif inp[i][j]== "#" and count < 4:
                output[i]+="#"
            else:
                output[i]+="L"
    return output

next = seats(input)

while next != seats(next):
    next = seats(next)

task1=0
for n in next:
    task1+=n.count("#")
print("Task 1: ",task1)

def seats2(inp):
    output = []
    for i in range(len(inp)):
        output.append("")
        for j in range(len(inp[i])):
            count = 0

            leni = len(input)
            lenj = len(input[i])
            ii = i
            jj = j

            while i-1>=0 and j-1>=0 :
                x=inp[i-1][j-1]
                if x=="#":
                    count+=1
                    break
                elif x == "L":
                    break
                else:
                    i-=1
                    j-=1
            j=jj
            i=ii
            while i-1>=0:
                x=inp[i-1][j]
                if x=="#":
                    count += 1
                    break
                elif x == "L":
                    break
                else:
                    i -= 1
            j = jj
            i = ii
            while i-1>=0 and j+1<lenj:
                x=inp[i-1][j+1]
                if x=="#":
                    count += 1
                    break
                elif x == "L":
                    break
                else:
                    i -= 1
                    j += 1
            j = jj
            i = ii
            while j-1>=0:
                x=inp[i][j-1]
                if x=="#":
                    count += 1
                    break
                elif x == "L":
                    break
                else:
                    j -= 1
            j = jj
            i = ii
            while j+1<lenj:
                x=inp[i][j+1]
                if x=="#":
                    count += 1
                    break
                elif x == "L":
                    break
                else:
                    j += 1
            j = jj
            i = ii
            while i+1<leni and j-1>=0:
                x=inp[i+1][j-1]
                if x=="#":
                    count += 1
                    break
                elif x == "L":
                    break
                else:
                    i += 1
                    j -= 1
            j = jj
            i = ii
            while i+1<leni:
                x=inp[i + 1][j]
                if x == "#":
                    count += 1
                    break
                elif x == "L":
                    break
                else:
                    i += 1
            j = jj
            i = ii
            while i+1<leni and j+1<lenj:
                x=inp[i+1][j+1]
                if x=="#":
                    count += 1
                    break
                elif x == "L":
                    break
                else:
                    i += 1
                    j += 1
            j = jj
            i = ii

            if inp[i][j] == "L" and count ==0:
                output[i]+="#"
            elif inp[i][j] == ".":
                output[i]+="."
            elif inp[i][j]== "#" and count < 5:
                output[i]+="#"
            else:
                output[i]+="L"
    return output

next=seats2(input)

while next != seats2(next):
    next = seats2(next)

task2=0
for n in next:
    task2+=n.count("#")
print("Task 2: ",task2)