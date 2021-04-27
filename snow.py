import turtle
scr = turtle.Screen()
t=turtle.Turtle()
t.speed(10)
n,stage=150,4 #ubah stage untuk bentuk
def star(h,s):
	if s>0:
		for i in range(stage):
			t.fd(h)
			star(h/2.5,s-1)
			t.bk(h)
			t.rt(360//stage)
star(n,stage)
turtle.mainloop()