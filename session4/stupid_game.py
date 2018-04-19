from random import *
loop = True
wrong_count = 0
n = randint(1, 100)
print("this is my stupid game call guess my fuckin numbers, you have 8 chance to guess")
while loop:
    m = int(input("guess my number?"))
    if m == n:
        print("bingo")
        loop = False
    elif m > n: 
        print("Too big")
        wrong_count += 1
    else:
        print("too small")
        wrong_count += 1
        
    if wrong_count >= 8:
        print("you run out of chance!!")
        loop = False
    
    
