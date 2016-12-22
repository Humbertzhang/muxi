def calculate():

	while True:
		a = input("Please input a word>>>>>>>>")
		import time
		t1=time.time()
		b = a.lower()
		letterlist = list(b)
		calculater = 0
		alphabet = {
		'a':1,'b':2,'c':3,'d':4,
		'e':5,'f':6,'g':7,'h':8,
		'i':9,'j':10,'k':11,'l':12,
		'm':13,'n':14,'o':15,'p':16,
		'q':17,'r':18,'s':19,'t':20,
		'u':21,'v':22,'w':23,'x':24,
		'y':25,'z':26,
		}
		for key,value in alphabet.items():
			for letters in letterlist:
				if letters in key:
					calculater = calculater + alphabet[key]

		print ('The final number is------>',calculater)
		t2=time.time()
		t = t2 - t1
		#程序运行时间
		print (t*1000,'ms')


Calculate = calculate()