#!/bin/python3

from berkas import *
from ahp import *
from carry import *

data_path = 'data.json'
krit_path = 'krit.json'

data = dataFromJson(data_path)
krit = kritFromJson(krit_path)

if isValidData(data) and isValidKrit(krit):
	print("Krit")
	m = matriksKrit(krit)
	cetakMatriks(m)
	print("")
	print("Data")
	dm = matriksData(data, krit['field'])
	cetakMatriks(dm)
	print("")
	print("Jumlah")
	jumlah = genJumlah(m)
	cetakMatriks(jumlah)
	print("")
	print("Normalisasi")
	normal = genNormal(m, jumlah)
	cetakMatriks(normal)
	print("")
	print("Average")
	av = genAveraging(normal)
	cetakMatriks(av)
	print("")
	print("Fielding")
	fielding = genFielding(av, m)
	cetakMatriks(fielding)
	print("")
	T = genT(fielding, av)
	print("T : ", T)
	print("")
	ci = genCI(T, krit['field'])
	print("CI : ", ci)
	print("")
	if ci < 0.1:
		print("Layak")
		print("")
		print("Ranking")
		rank = ranked(data, krit)
		cetakMatriks(rank)
		print("Result")
		for r in result(rank, av, data):
			print("" + r['nama'] + " = " + str(r['val']))
	else:print("Tidak layak")
else:
	print("Error")
