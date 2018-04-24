trash = {
    "vk": "một loài thú dữ",
    "ck": "chồng",
    "ttt": "thứ mà bọn trẻ đú hay nói",
    "ahihi": "some gay shit",
    "g9": "chúc bé ngủ ngon",
    "lol": "laugh out loud",
    "lmfao": "laugh my fuckin ass out",
}
while True:
    code = input("enter a code: ")
    if code in trash:
        print(trash[code])
    else:
        usr_choice = input("wish to contribute (Y/N?").upper()
        if usr_choice == "Y":
            translation = input("enter your trans:")
            trash[code] = translation
            print(trash)
        else:
            print("Thanks you") 
        # print("don't exist")
        # a = str(input("you want to add your new word (Y/N):"))
        # if a == "Y"
        #     code = str(input("enter your new word: "))
        #     b = str(input("enter your mean:"))



