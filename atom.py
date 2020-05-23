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
			"""
			#self
			P1=array([other.x, other.y])
			P2=array([self.x, self.y])
			P3=array([self.x+self.Vx, self.y+self.Vy])
			#print(P1,P2,P3)
			P4=((P1-P2)*dot(P3-P2, P1-P2))/(dot(P1-P2, P1-P2))+P2
			#print(P4)
			snewvx, snewvy=-(P4-P2)
			#other
			P1=array([self.x, self.y])
			P2=array([other.x, other.y])
			P3=array([other.x+other.Vx, other.y+other.Vy])
			#print(P1,P2,P3)
			P4=((P1-P2)*dot(P3-P2, P1-P2))/(dot(P1-P2, P1-P2))+P2
			#print(P4)
			onewvx, onewvy=-(P4-P2)
			self.Vx=onewvx
			self.Vy=onewvy
			other.Vx=snewvx
			other.Vy=snewvy
			"""
			self.Vx,other.Vx=other.Vx,self.Vx
			self.Vy,other.Vy=other.Vy,self.Vy


