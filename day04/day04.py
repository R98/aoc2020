import re
f = open("input.txt", "r")
input = f.read().split("\n\n")

counter=0
byr = "byr";iyr = "iyr";eyr = "eyr";hgt = "hgt";hcl = "hcl";ecl = "ecl";pid = "pid";cid = "cid"
musthave = [byr,iyr,eyr,hgt,hcl,ecl,pid]
for i in input:
    if all(x in i for x in(musthave)):
        counter+=1
print("Task 1: ",counter)

counter = 0
c = 0
for i in input:
    try:
        if int(re.findall("byr:(\d{4}\\b)",i)[0]) in range(1920,2003):
            if int(re.findall("iyr:(\d{4}\\b)",i)[0]) in range(2010,2021):
                if int(re.findall("eyr:(\d{4}\\b)",i)[0]) in range(2020,2031):
                    if re.findall("ecl:(\w{3})\\b",i)[0] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                        if re.findall("hcl:#([a-f0-9]{6})\\b",i):
                           if re.findall("pid:(\d{9})\\b",i):
                              try:
                                if int(re.findall("hgt:(\d{3})cm\\b",i)[0]) in range(150,194):
                                    counter += 1
                              except:
                                if int(re.findall("hgt:(\d{2})in\\b",i)[0]) in range(59,77):
                                    counter += 1
    except:
        pass

print("Task 2: ", counter)


