
# creat read update delete
#names = []
#print(names)
#print(type(names))
names = ["canh", "hieu", "duc anh", "Don", "Quan"]
#print(names)
#create
#names.append("Nguyen")
#new_name = "Don"
#names.append(new_name)
#print(names)
#print(names[0])
#for i in range(3):
    #print(names[i])
#for i in range(len(names)):
 #   print(names[i])


#foreach
no = 1
for n in names:
    #print(no,". ", n, sep="")
    #string format
    message = "{0}. {1}.".format(no, n)
    print(message)
    no = no +1 # cung nghia voi no += 1