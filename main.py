from graphics import *
from layout import *

def main_loop(window):
	#setup
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
	#loop
	while not window.isClosed():
		window.update()
	print("done")
		
if __name__=="__main__":
	#make a window
	main_window = GraphWin(layout_name,layout_screen_w,layout_screen_h,autoflush=False)
	main_window.update()
	main_loop(main_window)
	main_window.close()