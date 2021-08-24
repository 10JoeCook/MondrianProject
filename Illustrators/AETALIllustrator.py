from Generators.P1Rep import MondrianImg
from tkinter import Tk, Canvas
from PIL import Image


class AETALIllustrator:
	def __init__(self, img: MondrianImg):
		self.img = img
		self.save_no = 0
		self.window = Tk()
		self.canvas = Canvas(self.window, width=self.img.x_max, height=self.img.y_max)
		self.canvas.pack()
		self.draw_img()
		self.run()

	def run(self):
		self.window.mainloop()

	def draw_img(self):
		for rect in self.img.get_rects():
			if rect[2] == 1:
				color = "#FFFFFF"
			elif rect[2] == 2:
				color = "#FF0000"
			elif rect[2] == 3:
				color = "#FFFF00"
			elif rect[2] == 4:
				color = "#0000FF"
			else:
				color = "#000000"
			self.canvas.create_rectangle(rect[0][0], rect[0][1], rect[1][0], rect[1][1],
			                             fill=color, width=0)
		for line in self.img.get_lines():
			self.canvas.create_line(line[0][0], line[0][1], line[1][0], line[1][1],
			                        fill="#000000", width=line[2])


class ListIllustrator:
	def __init__(self, images: list):
		self.images = images
		self.save_no = 0
		self.img_count = 0
		self.window = Tk()
		self.canvas = Canvas(self.window, width=self.images[0].x_max, height=self.images[0].y_max)
		self.canvas.pack()
		self.canvas.bind("<Button-1>", self.mouse_click)
		self.draw_img(self.images[0])
		self.run()

	def run(self):
		self.window.mainloop()

	def draw_img(self, img: MondrianImg):
		for rect in img.get_rects():
			if rect[2] == 1:
				color = "#FFFFFF"
			elif rect[2] == 2:
				color = "#FF0000"
			elif rect[2] == 3:
				color = "#FFFF00"
			elif rect[2] == 4:
				color = "#0000FF"
			else:
				color = "#000000"
			self.canvas.create_rectangle(rect[0][0], rect[0][1], rect[1][0], rect[1][1],
			                             fill=color, width=0)
		for line in img.get_lines():
			self.canvas.create_line(line[0][0], line[0][1], line[1][0], line[1][1],
			                        fill="#000000", width=line[2])

	def draw_new_img(self):
		try:
			self.canvas.delete("all")
			self.draw_img(self.images[self.img_count])
		finally:
			self.img_count += 1
		# self.save_as_png(str(self.save_no))

	def mouse_click(self, event):
		self.draw_new_img()

	def save_as_png(self, file_name):
		# save postscipt image
		self.canvas.postscript(file=file_name + '.eps')
		# use PIL to convert to PNG
		img = Image.open(file_name + '.eps')
		img.save(file_name + '.png', 'png')
		self.save_no += 1