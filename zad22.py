# zad 22 FILES

f = open("powers.txt", "w")
for i in range (1,11):
    f.write(str(i)+ "," + str(i*i) + "," + str(i**3) + "\n") 
    
f.close()