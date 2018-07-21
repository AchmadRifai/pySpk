import json

def halo():
	print("Ok")

def critFromJson(path):
	d = []
	with open(path, "r")as f:
		d = json.load(f)
	return d

def dataFromJson(path):
	d = []
	with open(path, "r") as f:
		d = json.load(f)
	return d

def isValidCrit(crit):
	b = True
	if len(crit) > 0:
		for c in crit:
			b = 'cb' in c and 'kep' in c and 'krit' in c
			if not b:break
	return b

def isValidData(data):
	b = True
	if len(data) > 0:
		for c in data:
			b = 'krit' in c and 'nama' in c and 'value' in c
			if not b:break
	return b

def saveDataJson(data, path):
	with open(path, "w") as f:
		json.dump(data, f)

def saveCritJson(crit, path):
	with open(path, "w") as f:
		json.dump(crit, f)

def listNamaData(data):
	n = []
	for c in data:
		if len(n) > 0:
			if c['nama'] not in n:
				n.append(c['nama'])
		else:n.append(c['nama'])
	return n

