#!/bin/python3

from berkas import *
from cpi import *

data_path = "data.json"
tren_path = "tren.json"

tren = trenFromJson(tren_path)
data = dataFromJson(data_path)

if isValidData(data) and isValidTren(tren):
	print("Data")
	m = matriksData(data, tren)
	cetakMatriks(m)
	print("\nMinimum")
	minim = genMinimum(m)
	cetakMatriks(minim)
	print("\nMatriks Perhitungan")
	hitung = genHitung(tren, minim, m)
	cetakMatriks(hitung)
	print("\nMatriks Skor Perhitungan")
	skor = genSkor(hitung)
	cetakMatriks(skor)
	print("\nHasil")
	for v in genResult(skor, data, tren):
		print("" + str(v['res']) + " = " + str(v['nama']))
else:print("Error")

