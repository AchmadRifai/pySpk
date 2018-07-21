#!/bin/python3
from module1 import *
from hitung import *

data_path='data.json'
crit_path='crit.json'

data = dataFromJson(data_path)
crit = critFromJson(crit_path)

m = buatMatriks(data, crit)
print("Matriks")
cetakMatriks(m)

pembagi = genPembagi(m)
print("Pembagi")
cetakMatriks(pembagi)

normal = genNormalisasi(m, pembagi)
print("Normalisasi")
cetakMatriks(normal)

bobot = genBobot(normal, crit)
print("Terbobot")
cetakMatriks(bobot)

aplus = genAplus(bobot, crit)
amin = genAmin(bobot, crit)
print("A+")
cetakMatriks(aplus)
print("A-")
cetakMatriks(amin)

dplus = genDplus(bobot, aplus)
dmin = genDmin(bobot, amin)
print("D+")
cetakMatriks(dplus)
print("D-")
cetakMatriks(dmin)

for i in genValueData(data, dplus, dmin):
	print("" + str(i['nama']) + " = " + str(i['value']))
