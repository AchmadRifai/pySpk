import math
from berkas import *

def genPembagi(data, syarat):
	p = []
	l = []
	for x in range(0, len(syarat)):
		l2 = []
		s = syarat[x]
		for y in range(0, len(data)):l2.append(data[y][x])
		if s['cb'] == 'BENEFIT': l.append(max(l2))
		else: l.append(min(l2))
	p.append(l)
	return p

def genNormalisasi(pembagi, matriks, syarat):
	n = []
	for b in matriks:
		l = []
		p = pembagi[0]
		for x in range(0, len(b)):
			s = syarat[x]
			if 'COST' == s['cb']: l.append(p[x] / b[x])
			else: l.append(b[x] / p[x])
		n.append(l)
	return n

def genResult(syarat, normal, data):
	r = []
	nama = listNamaData(data)
	for x in range(0, len(nama)):
		v = {'nama':nama[x]}
		b = normal[x]
		f = 0
		for y in range(0, len(syarat)):
			s = syarat[y]
			f = f + (s['kep'] * b[y])
		v['val'] = f
		r.append(v)
	return r

