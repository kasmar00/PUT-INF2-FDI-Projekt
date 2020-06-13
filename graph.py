from cache import Node
from graphics import *
class CircularList:
	def __init__(self,size):
		self.size = size
		self.origin0 = Node(None)
		temp = self.origin0
		for i in range(size-1):
			temp.next = Node(None)
			temp = temp.next
		temp.value = 1
		temp.next = self.origin0
		self.entryPoint = self.origin0

#cll is circular linked list, named the class CircularList and run out of good names to remember, sry

#yeah, origin point is in bottom-left because math reasons and my lack of brain, shhhh
class Graph:
	def __init__(self,cll,origin,dim,init_max_value,window):
		self.cll = cll 
		self.window = window
		self.w,self.h = dim
		self.x,self.y = origin
		self.xAxis = Line(Point(self.x,self.y),Point(self.x+self.w,self.y))
		self.xAxis.draw(self.window)
		self.yAxis = Line(Point(self.x,self.y),Point(self.x,self.y-self.h))
		self.yAxis.draw(self.window)
		self.points = []
		self.maxValue = init_max_value
	def init_points(self):
		step = (self.w / self.cll.size)
		for i in range(self.cll.size):
			self.points.append(Circle(Point(self.x+step*i,self.y),1))
			self.points[self.points.__len__()-1].setFill("red")
			self.points[self.points.__len__()-1].setOutline("red")
			self.points[self.points.__len__()-1].draw(self.window)
	def updateGraph(self):
		temp = self.cll.entryPoint
		step = (self.w / self.cll.size)
		for i in range(self.cll.size):
			#self.points[i].move(0,-((self.points[i].getCenter().getY()-self.y-self.h)+((self.h*((temp.value-(self.points[i].getCenter().getY()-self.y-self.h)*self.maxValue/self.h)/self.maxValue)))))
			self.points[i].undraw()
			self.points[i] = Circle(Point(self.x+step*i,self.y-(self.h*(temp.value/self.maxValue))),1)
			self.points[i].setFill("red")
			self.points[i].setOutline("red")
			self.points[i].draw(self.window)
			temp = temp.next
			
if __name__=="__main__":
	ls = CircularList(10)
	it = ls.entryPoint
	for i in range(10):
		it.value = i
		it = it.next
	for i in range(10):
		print(it.value)
		it = it.next
