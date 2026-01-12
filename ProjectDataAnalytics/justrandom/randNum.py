import random
import time

def geneRand():
	num = range(0,10)
	num1 = random.sample(num, 7)
	print("randomly generated 7-digits is:", num1)	

def randChoose():
	txt = [1,2,3,4,5,6,7,8,9,0]
	num2 = random.sample(txt, 7)
	print("pick up from numList:", num2)

def seedGener():
	random.seed(time.time())
	num3 = []
	for i in range(7):
		num3.append(random.randint(0,9))
	print("generated with time as seed:",num3)


geneRand()
randChoose()
seedGener()