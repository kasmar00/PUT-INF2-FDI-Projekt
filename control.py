from graphics import *

class Button:
	def __init__(self,x,y,w,h,func,var,win):
		self.x = x
		self.y = y
		self.w = w 
		self.h = h 
		self.f = func
		self.var = var
		self.rect = Rectangle(Point(x,y),Point(x+w,y+h))
		self.rect.draw(win)
	def is_pressed(self,mouseX,mouseY):
		if(mouseX > self.x and mouseX < self.x+self.w and mouseY > self.y and mouseY < self.y+self.h):
			self.var = self.f(self.var)


def testButtonFunction(state):
	return not state
