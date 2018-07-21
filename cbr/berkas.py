import json

def resFromJson(path):
	d = []
	with open(path, "r") as f:
		d = json.load(f)
	return d

def isValidRes(res):
	b = True
	for r in res:
		if "id" not in r or "Nama" not in r:
			b = False
			break
	return b

def gejFromJson(path):
	d = []
	with open(path, "r") as f:
		d = json.load(f)
	return d

def isValidGej(gej):
	b = True
	for g in gej:
		if "id" not in g or "Nama" not in g:
			b = False
			break
	return b

def kasusFromJson(path):
	d = []
	with open(path, "r") as f:
		d = json.load(f)
	return d

def isValidKasus(kasus):
	b = True
	for k in kasus:
		if "id" not in k or "gej" not in k or "res" not in k:
			b = False
			break
	return b

def proFromJson(path):
	d = {}
	with open(path, "r") as f:
		d = json.load(f)
	return d

def isValidPro(pro, kasus):
	l = listKasus(kasus)
	b = "gej" in pro and "data" in pro
	if b:b = b and len(l) == len(pro['data'])
	if b:
		for d in pro['data']:
			if "cocok" not in d:
				b = False
				break
	return b

def getJumlahGejala(k, kasus):
	v = 0
	for i in kasus:
		if k['id'] == i['id']:v = v + 1
	return v

def listKasus(kasus):
	l = []
	for k in kasus:
		v = {'kasus':k['id'],'gejala':getJumlahGejala(k, kasus)}
		if v not in l:l.append(v)
	return l

