from graphics import *
from layout import *
from box import *
from control import *
from time import sleep
from cache import *
from copy import deepcopy

def setup_window(window):
	window.setBackground(color_rgb(188,188,188))
	vert_divider_right = Rectangle(Point(vetical_bar_right_w_offset,0),
		Point(vetical_bar_right_w_offset,layout_screen_h))
	vert_divider_right.setFill("black")
	vert_divider_right.draw(window)
	vert_divider_left = Rectangle(Point(vertical_bar_left_w_offset,0),
		Point(vertical_bar_left_w_offset,layout_screen_h))
	vert_divider_left.setFill("black")
	vert_divider_left.draw(window)
	horz_divider_down = Rectangle(Point(0,horizontal_bar_height_offset),
		Point(vertical_bar_left_w_offset,horizontal_bar_height_offset))
	horz_divider_down.setFill("black")
	horz_divider_down.draw(window)

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

def main_loop(window):
	#setup
	#chwilowo tu zmienne tego typu dam
	#wszystkie te zmienne powinny być zmienialne przez slidery/przyciski
	#czyli main loop musi je chyba dostawać jako argumenty, ale trzeba przemyślec które konkretnie
	num_atoms = 100
	atom_radius = 1
	kappa = 5
	virt_h, virt_w=100, 200
	scaling_factor=max(virt_h/box_h, virt_w/box_w)
	box_offset_w_centered=box_offset_w+(box_w-virt_w/scaling_factor)/2
	box_offset_h_centered=box_offset_h+(box_h-virt_h/scaling_factor)/2
	setup_window(window)
	box = Box((box_offset_w_centered,box_offset_h_centered),scaling_factor,(virt_w,virt_h),kappa,window)
	box.add_atoms(num_atoms, atom_radius)
	box.display_rect.setWidth(3)
	box.display_rect.draw(window)
	
	#cache driver code:
	cache_size = 0
	max_cache_size = 500 #does not affect the speed of the simulation while providing a solid buffer imo
	cache = List()

	pauseButton = Button((1400,10),(100,20),testButtonFunction,False,window)
	pauseButton.rect.setFill("pink")
	previousButton = Button((1360,10),(20,20),testButtonFunction,False,window)
	previousButton.rect.setFill("red")
	reverseButton = Button((1320,10),(20,20),testButtonFunction,False,window)
	reverseButton.rect.setFill("black")
	forwardButton = Button((1560,10),(20,20),testButtonFunction,False,window)
	forwardButton.rect.setFill("black")
	nextButton = Button((1520,10),(20,20),testButtonFunction,False,window)
	nextButton.rect.setFill("red")
	buttons = [pauseButton,previousButton,nextButton,reverseButton,forwardButton]
	#loop
	while not window.isClosed():
		clickPoint = window.checkMouse()
		if clickPoint is not None:
			check_and_logic_all(buttons,clickPoint)
			clickPoint = None
		if pauseButton.var == False:
			reverseButton.var = False
			forwardButton.var = False
			box.move_atoms()
			cache.insert_top(Node(deepcopy(box.atoms)))
			cache_size+=1
			if cache_size > max_cache_size:
				cache.delete_head()
				cache_size-=1
			box.check_collisions()
			box.update_visual_atoms()
		elif previousButton.var == True:	
			cache_size = step_back(cache,box,cache_size)
			previousButton.var = previousButton.f(previousButton.var)
		elif nextButton.var == True:	
			box.move_atoms()
			cache.insert_top(Node(deepcopy(box.atoms)))
			cache_size+=1
			if cache_size > max_cache_size:
				cache.delete_head()
				cache_size-=1
			box.check_collisions()
			box.update_visual_atoms()
			nextButton.var = nextButton.f(nextButton.var)
		elif reverseButton.var == True:	
			cache_size = step_back(cache,box,cache_size)
		window.update()
		if forwardButton.var == True:	
			pass
		else:
			sleep(0.01)
	print("done")

if __name__=="__main__":
	#make a window
	main_window = GraphWin(layout_name,layout_screen_w,layout_screen_h,autoflush=False)
	main_window.update()
	main_loop(main_window)
	main_window.close()