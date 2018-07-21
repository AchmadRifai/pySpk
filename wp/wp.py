import math
from berkas import *

def genJumlahBobot(krit):
	v = 0
	for k in krit:
		v = v + k['kep']
	return v

def genBobot(krit):
	m = []
	l = []
	j = genJumlahBobot(krit)
	for k in krit:
		l.append(k['kep'] / j)
	m.append(l)
	return m

def genPangkat(krit, bobot):
	m = []
	l = []
	for x in range(0, len(krit)):
		k = krit[x]
		if "BENEFIT" == k['cb']:l.append(bobot[0][x])
		else:l.append(-1 * bobot[0][x])
	m.append(l)
	return m

def genS(data, pangkat):
	m = []
	for b in data:
		l = []
		f = 1
		p = pangkat[0]
		for x in range(0, len(b)):
			t = b[x]
			t = math.pow(t, p[x])
			f = f * t
		l.append(f)
		m.append(l)
	return m

def suming(s):
	v = 0
	for i in s:
		v = v + i[0]
	return v

def genResult(data, s):
	r = []
	nama = listNamaData(data)
	kum = suming(s)
	for x in range(0, len(nama)):
		v = {'nama':nama[x],'val':s[x][0]}
		v['val'] = v['val'] / kum
		r.append(v)
	return r

