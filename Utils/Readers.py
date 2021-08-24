import scipy.io
from Generators.P1Rep import MondrianImg


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
			self.images.append(MondrianImg(ymax,
			                               xmax,
			                               vpts,
			                               hpts,
			                               rect_colors,
			                               vext,
			                               vthick,
			                               hext,
			                               hthick,
			                               rects))

	def get_images(self):
		return self.images

