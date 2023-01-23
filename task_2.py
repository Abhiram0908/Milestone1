boundary = "boundary"
f = open("Source.txt", "r")
f1 = open("output_1.txt", "a")

# printing header
for x in f:
    if boundary in x:
        break
    print(x, file=f1)

f.close()

# printing footer
f = open("Source.txt", "r")

lista = f.readlines()
lista = lista[-2:]

for i in lista:
    print(i, file=f1)

f.close()

f = open("Source.txt", "r")
lines = f.readlines()
lst = []
for k in lines:
    if "xy" in k:
        lst = k.split()
lst.pop(0)
res = [eval(i) for i in lst]
print("Modified list is: ", res)
for i in lst:
    print(i)
