f = open("Format_Source.txt", "r")
Find = 'boundary'
dimen = 'xy'
endel = 'endel'
count = 0

# Printing header part
for x in f:
    if Find in x:
        print(x)
        break

            
for x in f:
    print(x)
    if endel in x: 
        break

