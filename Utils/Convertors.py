import scipy.io


class MatToTxt:
	def __init__(self, filename: str = "images.mat"):
		self.filename = filename
		self.file_contents = None

	def __str__(self):
		out = ""
		for val in self.file_contents.keys():
			print(val)
			print(self.file_contents[val])

	def read(self):
		self.file_contents = scipy.io.loadmat(self.filename)

	def convert(self):
		pass

