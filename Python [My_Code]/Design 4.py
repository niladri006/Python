import turtle
t=turtle.Turtle()
turtle.bgcolor("Black")
t.speed(0)
temp=1
clrlist=["red","green","blue"]
for i in range(1000):
    t.color(clrlist[i%3])
    t.forward(temp)
    t.left(120)
    t.left(1)
    temp+=1
turtle.mainloop()