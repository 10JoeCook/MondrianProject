class FormalMondrian:
	def __init__(self, name: str, ymax: int, xmax:int, vpts: list, hpts: list, rect_colors: list, vext: list, vthick: list,
	             hext: list, hthick: list, rects: list):
		self.name = name
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
			tl = (self.v_pts[rect[0] - 1], self.h_pts[rect[2] - 1])
			br = (self.v_pts[rect[1] - 1], self.h_pts[rect[3] - 1])
			color = self.rect_colours[self.rects.index(rect)]
			ret.append((tl, br, color))
		return ret

	def get_lines(self) -> list:
		ret = []
		for i in range(len(self.v_pts)):
			start = (self.v_pts[i], self.h_pts[self.v_ext[i][0] - 1])
			end = (self.v_pts[i], self.h_pts[self.v_ext[i][1] - 1])
			thickness = self.v_thick[i]
			ret.append((start, end, thickness))
		for i in range(len(self.h_pts)):
			start = (self.v_pts[self.h_ext[i][0] - 1], self.h_pts[i])
			end = (self.v_pts[self.h_ext[i][1] - 1], self.h_pts[i])
			thickness = self.h_thick[i]
			ret.append((start, end, thickness))
		return ret
