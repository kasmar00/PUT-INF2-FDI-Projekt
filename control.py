from graphics import *
from layout import *
from sys import stderr

class Button:
	def __init__(self,pos,size,func,var,win):
		self.x, self.y = pos
		self.w, self.h= size 
		self.f = func
		self.var = var
		self.role = ""
		self.rect = Rectangle(Point(self.x,self.y),Point(self.x+self.w,self.y+self.h))
		self.symb = Text(Point(self.x+self.w/2,self.y+self.h/2),"")
		self.symb.setSize(8)
		self.rect.draw(win)
		self.symb.draw(win)

	def is_pressed(self,mouseX,mouseY):
		if(mouseX > self.x and mouseX < self.x+self.w and mouseY > self.y and mouseY < self.y+self.h):
			print("Button input: ", self.role, file=stderr)
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
			print("New speed: ", self.var)
			self.wedge = Rectangle(Point(self.x + int(self.len*((self.var-self.vmin)/abs(self.vmin-self.vmax)))-5,self.y),
				Point(self.x + int(self.len*((self.var-self.vmin)/abs(self.vmin-self.vmax)))+5,self.y+30))
			self.wedge.setFill("orange")
			self.wedge.draw(self.win)
	
def testButtonFunction(state):
	return not state

def check_and_logic_all(buttons,clickPoint):
	pauseButton,previousButton,nextButton,reverseButton,forwardButton = buttons
	pauseButton.is_pressed(clickPoint.getX(),clickPoint.getY())
	previousButton.is_pressed(clickPoint.getX(),clickPoint.getY())
	nextButton.is_pressed(clickPoint.getX(),clickPoint.getY())
	if pauseButton.var == True:
		reverseButton.is_pressed(clickPoint.getX(),clickPoint.getY())
	if pauseButton.var == False:
		forwardButton.is_pressed(clickPoint.getX(),clickPoint.getY())

def setup_window(window):
	window.setBackground(color_rgb(188,188,188))
	vert_divider_left = Rectangle(Point(vertical_bar_left_w_offset,0),
		Point(vertical_bar_left_w_offset,layout_screen_h))
	vert_divider_left.setFill("black")
	vert_divider_left.draw(window)
	horz_divider_down = Rectangle(Point(0,horizontal_bar_height_offset),
		Point(vertical_bar_left_w_offset,horizontal_bar_height_offset))
	horz_divider_down.setFill("black")
	horz_divider_down.draw(window)

def setup_buttons(window):
	pauseButton = Button((buttons_origin_point_x,buttons_origin_point_y),(100,20),testButtonFunction,False,window)
	pauseButton.role="Pause toggle"
	pauseButton.rect.setFill("pink")
	pauseButton.symb.setText("||")
	pauseButton.symb.setStyle("bold")
	previousButton = Button((buttons_origin_point_x-40,buttons_origin_point_y),(20,20),testButtonFunction,False,window)
	previousButton.role="Previous frame"
	previousButton.rect.setFill("red")
	previousButton.symb.setText("◀")
	reverseButton = Button((buttons_origin_point_x-80,buttons_origin_point_y),(20,20),testButtonFunction,False,window)
	reverseButton.role="Play backwards"
	reverseButton.rect.setFill("sienna")
	reverseButton.symb.setText("◀◀")
	forwardButton = Button((buttons_origin_point_x+160,buttons_origin_point_y),(20,20),testButtonFunction,False,window)
	forwardButton.role="Play forward"
	forwardButton.rect.setFill("sienna")
	forwardButton.symb.setText("▶▶")
	nextButton = Button((buttons_origin_point_x+120,buttons_origin_point_y),(20,20),testButtonFunction,False,window)
	nextButton.role="Next frame"
	nextButton.rect.setFill("red")
	nextButton.symb.setText("▶")
	buttons = [pauseButton,previousButton,nextButton,reverseButton,forwardButton]
	return buttons