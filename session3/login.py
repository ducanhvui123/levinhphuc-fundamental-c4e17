from getpass import getpass
while True:
    print("welcome guest")
    login = input("your user name:")
    password = getpass("your password:")

    if login == ("c4e"):
        if password == ("techkid"):
            print("login access")
        if password != ("techkid"):
            print("login failed")  
    else:
        print("login failed")       
        