from numpy import array, dot

class atom:
	def __init__(self, position, velocity, radius):
		self.x, self.y=position
		self.Vx, self.Vy=velocity #velocity on x axis in pixels per time quant
		self.radius=radius
	
	def move(self):
		self.x+=self.Vx
		self.y+=self.Vy
		return(self.x,self.y)

	def check_collision_boundary(self, box_size):
		bx,by=box_size
		epsilon=0.1*self.radius #tollerance for collisions, maybe this could be moved elsewhere, maybe it should deppend on kappa
		d=self.radius+epsilon
		if self.x<d or self.x>bx-d:
			self.Vx*=-1
		if self.y<d or self.y>by-d:
			self.Vy*=-1

	def check_collision_others(self, other):
		epsilon=0.1*(self.radius+other.radius) #tollerance for collisions, maybe this could be moved elsewhere, maybe it should deppend on kappa
		d=self.radius+other.radius+epsilon
		dist=((self.x-other.x)**2+(self.y-other.y)**2)**0.5
		if dist<d:
			self_velocity_parallel=self.__get_projected_vector((other.x, other.y), (self.Vx, self.Vy))
			other_velocity_parallel=other.__get_projected_vector((self.x, self.y), (other.Vx, other.Vy))
			self_velocity_perpendicular=self.__get_projected_vector(self.__get_perp_vector(other), (self.Vx, self.Vy))
			other_velocity_perpendicular=other.__get_projected_vector(other.__get_perp_vector(self), (other.Vx, other.Vy))
			#print(self_velocity_parallel, self_velocity_perpendicular, other_velocity_parallel, other_velocity_perpendicular)
			self.Vx, self.Vy=array(self_velocity_perpendicular)+array(other_velocity_parallel)
			other.Vx, other.Vy=array(other_velocity_perpendicular)+array(self_velocity_parallel)
			#print(self.Vx, self.Vy, other.Vx, other.Vy)

	def __get_projected_vector(self, o, v):
		x=array((self.Vx, self.Vy))
		y=array(o)-array((self.x, self.y))
		newV=y * dot(x, y) / dot(y, y) #this is for projecting vector x onto vector y
		return(newV)

	def __get_perp_vector(self, other):
		sx, sy=self.x, self.y
		ox, oy=other.x, other.y
		ox-=sx
		oy-=sy
		onx=-oy+sx
		ony=ox+sy
		return(onx, ony)



