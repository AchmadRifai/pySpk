import json

def dataFromJson(path):
	d = []
	with open(path, "r") as f:
		d = json.load(f)
	return d

def isValidData(data):
	b = True
	for v in data:
		if "krit" not in v or "nama" not in v or "value" not in v:
			return False
	return b

def syaratFromJson(path):
	s = []
	with open(path, "r") as f:
		s = json.load(f)
	return s

def isValidSyarat(syarat):
	for v in syarat:
		if "cb" not in v or "nama" not in v or "kep" not in v:
			return False
	p = 0
	for v in syarat: p = p + v['kep']
	b = 1.0 == p
	return b

def listNamaData(data):
	n = []
	for i in data:
		if len(n) > 0:
			if i['nama'] not in n:n.append(i['nama'])
		else:n.append(i['nama'])
	return n

def valData(data, n, s):
	r = 0
	for v in data:
		if v['krit'] == s['nama'] and n == v['nama']:
			r = v['value']
			break
	return r

def buatMatriks(data, syarat):
	m = []
	for n in listNamaData(data):
		l = []
		for s in syarat:l.append(valData(data, n, s))
		m.append(l)
	return m

def cetakMatriks(m):
	for b in m:
		print(b)

