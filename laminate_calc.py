# 1292
# 1,292
# 194
# 8
# 2.005

# -0,363

# всего 8 * 9 = 72 панели

# размеры комнаты 5.335 * 3.33 впритык
# 2,584 две панели целые

# 0,746

# 5.48

import sys
import os

lw = 0.194
lh = 1.291
cw = 3.53
# ch = 5.435
ch = 5.475
if 1:
	cw, ch = ch, cw
threshold = 0.25

null = open(os.devnull,'w')

def calc_silent(*args, **kw):
	_stout = sys.stdout
	sys.stdout = null
	r = calc(*args, **kw)
	sys.stdout = _stout
	return r

def calc(w_otstup, rem_1st=0):
	w = cw - (2 * w_otstup)
	h = ch #- (2 * 0.01)
	
	print('Rows', h / lw)
	rows = int(h / lw)
	llh = rows * lw
	print('%s rows =' % rows, llh, 'm')
	h_otstup = (h - llh) / 2
	print('otstup h from each side', h_otstup)
	
	print('obreski')
	rem = rem_1st
	total_doski = 0
	total_warnings = 0
	for i in range(rows):
		cnt = int((w - rem) / lh)
		obres = w - rem - lh * cnt
		rem = lh - obres
		total_doski += cnt + 1
		
		warning = ''
		if rem < threshold or obres < threshold:
			warning = '<---'
			total_warnings += 1
		if rem < threshold:
			rem = 0.0
		print(i + 1, '\twhole', cnt, '\tremain %.3f' % rem, '\tobresok %.3f' % obres, warning)
		
	print('summa dosok', total_doski, 'poor parts:', total_warnings)
	return total_warnings
	
def drange(start, stop, step):
	l = stop - start
	tot = int(l / step)
	return (start + l * i / tot for i in range(0, tot + 1))
	
def test_drange():
	# print(list(range(0,1)))
	for i in drange(0.0, 1.0, 0.1):
		print(i)
		
def na(*args):
	pass

def brute():
	min = (1000, 0, 0)
	for otst in drange(0.01, 0.02, 0.001):
		for rem1 in drange(0.0, lh, 0.001):
			tw = calc_silent(otst, rem1)
			if min[0] > tw:
				min = (tw, otst, rem1)
			# print(tw)
	print('best', min)

# brute()
# calc(0.003, 0.023, silent=False)
# calc(0.05, 0.3)
# calc(0.025, 0.113) # 5
# calc(0.01, 0.0) # 5
# calc(0.01, 0.0)
calc(0.00, 0.0)  #