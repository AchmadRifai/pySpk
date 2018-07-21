#!/bin/python3

from berkas import *
from cbr import *

ex_path = ["ex1.json","ex2.json","ex3.json"]
gej_path = "gej.json"
kasus_path = "kasus.json"
res_path = "res.json"

gej = gejFromJson(gej_path)
kasus = kasusFromJson(kasus_path)
res = resFromJson(res_path)

if isValidGej(gej) and isValidKasus(kasus) and isValidRes(res):
	print("Gejala")
	for g in gej:print("" + str(g['id']) + " = " + g['Nama'])
	print("\nResult List")
	for r in res:print("" + str(r['id']) + " = " + r['Nama'])
	print("\nResult Kasus")
	for k in kasus:print("" + str(k['id']) + ", Gejala = " + str(gej[k['gej'] - 1]['Nama']) + ", Result = " + str(res[k['res'] - 1]['Nama']))
	for p in ex_path:
		print("\n" + p)
		e = proFromJson(p)
		if isValidPro(e, kasus):
			r = genResult(e, gej, kasus, res)
			print(r['intro'])
			for d in r['data']:
				print("" + str(d['No']) + ", " + str(d['Gejala Cocok']) + ", " + str(d['Gejala Kasus']) + ", " + str(d['Gejala Pilih']) + ", " + str(d['pembagi']) + ", " + str(d['Nilai']) + "%")
		else:print("2:Error")
else:print("1:Error")
