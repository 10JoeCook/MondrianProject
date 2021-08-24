from Utils.Readers import MatReader
from Illustrators.AETALIllustrator import ListIllustrator

reader = MatReader("../Paper1Data/MondriansAndTransatlantics.mat")
reader.read()
illustrator = ListIllustrator(reader.get_images())
