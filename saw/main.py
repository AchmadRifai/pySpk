#!/bin/python3

from berkas import *
from saw import *

syarat_path = "syarat.json"
data_path = "data.json"

data = dataFromJson(data_path)
syarat = syaratFromJson(syarat_path)

if isValidData(data):
	print("Data")
	print(data)
else:print("Salah oi")
print("")
if isValidSyarat(syarat):
	print("Syarat")
	print(syarat)
else:print("Salah oi")
print("")

m = buatMatriks(data, syarat)
print("Data Matriks")
cetakMatriks(m)
print("")

pembagi = genPembagi(m, syarat)
print("Pembagi")
cetakMatriks(pembagi)
print("")

normal = genNormalisasi(pembagi, m, syarat)
print("Normalisasi")
cetakMatriks(normal)
print("")

print("Hasil")
for r in genResult(syarat, normal, data):
	print("" + str(r['nama']) + " = " + str(r['val']))

