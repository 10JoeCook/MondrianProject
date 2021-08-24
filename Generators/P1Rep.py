class MondrianImg:
	def __init__(self, ymax: int, xmax:int, vpts: list, hpts: list, rect_colors: list, vext: list, vthick: list,
	             hext: list, hthick: list, rects: list):
		self.y_max = ymax
		self.x_max = xmax
		self.v_pts = vpts
		self.h_pts = hpts
		self.rect_colours = rect_colors
		self.v_ext = vext
		self.v_thick = vthick
		self.h_ext = hext
		self.h_thick = hthick
		self.rects = rects

	def get_rects(self) -> list:
		ret = []
		for rect in self.rects:
			tl = (self.v_pts[rect[0]], self.h_pts[rect[2]])
			br = (self.v_pts[rect[1]], self.h_pts[rect[3]])
			color = self.rect_colours[self.rects.index(rect)]
			ret.append((tl, br, color))
		return ret
