# zad 18 FILES

f = open ("work.txt", "r")
e = open ("blank2.txt", "w")

for line in f:
    e.write(line)
    
f.close()
e.close()
