#!/usr/bin/env python3
import my_pkg
if __name__=='__main__':
	while 1:
		menu = int(input('Select menu: 1)conversion 2)union/intersection 3)exit ? '))
		if(menu == 1):
			my_pkg.BTO()
		elif(menu == 2):
			my_pkg.UAI()
		elif (menu==3):
			print("exit the program...")
			break;		

