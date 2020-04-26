#!/usr/bin/env python3

#define function
def BTO():
	num = input("input binary number : ")
	b=int(num,2)
	o=format(b,'o')
	x=format(b,'X')
	print("=> OCT> " + o);
	print("=> DEC> %d" %b)
	print("=> HEX> " + x);

