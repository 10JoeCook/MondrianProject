import scipy.io


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
		pass
