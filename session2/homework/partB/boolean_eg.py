# boolean is a value that either true or false
# x == y - produce true if ... x is equal to y
# x != y - ... x is not equal to y\
# x > y - ... x is greater than y
# x < y - ... x is smaller than y
# x >= y - ... x is greather than or equal to y
# x <= y - ... x is smaller than or equal to y
# vi du
print("the comparision between 2 person")
a = float(input("enter your first person age"))
b = float(input("enter your second person age"))
if a==b:
    print(bool(a==b))
    print("they have the same age")
if a > b:
    print(bool(a>b))
    print("person 1 is older than person 2")
if a < b:
    print(bool(a<b))
    print("person 2 is older than person 1")