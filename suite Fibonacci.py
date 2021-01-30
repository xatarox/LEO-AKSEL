#suite de fibonacci


from time import *


a, b, c=1,1,1

while True:
	print(c, "<>", b, type(b)) #int
	a,b,c=b,a+b,c+1
	sleep(0.1)

''''
while True:
	print("[+]", b, type(b)) #int
	a,b=b,a+b
	sleep(0.1)
''''
