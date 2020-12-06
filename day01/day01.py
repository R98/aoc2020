f = open("input.txt", "r")
input = f.readlines()
f.close()
try:
    for x in input:
        for y in input:
            if int(x)+int(y)==2020:
                print("Task 1: " ,int(x)*int(y))
                raise StopIteration
except StopIteration: pass

try:
    for x in input:
      for y in input:
          for z in input:
            if int(x)+int(y)+int(z)==2020:
              print("Task 2: ",int(x)*int(y)*int(z))
              raise StopIteration
except StopIteration: pass