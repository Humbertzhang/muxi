#题目2
#依次计算一系列给定字符串的字母值，字母值为字符串中每个字母对应的编号值
#（A对应1，B对应2，以此类推，不区分大小写字母，非字母字符对应的值为0）的总和。
#例如，Colin 的字母值为 3 + 15 + 12 + 9 + 14 = 53

#输入格式:一系列字符串，每个字符串占一行。
#输出格式：计算并输出每行字符串的字母值。
#输入样例：
#Colin
#ABC 
#输出样例：
#53
#6
#时间限制：500ms 内存限制：32000kb



def calculate():
	#使程序一直运行，来满足一直输入的需求。	
	while True:
		a = input("Please input a word>>>>>>>>")
		import time
		#计时开始：为每次输入后开始计时。		
		t1=time.time()
		#转换为小写，以便统一计算		
		b = a.lower()
		#使单词变为一个列表		
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
		#用字典的key-value来实现计算	
		#对每个字母进行计算		
		for key,value in alphabet.items():
			for letters in letterlist:
				if letters in key:
					calculater = calculater + alphabet[key]

		print ('The final number is>>>>>>>>',calculater)
		t2=time.time()
		t = t2 - t1
		#计时结束		
		print (t*1000,'ms')
Calculate = calculate()
