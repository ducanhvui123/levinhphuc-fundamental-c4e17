# python allowed us to have nested conditional, which mean we can put an if statement within an if statement.
#for example
print("How to pass your high school exam in Viet Nam")
score = float(input("enter your score:"))
money = int(input("enter your money: "))
if score > 53:
    print("you pass, you have enough point")
    if money >= 50:
        print("you pass and you have enough money to study")          
    else:
        print("you pass but you don't have enough money to study")
else:
    print("loserrrr")
