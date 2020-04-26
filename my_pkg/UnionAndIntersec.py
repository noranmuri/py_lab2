#!/usr/bin/env ython3
import re
def UAI():
	a=[]
	b=[]
	a = input("1st list: ")
	b = input("2nd list: ")
	a = re.findall("\d+", a)	
	for i in range(len(a)):
		a[i]=int(a[i])
	
	b = re.findall("\d+", b)	
	for i in range(len(b)):
		b[i]=int(b[i])
	
	union = list(set(a)|set(b))
	inter = list(set(a)&set(b))
	
	print("=> union " , union)
	print("=> intersection " , inter)
