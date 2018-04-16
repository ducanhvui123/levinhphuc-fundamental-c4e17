items = ["t-shirt", "sweeter"]
while True:
    a = input("Welcome to our shop, what you need (C,R,U,D):")
    if a == "C":
        b = input("enter your new items:")
        items.append(b)
        print(items, sep=", ")
    elif a == "R":
        print(items, sep=", ")
    elif a == "U":
        c = int(input("Enter your position of an item that you want to replace"))
        new_item = input("enter your new item:")
        items[c - 1] = new_item
        print(items, sep=", ")
    elif a == "D":
        c = int(input("Enter the position of an item that you want to delete"))
        del items[c - 1]
        print(items, sep=", ")
    else:
        print("Lam deoo co cai do m bi mu` a :v")

