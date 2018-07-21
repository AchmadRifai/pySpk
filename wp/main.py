#!/bin/python3

from berkas import *
from wp import *

data_path = 'data.json'
krit_path = 'krit.json'

data = dataFromJson(data_path)
krit = kritFromJson(krit_path)

if isValidData(data) and isValidKrit(krit):
	print("Data")
	m = matriksData(data, krit)
	cetakMatriks(m)
	print("")
	bobot = genBobot(krit)
	print("Bobot")
	cetakMatriks(bobot)
	print("")
	pangkat = genPangkat(krit, bobot)
	print("Pangkat")
	cetakMatriks(pangkat)
	print("")
	s = genS(m, pangkat)
	print("S")
	cetakMatriks(s)
	print("")
	print("S")
	for r in genResult(data, s):
		print("" + r['nama'] + " = " + str(r['val']))
	print("")
else:print("Format salah")

