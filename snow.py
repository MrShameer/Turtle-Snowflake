import turtle
scr = turtle.Screen()
t=turtle.Turtle()
t.speed(100)
n,stage=150,5
b=5 #ubah branch untuk bentuk lain2
def star(h,s):
	if s>0:
		for i in range(b):
			t.fd(h)
			star(h/2.5,s-1)
			t.bk(h)
			t.rt(360//b)
star(n,stage)
turtle.mainloop()