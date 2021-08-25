import scipy.io
from Structures.Formal import FormalMondrian


class MatReader:
	def __init__(self, filename: str = "../Paper1Data/MondriansAndTransatlantics.mat"):
		self.filename = filename
		self.file_contents = None
		self.keys = []
		self.header = ""
		self.version = 0
		self.labels = []
		self.names = []
		self.reps = []
		self.images = []
		self.attr_lists = {}

	def read(self):
		self.file_contents = scipy.io.loadmat(self.filename)
		self.keys = self.file_contents.keys()
		self.header = self.file_contents["__header__"]
		self.version = self.file_contents["__version__"]
		self.labels = self.file_contents["labels"]
		self.labels = self.labels[0]
		self.names = self.file_contents["names"]
		self.names = self.names[0]
		for i in range(len(self.names)):
			self.names[i] = self.names[i][0]
		self.reps = self.file_contents["reps"]
		self.reps = self.reps[0]
		self.generate_image_objects()

	def generate_image_objects(self):
		for i in range(len(self.names)):
			name = self.names[i]
			rep = self.reps[i]
			ymax = int(rep[0][0][0])
			xmax = int(rep[1][0][0])
			vpts = list(rep[2][0])
			vext = list(rep[3])
			for i in range(len(vext)):
				vext[i] = list(vext[i])
			vthick = list(rep[4])
			for i in range(len(vthick)):
				vthick[i] = list(vthick[i])
			hpts = list(rep[5][0])
			hext = list(rep[6])
			for i in range(len(hext)):
				hext[i] = list(hext[i])
			hthick = list(rep[7])
			for i in range(len(hthick)):
				hthick[i] = list(hthick[i])
			rects = list(rep[8])
			for i in range(len(rects)):
				rects[i] = list(rects[i])
			rect_colors = list(rep[9][0])
			self.images.append(FormalMondrian(ymax,
			                                  xmax,
			                                  vpts,
			                                  hpts,
			                                  rect_colors,
			                                  vext,
			                                  vthick,
			                                  hext,
			                                  hthick,
			                                  rects))

	def generate_attr_lists(self):
		self.attr_lists["ymax"] = []
		self.attr_lists["xmax"] = []
		self.attr_lists["vpts"] = []
		self.attr_lists["vext"] = []
		self.attr_lists["vthick"] = []
		self.attr_lists["htps"] = []
		self.attr_lists["hext"] = []
		self.attr_lists["hthick"] = []
		self.attr_lists["rects"] = []
		self.attr_lists["rect_colors"] = []
		for i in range(len(self.names)):
			rep = self.reps[i]
			self.attr_lists["ymax"].append(int(rep[0][0][0]))
			self.attr_lists["xmax"].append(int(rep[1][0][0]))
			self.attr_lists["vpts"].append(list(rep[2][0]))
			vext = list(rep[3])
			for i in range(len(vext)):
				vext[i] = list(vext[i])
			self.attr_lists["vext"].append(vext)
			vthick = list(rep[4])
			for i in range(len(vthick)):
				vthick[i] = list(vthick[i])
			self.attr_lists["vthick"].append(vthick)
			self.attr_lists["hpts"].appemd(list(rep[5][0]))
			hext = list(rep[6])
			for i in range(len(hext)):
				hext[i] = list(hext[i])
			self.attr_lists["hext"].append(hext)
			hthick = list(rep[7])
			for i in range(len(hthick)):
				hthick[i] = list(hthick[i])
			self.attr_lists["hthick"].append(hthick)
			rects = list(rep[8])
			for i in range(len(rects)):
				rects[i] = list(rects[i])
			self.attr_lists["rects"].append(rects)
			self.attr_lists["rect_colors"].append(list(rep[9][0]))

	def get_images(self):
		return self.images

