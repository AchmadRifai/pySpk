import json

def trenFromJson(path):
	l = []
	with open(path, "r") as f:
		l = json.load(f)
	return l

def dataFromJson(path):
	l = []
	with open(path, "r") as f:
		l = json.load(f)
	return l

def isValidTren(tren):
	b = True
	if b:
		for t in tren:
			if "nama" not in t or "bobot" not in t or "arah" not in t:
				b = False
				break
	return b

def isValidData(data):
	b = True
	if b:
		for d in data:
			if "nama" not in d or "args" not in d or "val" not in d:
				b = False
				break
	return b

def cetakMatriks(m):
	for b in m:
		print(b)

