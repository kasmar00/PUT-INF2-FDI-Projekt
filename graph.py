from cache import Node
from graphics import *
class CircularList: #circular linked list
	def __init__(self,size):
		self.size = size
		self.origin0 = Node(0)
		temp = self.origin0
		for i in range(size-1):
			temp.next = Node(0)
			temp = temp.next
		temp.value = 1
		temp.next = self.origin0
		self.entryPoint = self.origin0

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
			self.points[i].undraw()
			self.points[i] = Circle(Point(self.x+step*i,self.y-(self.h*(temp.value/self.maxValue))),1)
			self.points[i].setFill("red")
			self.points[i].setOutline("red")
			if temp.value != 0:
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