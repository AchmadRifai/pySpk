import json

def dataFromJson(path):
	d = []
	with open(path, "r") as f:
		d = json.load(f)
	return d

def kritFromJson(path):
	k = []
	with open(path, "r") as f:
		k = json.load(f)
	return k

def isValidData(data):
	b = True
	for v in data:
		if "krit" not in v or "nama" not in v or "value" not in v:
			b = False
			break
	return b

def isValidKrit(krit):
	b = True
	for v in krit:
		if "cb" not in v or "krit" not in v or "kep" not in v:
			b = False
			break
	return b

def listNamaData(data):
	l = []
	for d in data:
		if d['nama'] not in l:l.append(d['nama'])
	return l

def genValue(data, n, k):
	v = 0
	for d in data:
		if d['nama'] == n and d['krit'] == k:
			v = d['value']
			break
	return v

def matriksData(data, krit):
	m = []
	for n in listNamaData(data):
		b = []
		for k in krit:b.append(genValue(data, n, k['krit']))
		m.append(b)
	return m

def cetakMatriks(m):
	for b in m:
		print(b)

