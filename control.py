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


class Slider:
	def __init__(self,pos,slen,var,vmin,vmax,win):
		self.x, self.y = pos
		self.len = slen
		self.var = var
		self.vmin = vmin
		self.vmax = vmax
		self.body = Rectangle(Point(self.x,self.y+10),Point(self.x+self.len,self.y+30-10))
		self.body.setFill("grey")
		self.body.draw(win)
		self.wedge = Rectangle(Point(self.x + int(self.len*(self.var/abs(self.vmin-self.vmax)))-5,self.y),
			Point(self.x + int(self.len*(self.var/abs(self.vmin-self.vmax)))+5,self.y+30))
		self.wedge.setFill("orange")
		self.wedge.draw(win)
		self.win = win

	def is_pressed(self,mouseX,mouseY):
		if(mouseX > self.x and mouseX < self.x+self.len and mouseY > self.y and mouseY < self.y+30):
			temp = self.var
			self.var = int((self.vmax-self.vmin)*((mouseX-self.x)/self.len))+self.vmin
			self.wedge.undraw()
			print(self.var)
			self.wedge = Rectangle(Point(self.x + int(self.len*((self.var-self.vmin)/abs(self.vmin-self.vmax)))-5,self.y),
				Point(self.x + int(self.len*((self.var-self.vmin)/abs(self.vmin-self.vmax)))+5,self.y+30))
			self.wedge.setFill("orange")
			self.wedge.draw(self.win)
	
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


