 #text = input("Enter your data:").lower()
text = "This is my bullshit things ".lower()
dict={}
for i in text:
    dict[i]=dict.get(i,0)+1
word=list(dict.items())
word.sort()
word.pop(0)
for value in word:
    print(*value,end="\n")