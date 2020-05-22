class atom:
	def __init__(self,x, y, Vx, Vy):
		self.x=x
		self.y=y
		self.Vx=Vx #velocity on x axis in pixels per time quant
		self.Vy=Vy
	
	def move(self,time):
		self.x+=self.Vx
		self.y+=self.Vy
		return(self.x,self.y)