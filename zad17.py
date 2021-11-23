# zad 17 FILES 

f_1 = open("work.txt", "r")
f_2 = open ("blank.txt", "w")

f_2.write(f_1.read()) 

f_1.close()
f_2.close() 

        