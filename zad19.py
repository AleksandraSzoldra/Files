# zad 19 FILES

f = open("MeatAndFish.txt", "r")
e = open ("GrainsAndBread.txt", "r")
g = open("shopping_list.txt", "w+")


g.write(f.read() + "\n")
g.write(e.read())

print(g.read())
f.close()
g.close()
e.close() 