from graphics import *
from atom import atom
from random import random, randint

class Box:
	def __init__(self,posX,posY,w,h,virt_w,virt_h,kappa,window):
		self.posX = posX
		self.posY = posY
		self.w = w
		self.h = h
		self.virt_w = virt_w
		self.virt_h = virt_h
		self.display_rect = Rectangle(Point(posX,posY),Point(posX+w,posY+h))
		self.atoms=[]
		self.visual_atoms = []
		self.kappa=kappa
		self.window = window
		self.bbox=Rectangle(Point(posX,posY), Point(posX+w, posY+h)) #a temporary bbox
		self.bbox.draw(window)
		
	#P R Z Y P A D E K	S Z C Z E G Ó L N Y
	def add_atoms(self, n):
		V=1/self.kappa
		for _ in range(n):
			x=randint(0, self.virt_w)
			y=randint(0, self.virt_h)
			Vx=(random()*2-1)*V
			Vy=(random()*2-1)*V
			self.atoms.append(atom(x, y, Vx, Vy))
			self.visual_atoms.append(Circle(Point(self.translate_horz_coordinate(x), self.translate_vert_coordinate(y)),5))
			self.visual_atoms[-1].setFill("blue")
			self.visual_atoms[-1].draw(self.window)

	def translate_vert_coordinate(self,coord):
		return self.posY+int(abs(coord-self.virt_h)*(self.h/self.virt_h))

	def translate_horz_coordinate(self,coord):
		return self.posX+int(coord*(self.w/self.virt_w))
	
	def move_atoms(self):
		for i in range(len(self.atoms)):
			self.atoms[i].move()	
	
	def check_collisions(self):
		for i in self.atoms:
			i.check_collision_boundary(self.virt_w, self.virt_h)
	
	def update_visual_atoms(self):
		for i in range(len(self.atoms)):
			pos=self.visual_atoms[i].getCenter()
			self.visual_atoms[i].move(self.translate_horz_coordinate(self.atoms[i].x)-pos.getX(),
				self.translate_vert_coordinate(self.atoms[i].y)-pos.getY())
