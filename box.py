from graphics import *
from atom import atom, red_atom, point_distance
from random import random, randint, choice

class Box:
	free_places=[]

	def __init__(self,position,scaling_factor,virtual_size,kappa,window):
		self.posX, self.posY = position
		self.scaling_factor = scaling_factor
		self.virt_w, self.virt_h = virtual_size
		self.w, self.h = self.virt_w/self.scaling_factor, self.virt_h/self.scaling_factor
		self.display_rect = Rectangle(Point(*position),Point(*sum_pair(position, (self.w, self.h))))
		self.atoms=[]
		self.visual_atoms = []
		self.kappa=kappa
		self.window = window

	def add_atoms(self, n, radius):
		V=1/self.kappa
		self.generate_spawn_array(radius)
		for _ in range(n):
			x, y=choice(self.free_places)
			Vx=(random()*2-1)*V
			Vy=(random()*2-1)*V
			self.atoms.append(atom((x, y), (Vx, Vy), radius))
			self.visual_atoms.append(Circle(Point(self.translate_horz_coordinate(x), self.translate_vert_coordinate(y)),radius/self.scaling_factor))
			self.visual_atoms[-1].setFill("blue")
			self.visual_atoms[-1].draw(self.window)
			self.remove_from_spawn_array(self.atoms[-1])

	def add_red(self, radius): #mainly coppied form add_atoms
		V=1/self.kappa
		x=radius+1
		y=radius+1
		Vx=(random()*2-1)*V
		Vy=(random()*2-1)*V
		self.atoms.append(red_atom((x, y), (Vx, Vy), radius))
		self.visual_atoms.append(Circle(Point(self.translate_horz_coordinate(x), self.translate_vert_coordinate(y)),radius/self.scaling_factor))
		self.visual_atoms[-1].setFill("red")
		self.visual_atoms[-1].draw(self.window)
		self.remove_from_spawn_array(self.atoms[-1])

	def generate_spawn_array(self, radius):
		self.free_places=[]
		for i in range(radius+2,self.virt_w-radius-1):
			for j in range(radius+2,self.virt_h-radius-1):
				self.free_places.append((i, j))
		for i in self.atoms:
			self.remove_from_spawn_array(i)

	def remove_from_spawn_array(self, at):
		i=0
		while i<len(self.free_places):
			if point_distance((at.x, at.y), self.free_places[i])<=2.1*at.radius:
				self.free_places.pop(i)
			else:
				i+=1

	def translate_vert_coordinate(self,coord):
		return self.posY+int(abs(coord-self.virt_h)*(self.h/self.virt_h))

	def translate_horz_coordinate(self,coord):
		return self.posX+int(coord*(self.w/self.virt_w))
	
	def move_atoms(self):
		for i in range(len(self.atoms)):
			self.atoms[i].move()	
	
	def check_collisions(self):
		for i in range(len(self.atoms)):
			self.atoms[i].check_collision_boundary((self.virt_w, self.virt_h))
			for j in range(i+1, len(self.atoms)):
				self.atoms[i].check_collision_others(self.atoms[j])
	
	def update_visual_atoms(self):
		for i in range(len(self.atoms)):
			pos=self.visual_atoms[i].getCenter()
			self.visual_atoms[i].move(self.translate_horz_coordinate(self.atoms[i].x)-pos.getX(),
				self.translate_vert_coordinate(self.atoms[i].y)-pos.getY())

	def red_velocity(self):
		return (self.atoms[0].Vx**2+self.atoms[0].Vy**2)**0.5

def sum_pair(a,b): 
	return(a[0]+b[0], a[1]+b[1])