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
