favs = ["teaching", "coding", "bla"]
print("Hi, favs:"")
print(*favs, sep=", " )
new_fav = input("enter your new fav:")
favs.append(new_fav)
print(favs)