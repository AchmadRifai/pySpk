from module1 import *
import math

def getMaksud(data, c, n):
	for d in data:
		if n == d['nama'] and c['krit'] == d['krit']:
			return d['value']

def buatMatriks(data, crit):
	m = []
	if isValidCrit(crit) and isValidData(data):
		for n in listNamaData(data):
			l = []
			for c in crit:
				l.append(getMaksud(data, c, n))
			m.append(l)
	else:print("Salah oi")
	return m

def cetakMatriks(m):
	for l in m:
		print(""+str(l))

def genPembagi(m):
	p = []
	l = []
	for x in range(0 ,len(m[0])):l.append(0)
	for l2 in m:
		for x in range(0, len(l2)):
			l[x] = l[x] + (l2[x] ** 2)
	for x in range(0, len(l)):l[x] = math.sqrt(l[x])
	p.append(l)
	return p

def genNormalisasi(m, pembagi):
	n = []
	for b in m:
		l = []
		p = pembagi[0]
		for x in range(0, len(b)):
			l.append(b[x] / p[x])
		n.append(l)
	return n

def genBobot(normal, crit):
	b = []
	for l in normal:
		v = []
		for x in range(0, len(crit)):
			c = crit[x]
			v.append(l[x] * c['kep'])
		b.append(v)
	return b

def genAplus(bobot, crit):
	m = []
	l = []
	for x in range(0, len(crit)):
		t = []
		c = crit[x]
		for y in range(0, len(bobot)):t.append(bobot[y][x])
		if "BENEFIT" == c['cb']:l.append(max(t))
		else:l.append(min(t))
	m.append(l)
	return m

def genAmin(bobot, crit):
	m = []
	l = []
	for x in range(0, len(crit)):
		t = []
		c = crit[x]
		for y in range(0, len(bobot)):t.append(bobot[y][x])
		if "COST" == c['cb']:l.append(max(t))
		else:l.append(min(t))
	m.append(l)
	return m

def genDplus(bobot, aplus):
	m = []
	for b in bobot:
		l = [0]
		for x in range(0, len(b)): l[0] = l[0] + ((aplus[0][x] - b[x]) ** 2)
		l[0] = math.sqrt(l[0])
		m.append(l)
	return m

def genDmin(bobot, amin):
	m = []
	for b in bobot:
		l = [0]
		for x in range(0, len(b)): l[0] = l[0] + ((b[x] - amin[0][x]) ** 2)
		l[0] = math.sqrt(l[0])
		m.append(l)
	return m

def genValueData(data, dplus, dmin):
	r = []
	n = listNamaData(data)
	for x in range(0, len(n)):
		v = {'nama' : n[x]}
		v['value'] = dmin[x][0] / (dmin[x][0] + dplus[x][0])
		r.append(v)
	return r
