from random import choice
loop = True
wrong_count = 0
list_of_word = ("python", "yeudieuanh", "dieuanhxinh", "woaini",)
print('''Welcome my homie
this is my stupid game call: Word Jumble
you have to guess my word in wrong order, and you only have ten chance to guess :3''')
text = choice(list_of_word)
character = list(text)
b = sorted(character)
print("my jumble word is:", b, sep="")
while loop:
    player_guess = str(input("your guess is:"))
    if player_guess == text:
        print("bingooo")
        loop = False
    else:
        print("you are wrong")
        wrong_count += 1
    if wrong_count >= 10:
        print("you have run out of chance")
        loop = False
    
# print(character)

# from random import choice
#    # print(choice(character))

# for i in character:
#     print("{0} {1}".format(choice(character), " "))
