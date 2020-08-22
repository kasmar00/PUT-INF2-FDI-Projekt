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
from setup import get_args

def main_loop(window, args):
	#setup
	#chwilowo tu zmienne tego typu dam
	#wszystkie te zmienne powinny być zmienialne przez slidery/przyciski
	#czyli main loop musi je chyba dostawać jako argumenty, ale trzeba przemyślec które konkretnie
	num_atoms, atom_radius, kappa, size_mul, maxFrames=args
	virt_h=virt_w=size_mul*atom_radius
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
	testGraph = Graph(CircularList(200),(1100,300),(400,200),200,window)
	testGraph.init_points()
	testGraph.updateGraph()

	#text counters
	textFrames=Text(Point(1300,400), "Klatka: 0/"+str(maxFrames))
	textFrames.draw(window)

	frameCount = 0
	#loop
	while not window.isClosed():
		if frameCount>=maxFrames: #after completeing all frames the sim pauses
			pauseButton.var = True
		start_frametime = time()
		textFrames.setText("Klatka: "+str(frameCount)+"/"+str(maxFrames))
		#graph testing code begin
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
			frameCount+=1
			cache.insert_top(Node(deepcopy(box.atoms)))
			cache_size+=1
			if cache_size > max_cache_size:
				cache.delete_head()
				cache_size-=1
			box.check_collisions()
			box.update_visual_atoms()
			if box.atoms[0].path != [] and box.atoms[0].path[-1][1]==box.atoms[0].x and box.atoms[0].path[-1][2]==box.atoms[0].y and box.atoms[0].path[-1][0] != 0:
				testGraph.cll.entryPoint.next.value = 0
			else: 
				testGraph.cll.entryPoint.next.value = testGraph.cll.entryPoint.value + box.red_velocity()
			testGraph.cll.entryPoint = testGraph.cll.entryPoint.next
			testGraph.updateGraph()
		elif previousButton.var == True:	
			cache_size = step_back(cache,box,cache_size)
			previousButton.var = previousButton.f(previousButton.var)
			frameCount-=1
		elif nextButton.var == True:	
			box.move_atoms()
			frameCount+=1
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
			frameCount-=1
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
	sim_args=get_args()
	#make a window
	main_window = GraphWin(layout_name,layout_screen_w,layout_screen_h,autoflush=False)
	main_window.update()
	main_loop(main_window, sim_args)
	main_window.close()