from Utils.Convertors import MatToTxt

conv = MatToTxt("../Paper1Data/MondriansAndTransatlantics.mat")

conv.read()
print(conv)
conv.convert()
