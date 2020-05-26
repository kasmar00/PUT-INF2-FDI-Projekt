from graphics import *

class Button:
	def __init__(self,pos,size,func,var,win):
		self.x, self.y = pos
		self.w, self.h= size 
		self.f = func
		self.var = var
		self.rect = Rectangle(Point(self.x,self.y),Point(self.x+self.w,self.y+self.h))
		self.rect.draw(win)

	def is_pressed(self,mouseX,mouseY):
		if(mouseX > self.x and mouseX < self.x+self.w and mouseY > self.y and mouseY < self.y+self.h):
			self.var = self.f(self.var)


def testButtonFunction(state):
	return not state
