from graphics import *
from layout import *
from box import *
from control import *
from time import sleep
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


def main_loop(window):
	#setup
	#chwilowo tu zmienne tego typu dam
	num_atoms = 100
	scaling_factor = 1
	setup_window(window)
	box = Box(box_offset_w,box_offset_h,box_w,box_h,box_w*scaling_factor,box_h*scaling_factor,1,window)
	box.add_atoms(num_atoms)
	box.display_rect.setWidth(3)
	box.display_rect.draw(window)

	pauseButton = Button(1400,10,100,20,testButtonFunction,False,window)
	pauseButton.rect.setFill("pink")
	#loop
	while not window.isClosed():
		clickPoint = window.checkMouse()
		if clickPoint is not None:
			pauseButton.is_pressed(clickPoint.getX(),clickPoint.getY())
			#later, invoke a global all-button check function
		if pauseButton.var == False:
			box.move_atoms()
			box.check_collisions()
			box.update_visual_atoms()
		window.update()
		sleep(0.01)
	print("done")
if __name__=="__main__":
	#make a window
	main_window = GraphWin(layout_name,layout_screen_w,layout_screen_h,autoflush=False)
	main_window.update()
	main_loop(main_window)
	main_window.close()