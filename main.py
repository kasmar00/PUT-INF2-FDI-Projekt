from graphics import *
from layout import *
from box import *
from control import *
from time import sleep, time
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
	box.add_red(atom_radius)
	box.add_atoms(num_atoms, atom_radius)
	box.display_rect.setWidth(3)
	box.display_rect.draw(window)
	
	#cache driver code:
	cache_size = 0
	max_cache_size = 500 #does not affect the speed of the simulation while providing a solid buffer imo
	cache = List()
	buttons_origin_point_x = 430
	buttons_origin_point_y = 700
	pauseButton = Button((buttons_origin_point_x,buttons_origin_point_y),(100,20),testButtonFunction,False,window)
	pauseButton.rect.setFill("pink")
	previousButton = Button((buttons_origin_point_x-40,buttons_origin_point_y),(20,20),testButtonFunction,False,window)
	previousButton.rect.setFill("red")
	reverseButton = Button((buttons_origin_point_x-80,buttons_origin_point_y),(20,20),testButtonFunction,False,window)
	reverseButton.rect.setFill("black")
	forwardButton = Button((buttons_origin_point_x+160,buttons_origin_point_y),(20,20),testButtonFunction,False,window)
	forwardButton.rect.setFill("black")
	nextButton = Button((buttons_origin_point_x+120,buttons_origin_point_y),(20,20),testButtonFunction,False,window)
	nextButton.rect.setFill("red")
	buttons = [pauseButton,previousButton,nextButton,reverseButton,forwardButton]
	
	speedSlider = Slider((buttons_origin_point_x-75,buttons_origin_point_y+30),250,75,5,100,window)

	#loop
	while not window.isClosed():
		start_frametime = time()
		clickPoint = window.checkMouse()
		if clickPoint is not None:
			check_and_logic_all(buttons,clickPoint)
			speedSlider.is_pressed(clickPoint.getX(),clickPoint.getY())
			clickPoint = None
		if pauseButton.var == False:
			reverseButton.var = False
			#forwardButton.var = False
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
		end_frametime = time()
		if forwardButton.var == True:	
			pass
		else:
			tsleep = 1/speedSlider.var - (end_frametime - start_frametime)
			if tsleep > 0:
				sleep(tsleep)
	print("done")

if __name__=="__main__":
	#make a window
	main_window = GraphWin(layout_name,layout_screen_w,layout_screen_h,autoflush=False)
	main_window.update()
	main_loop(main_window)
	main_window.close()