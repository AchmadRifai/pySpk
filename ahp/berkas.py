import json

def kritFromJson(path):
	k = {}
	with open(path, "r") as f:
		k = json.load(f)
	return k

def dataFromJson(path):
	d = []
	with open(path, "r") as f:
		d = json.load(f)
	return d

def isValidData(data):
	b = True
	for d in data:
		if "krit" not in d or "nama" not in d or "value" not in d:
			b = False
			break
	return b

def isValidKrit(krit):
	b = False
	if "field" in krit and "pengaruh" in krit:
		b = True
		for f in krit['field']:
			if "nama" not in f or "n" not in f or "RI" not in f or "cb" not in f:
				b = False
				break
		if b:
			for p in krit['pengaruh']:
				if "kep" not in p or "n2" not in p or "n1" not in p:
					b = False
					break
	return b

def listNamaData(data):
	n = []
	for d in data:
		if len(n) > 0:
			if d['nama'] not in n:n.append(d['nama'])
		else:n.append(d['nama'])
	return n

def cetakMatriks(m):
	for b in m:
		print(b)
