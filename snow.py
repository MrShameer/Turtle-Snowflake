import turtle
scr = turtle.Screen()
t=turtle.Turtle()
t.speed(10)
n,stage=150,4
def star(h,s):
	if s>0:
		for i in range(5):
			t.fd(h)
			star(h/2.5,s-1)
			t.bk(h)
			t.rt(360//5)
star(n,stage)
turtle.mainloop()