# zad 15 FILES

file_name = str(input("File name: "))
quantity = 0

with open (f"{file_name}.txt") as file:
    for line in file:
        quantity +=1
    print (f"Number of lines: {quantity}")
    
