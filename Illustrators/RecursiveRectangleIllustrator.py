from Structures.RecursiveRectangle import RecursiveRectangle
from tkinter import Tk, Canvas
import random
from PIL import Image


class RecursiveRectangleIllustrator:
	def __init__(self, rect: RecursiveRectangle):
		""" init function for a Illustrator for recursive rectangles

		:param rect: Rectangle to draw
		:type rect: RecursiveRectangle
		"""
		self.rect = rect
		self.save_no = 0
		self.window = Tk()
		self.canvas = Canvas(self.window, width=self.rect.get_width(), height=self.rect.get_height())
		self.canvas.pack()
		self.canvas.bind("<Button-1>", self.mouse_click)
		self.draw_img()
		self.run()

	def run(self):
		"""run tkinter windows
		"""
		self.window.mainloop()

	def draw_img(self):
		"""draw the image represented by the recursive rectangle
		:return: None
		:rtype: None
		"""
		rects = self.rect.collect_rects()
		for rect in rects:
			self.canvas.create_rectangle(rect.x - rect.half_width, rect.y - rect.half_height,
										rect.x + rect.half_width, rect.y + rect.half_height,
										fill=rect.color, width=random.randint(rect.bar_width_lower, rect.bar_width_upper))

	def draw_new_img(self):
		"""draw the image represented by a new recursive rectangleevent
		:return: None
		:rtype: None
		"""
		self.rect = RecursiveRectangle((self.rect.x, self.rect.y), (self.rect.half_width, self.rect.half_height),
		                               colors=self.rect.possible_colors, level_weights=self.rect.level_weights,)
		self.rect.generate()
		self.canvas.delete("all")
		self.draw_img()
		self.save_no += 1

	def mouse_click(self, event):
		"""function to handle a mouse click
		:param event: mouse click event
		:return: None
		:rtype: None
		"""
		self.draw_new_img()

	def save_as_png(self, file_name):
		"""Save the tinker canvas to a png file
		:return: None
		:rtype: None
		"""
		# save postscipt image
		self.canvas.postscript(file=file_name + '.eps')
		# use PIL to convert to PNG
		img = Image.open(file_name + '.eps')
		img.save(file_name + '.png', 'png')
