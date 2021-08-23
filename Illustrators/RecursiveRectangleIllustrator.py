from Generators import RecursiveRectangle
from tkinter import Tk, Canvas
import random


class RecursiveRectangleIllustrator:
	def __init__(self, rect: RecursiveRectangle):
		self.rect = rect
		self.save_no = 0
		self.window = Tk()
		self.canvas = Canvas(self.window, width=self.rect.get_width(), height=self.rect.get_height())
		self.canvas.pack()
		# self.canvas.bind("<Button-1>", self.mouse_click)
		self.draw_img()
		self.run()

	def run(self):
		self.window.mainloop()

	def draw_img(self):
		rects = self.rect.collect_rects()
		for rect in rects:
			self.canvas.create_rectangle(rect.x - rect.half_width, rect.y - rect.half_height,
										rect.x + rect.half_width, rect.y + rect.half_height,
										fill=rect.color, width=random.randint(rect.bar_width_lower, rect.bar_width_upper))