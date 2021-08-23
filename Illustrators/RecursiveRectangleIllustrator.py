from Generators import RecursiveRectangle
from tkinter import Tk, Canvas


class RecursiveRectangleIllustrator:
	def __init__(self, rect: RecursiveRectangle):
		self.rect = rect
		self.save_no = 0
		self.window = Tk()
		self.canvas = Canvas(self.window, width=self.rect.get_width(), height=self.rect.get_height())
		self.canvas.pack()
		self.canvas.bind("<Button-1>", self.mouse_click)
		self.draw_img()
		self.run()