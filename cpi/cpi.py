
def matriksData(data, tren):
	m = []
	nl = listNamaData(data)
	for n in nl:
		b = []
		for t in tren:
			b.append(getVal(data, n ,t))
		m.append(b)
	return m

def getVal(data, n ,t):
	v = 0
	for d in data:
		if n == d['nama'] and t['nama'] == d['args']:
			v = d['val']
			break
	return v

def listNamaData(data):
	l = []
	for d in data:
		if d['nama'] not in l:l.append(d['nama'])
	return l

def genMinimum(data):
	m = []
	l = []
	tmp = []
	for x in range(0, len(data[0])):
		b = []
		for y in range(0, len(data)):
			b.append(data[y][x])
		tmp.append(b)
	for b in tmp:
		l.append(min(b))
	m.append(l)
	return m

def genHitung(tren, minim, data):
	m = []
	for d in data:
		b = []
		my = minim[0]
		for x in range(0, len(d)):
			t = tren[x]
			minime = my[x]
			if "negatif" == t['arah']:b.append(minime /  d[x])
			else:b.append(d[x] /  minime)
		m.append(b)
	return m

def genSkor(hitung):
	m = []
	for b in hitung:
		l = []
		for v in b:l.append(v * 100)
		m.append(l)
	return m

def genResult(skor, data, tren):
	r = []
	nl = listNamaData(data)
	for x in range(0, len(nl)):
		s = skor[x]
		v = {"nama":nl[x],"res":0}
		for y in range(0, len(s)):
			t = tren[y]
			v['res'] = v['res'] + (t['bobot'] * s[y])
		r.append(v)
	return r

