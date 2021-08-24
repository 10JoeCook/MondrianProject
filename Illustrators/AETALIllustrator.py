from Generators.P1Rep import MondrianImg
from tkinter import Tk, Canvas


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
		self.window = Tk()
		self.canvas = Canvas(self.window, width=self.images[0].x_max, height=self.images[0].y_max)
		self.canvas.pack()
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
