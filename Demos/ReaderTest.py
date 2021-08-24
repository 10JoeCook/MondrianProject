from Utils.Readers import MatReader

reader = MatReader("../Paper1Data/MondriansAndTransatlantics.mat")
reader.read()
temp = reader.get_images()


print("DONE")
