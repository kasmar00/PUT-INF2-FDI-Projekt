from graphics import *
from layout import *
from box import *
from control import *
from graph import *
from time import sleep, time
from cache import *
from copy import deepcopy
from math import log
from export import export_red_collisions

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
	buttons = setup_buttons(window)
	pauseButton,previousButton,nextButton,reverseButton,forwardButton = buttons

	speedSlider = Slider((buttons_origin_point_x-75,buttons_origin_point_y+30),250,75,5,100,window)

	#graph init test code
	testGraph = Graph(CircularList(100),(1000,200),(250,100),10,window)
	testGraph.init_points()
	it = testGraph.cll.entryPoint
	for i in range(100):
		it.value = 0
		it = it.next
	testGraph.updateGraph()

	frameCount = 0
	#loop
	while not window.isClosed():
		frameCount+=1
		start_frametime = time()
		#graph testing code begin
		if frameCount%10 == 0:
			testGraph.cll.entryPoint.value = testGraph.cll.entryPoint.next.value + 1
			testGraph.cll.entryPoint = testGraph.cll.entryPoint.next
			testGraph.updateGraph()
		#graph testing code end
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
	export_red_collisions(box.atoms[0].path)
	print("done")

if __name__=="__main__":
	#make a window
	main_window = GraphWin(layout_name,layout_screen_w,layout_screen_h,autoflush=False)
	main_window.update()
	main_loop(main_window)
	main_window.close()