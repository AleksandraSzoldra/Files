# zad 16 FILES

num = 0 
with open ("work.txt") as file:
    for line in file:
        num = num +1 
        if num % 5 ==0:
            print(f"{num}.{line}", end= "")
            input("Press ENTER to continue...")
        else:
            print(f"{num}.{line}", end = "") 
        
    