from graphics import *

class Box:
	def __init__(self,posX,posY,w,h,virt_w,virt_h):
		self.posX = posX
		self.posY = posY
		self.w = w
		self.h = h
		self.virt_w = virt_w
		self.virt_h = virt_h
		self.rect = Rectangle(Point(posX,posY),Point(posX+w,posY+h))