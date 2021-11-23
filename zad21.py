# zad 21 FILES

import random

f = open ("numbers21.txt", "w") 
for i in range (1,51):
    f.write(str(random.randrange(100,999)) + "\n")
    
    
f.close()