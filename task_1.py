import linecache

boundary = "boundary"
dimen = "xy"
endel = "endel"
count = 0
boun = []
ende = []

f = open("Format_Source.txt", "r")
f1 = open("output.txt", "a")

# printing hearder
for x in f:
    if boundary in x:
        break
    print(x, file=f1)

f.close()
f = open("Format_Source.txt", "r")

lines = f.readlines()
for k in lines:
    count = count + 1

    if boundary in k:
        count1 = count
        boun.append(count1)

print(*boun, sep=" ")

for i in range(boun[0], boun[2]):
    particular_line = linecache.getline("Format_Source.txt", i)

    # print the particular line
    print(particular_line, file=f1)

f.close()
f = open("Format_Source.txt", "r")

lista = f.readlines()
lista = lista[-2:]

for i in lista:
    print(i, file=f1)

f.close()
f1.close()
