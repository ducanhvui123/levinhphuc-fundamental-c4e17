loop = True
wrong_count = 0
while loop: 
    username = input("your user name:")
    password = input("your password:")
    if username != "c4e":
        print("no such user!")
        wrong_count += 1
    elif password != "dkmchau123":
        print("wrong password")
        wrong_count += 1
    else:
        print("login access!!!")
        loop = False
    
    if wrong_count >= 3:
        loop = False
