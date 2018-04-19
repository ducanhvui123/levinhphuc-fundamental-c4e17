from turtle import *
speed(0)
colors = ["red", "purple", "pink", ]
for n in range(3, 120):
    color(colors[(n -3)%3 ]) # lay % thi phan du se k bao gio qua dc 3 :v kieu nhu la neu len den 120 thi k du? mau va no lap lien tuc nha homie
    for i in range(n):
        forward(100)
        left(360/n) #360/5 = 72 trong 1 hinh da giac deu` cach tinh goc: lay 360 do chia cho so canh `
    

mainloop()
