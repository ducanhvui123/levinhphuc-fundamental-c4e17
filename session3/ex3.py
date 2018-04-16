m = int(input("enter your number of row"))
n = int(input("enter your number of collum"))
for i in range(n):
    for j in range(m):
       if (i + j) % 2 == 0:
           print("o", end="")
       else :
           print("*", end="")     
    print()    