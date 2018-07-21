from berkas import *

def genPembagi(kasus, pilih):
	if kasus > pilih:return kasus
	else:return pilih

def genNilai(cocok, pembagi):
	v = cocok
	v = v / pembagi
	v = v * 100
	return v

def genResult(pro, gej, kasus, res):
	pilih = len(pro['gej'])
	lk = listKasus(kasus)
	r = {"data":[],"intro":"Dipilih " + str(pilih) + "Gejala : "}
	for i in pro['gej']:
		r['intro'] = r['intro'] + gej[i - 1]['Nama'] + ", "
	for x in range(0, len(pro['data'])):
		d = pro['data'][x]
		k = lk[x]
		b = {"No":x + 1,"Gejala Cocok":d['cocok'],"Gejala Kasus":k['gejala'],"Gejala Pilih":pilih}
		b["pembagi"] = genPembagi(k['gejala'], pilih)
		b["Nilai"] = genNilai(b['Gejala Cocok'], b['pembagi'])
		r['data'].append(b)
	return r

