from berkas import *

def genPengaruh(pengaruh, n1, n2):
	r = 1
	for p in pengaruh:
		b1 = p['n1'] == n1 and p['n2'] == n2
		b2 = p['n1'] == n2 and p['n2'] == n1
		if b1:
			r = p['kep']
			break
		if b2:
			r = r / p['kep']
			break
	return r

def matriksKrit(krit):
	m = []
	for f in krit['field']:
		b = []
		for f2 in krit['field']:
			if f['nama'] == f2['nama']:b.append(1)
			else:b.append(genPengaruh(krit['pengaruh'], f2['nama'], f['nama']))
		m.append(b)
	return m

def genJumlah(matriks):
	m = []
	l = []
	for x in range(0, len(matriks)):
		f = 0
		for y in range(0, len(matriks)):f = f + matriks[y][x]
		l.append(f)
	m.append(l)
	return m

def genNormal(matriks, jumlah):
	m = []
	for x in range(0, len(matriks)):
		l = []
		j =  jumlah[0]
		ma = matriks[x]
		for y in range(0, len(ma)):l.append(ma[y] / j[y])
		m.append(l)
	return m

def genAveraging(normal):
	m = []
	for b in normal:
		l = [0]
		for x in range(0, len(b)):l[0] = l[0] + b[x]
		l[0] = l[0] / len(b)
		m.append(l)
	return m

def genFielding(normal, matriks):
	m = []
	for b in matriks:
		l = [0]
		for x in range(0, len(b)):
			n = normal[x]
			l[0] = l[0] + (n[0] * b[x])
		m.append(l)
	return m

def genT(fielding, av):
	r = 0
	for x in range(0, len(av)):
		f = fielding[x]
		a = av[x]
		r = r + (f[0] / a[0])
	r = r / len(av)
	return r

def genCI(T, field):
	ri6 = field[len(field) - 2]['RI']
	ci = (T - len(field)) / (len(field) - 1)
	return ci / ri6

def getValueData(data, nama, krit):
	for d in data:
		if d['nama'] == nama and d['krit'] == krit:
			return d['value']

def matriksData(data, field):
	m = []
	if isValidData(data):
		for n in listNamaData(data):
			l = []
			for f in field:
				l.append(getValueData(data, n, f['nama']))
			m.append(l)
	return m

