class Node:
	def __init__(self,value):
		self.value = value
		self.next = None
class List:
	def __init__(self):
		self.head = None
	def insert_top(self,x):
		if self.head == None:
			self.head = x
		else:
			self._insert_top(x)
	def _insert_top(self,x):
		temp = self.head
		while temp.next is not None:
			temp = temp.next
		temp.next = x
	def delete_head(self):
		if self.head.next is not None:
			temp = self.head.next
			self.head = temp
		else:
			self.head = None
	def delete_top(self):
		temp = self.head
		while temp.next.next is not None:
			temp = temp.next
		del(temp.next)
		temp.next = None

def step_back(cache,box,cache_size):
	#delete_top kind of does not like smaller lists and tbh it is kinda useless to
	#implemet an edge case just to get 2 more iterations of caching
	if cache_size > 2:
		temp = cache.head
		while temp.next is not None:
			temp = temp.next
		box.atoms = deepcopy(temp.value)
		box.update_visual_atoms()
		cache.delete_top()
		cache_size -=1
	return cache_size
