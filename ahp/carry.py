from ahp import *
from berkas import *

def isLayakKrit(krit):
	b = False
	if isValidKrit(krit):
		m = matriksKrit(krit)
		jumlah = genJumlah(m)
		normal = genNormal(m, jumlah)
		av = genAveraging(normal)
		fielding = genFielding(av, m)
		T = genT(fielding, av)
		ci = genCI(T, krit['field'])
		b = ci < 0.1
	return b

def pushRanked(l, k):
	m = []
	for v1 in l:
		l2 = []
		for v2 in l:
			if "COST" == k['cb']:l2.append(v2 / v1)
			else:l2.append(v1 / v2)
		m.append(l2)
	return m

def summing(p):
	m = []
	l = []
	for x in range(0, len(p[0])):l.append(0)
	for x in range(0, len(p[0])):
		for y in range(0, len(p)):
			l[x] = l[x] + p[y][x]
	m.append(l)
	return m

def diving(p, tmb):
	m = []
	for v in p:
		l = []
		for x in range(0, len(v)):
			l.append(v[x] / tmb[0][x])
		m.append(l)
	return m

def mmr(div):
	m = []
	for b in div:
		f = 0
		for v in b:f = f + v
		f = f / len(b)
		m.append(f)
	return m

def genTmp(dm, krit):
	tmp = []
	for x in range(0, len(krit['field'])):
		k = krit['field'][x]
		l = []
		for y in range(0, len(dm)):l.append(dm[y][x])
		p = pushRanked(l, k)
		tmb = summing(p)
		div = diving(p, tmb)
		tmp.append(mmr(div))
	return tmp

def ranked(data, krit):
	r = []
	if isValidData(data):
		dm = matriksData(data, krit['field'])
		tmp = genTmp(dm, krit)
		for x in range(0, len(dm)):
			l = []
			for y in range(0, len(tmp)):l.append(tmp[y][x])
			r.append(l)
	return r

def result(rank, av, data):
	l = []
	n = listNamaData(data)
	for x in range(0, len(n)):
		v = {'nama':n[x],'val':0}
		b = rank[x]
		for y in range(0, len(b)):
			v['val'] = v['val'] + (b[y] * av[y][0])
		l.append(v)
	return l

