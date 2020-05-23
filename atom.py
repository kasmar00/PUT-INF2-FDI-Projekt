from numpy import array, dot

class atom:
	def __init__(self,x, y, Vx, Vy):
		self.x=x
		self.y=y
		self.Vx=Vx #velocity on x axis in pixels per time quant
		self.Vy=Vy
	
	def move(self):
		self.x+=self.Vx
		self.y+=self.Vy
		return(self.x,self.y)

	def check_collision_boundary(self, bx, by):
		d=1
		if self.x<d or self.x>bx-d:
			self.Vx*=-1
		if self.y<d or self.y>by-d:
			self.Vy*=-1

	def check_collision_others(self, other):
		d=5
		dist=((self.x-other.x)**2+(self.y-other.y)**2)**0.5
		if dist<d:
			self_velocity_parallel=self.__get_projected_vector((other.x, other.y), (self.Vx, self.Vy))
			other_velocity_parallel=other.__get_projected_vector((self.x, self.y), (other.Vx, other.Vy))
			self_velocity_perpendicular=self.__get_projected_vector(self.__get_perp_vector(other), (self.Vx, self.Vy))
			other_velocity_perpendicular=other.__get_projected_vector(other.__get_perp_vector(self), (other.Vx, other.Vy))
			self.Vx, self.Vy=array(self_velocity_perpendicular)+array(other_velocity_parallel)
			other.Vx, other.Vy=array(other_velocity_perpendicular)+array(self_velocity_parallel)
			#self.Vx,other.Vx=other.Vx,self.Vx
			#self.Vy,other.Vy=other.Vy,self.Vy

	def __get_projected_vector(self, o, v):
		ox,oy=o
		x,y=v
		P1=array([ox, oy])
		P2=array([self.x, self.y])
		P3=array([self.x+x, self.y+y])
		P4=((P1-P2)*dot(P3-P2, P1-P2))/(dot(P1-P2, P1-P2))+P2
		snewvx, snewvy=-(P4-P2)
		return(snewvx, snewvy)

	def __get_perp_vector(self, other):
		sx, sy=self.x, self.y
		ox, oy=other.x, other.y
		onx=1+sx
		print(sx, sy, ox, oy)
		ony=((ox-sx)*(onx-sx))/(oy-sy)+sy
		return(onx, ony)



