import random


class RecursiveRectangle:
	def __init__(self, pos: (int, int), half_size: (int, int),
	             bar_width_bounds: (int, int) = (8, 8),
	             level: int = 0,
	             level_weights: tuple = (1, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1),
	             padding: float = 0.05,
	             color: str = "#FFFFFF",
	             colors: tuple = ("#000000", "#FF0000", "#FF0000", "#0000FF", "#0000FF", "#FFFF00", "#FFFF00", "#767676",
	                              "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF")):
		"""Recursive Rectangle, generates a Mondrian image by recursively fitting rectangles inside one another.

		:param pos: Position of middle
		:type pos: tuple(int, int)
		:param half_size: Width, Height
		:type half_size: tuple(int, int)
		:param padding: 0-1 fraction of width to use as padding
		:type padding: float
		:param bar_width_bounds: lower and upper bounds for border width
		:type bar_width_bounds tuple(int, int)
		:param color: Hex value representing color
		:type color: str
		:param level: level of the rectangle in the tree
		:type level: int
		:param level_weights: 0-1 chance of split at each level
		:type level_weights: tuple
		:param colors: contains all possible colours for the rectangles
		:type colors: tuple(str, str, ...)
		"""
		self.x, self.y = pos
		self.half_width, self.half_height = half_size
		self.pad = padding
		self.bar_width_lower, self.bar_width_upper = bar_width_bounds
		self.color = color
		self.possible_colors = colors
		self.level = level
		self.level_weights = level_weights
		self.r1 = None
		self.r2 = None

	def get_width(self):
		"""
		:return: full width of the rectangle
		:rtype: int
		"""
		return self.half_width * 2

	def get_height(self):
		"""
		:return: full height of the rectangle
		:rtype: int
		"""
		return self.half_height * 2

	def collect_rects(self):
		"""recursively collect all the rectangles underneath and including this one
		:return: list of rectangles underneath hsi one
		:rtype: list
		"""
		res = [self]
		if self.r1:
			res += self.r1.collect_rects()
		if self.r2:
			res += self.r2.collect_rects()
		return res

	def get_tl_br(self):
		"""get top left and bottom right co-ordinates

		used for tkinter drawing
		:return: tuple(tuple, tuple) with top left and br respectively
		:rtype: tuple
		"""
		tl = (self.x - self.half_width, self.y - self.half_height)
		br = (self.x + self.half_width, self.y + self.half_height)
		return tl, br

	def generate(self):
		"""Recursively generate an image using rectangles
		"""
		horizontal = False
		vertical = False
		new_level = random.random()
		if new_level <= self.level_weights[self.level]:
			if random.choice([True, False]):
				horizontal = True
			else:
				vertical = True
		if vertical:
			pass
		elif horizontal:
			pass
