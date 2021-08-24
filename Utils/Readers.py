import scipy.io


class MatReader:
	def __init__(self, filename: str = "../Paper1Data/MondriansAndTransatlantics.mat"):
		self.filename = filename
		self.file_contents = None
		self.names = None
		self.reps = None
		self.labels = None

	def read(self):
		self.file_contents = scipy.io.loadmat(self.filename)
		self.names = self.file_contents["names"]
