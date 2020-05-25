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

def check_and_logic_all(buttons,clickPoint):
	pauseButton = buttons[0]
	previousButton = buttons[1]
	nextButton = buttons[2]
	reverseButton = buttons[3]
	forwardButton = buttons[4]
	pauseButton.is_pressed(clickPoint.getX(),clickPoint.getY())
	previousButton.is_pressed(clickPoint.getX(),clickPoint.getY())
	nextButton.is_pressed(clickPoint.getX(),clickPoint.getY())
	if pauseButton.var == True:
		reverseButton.is_pressed(clickPoint.getX(),clickPoint.getY())
	if pauseButton.var == False:
		forwardButton.is_pressed(clickPoint.getX(),clickPoint.getY())


