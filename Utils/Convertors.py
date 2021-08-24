import scipy.io


class MatToTxt:
	def __init__(self, filename: str = "images.mat"):
		self.filename = filename
		self.file_contents = None

	def __str__(self):
		out = ""
		for val in self.file_contents.keys():
			out += f"{val}\n"
			out += f"{self.file_contents[val]}\n"
		return out

	def read(self):
		self.file_contents = scipy.io.loadmat(self.filename)

	def convert(self):
		pass

	def get_keys(self):
		return str(self.file_contents.keys())

	def get_version(self) -> str:
		return self.file_contents["__version__"]

	def get_header(self) -> str:
		return self.file_contents["__header__"]

	def get_names(self) -> str:
		return self.file_contents["names"]

	def get_reps(self) -> str:
		return self.file_contents["reps"]
