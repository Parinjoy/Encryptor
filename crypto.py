#comments are debugging statements
import pickle
import random

def prime(a):
	for i in range (2,a//2+1):
		if a%i==0:
			return False
	else:
		return True

def prime_generator(code,count=100):
	g=[]
	a=1
	p=code+1
	while a<=count:
		if prime(p):
			g.append(p)
			a+=1
		p+=1
	return g

def key_generator():
	key=random.randint(10,1000)
	if prime(key):
		return key
	else:
		return key_generator()

def encrypt(word):
	k=[]
	code=key_generator()
	#print (code)
	l=prime_generator(code)
	#print (l)
	for j in word:
		temp=1
		m=0
		for q in range (48,ord(j)+1):
			temp*=l[m]
			m+=1
		k.append(temp)
	return k,code

def decrypt(data,code):
	buf=[]
	y=prime_generator(code)
	#print (y)
	for i in data:
		ans,j,count=0,0,0
		#print (y[j])
		#print(i%y[1])
		#print('Hello')
		while ans==0:
			#print (count)
			#print ('Hello')
			#print(i,j)
			#print (y[j])
			ans=i%y[j]
			#print(i,j)
			j+=1
			#print(j)
			count+=1
		count+=46
		#Why 46?
		buf.append(chr(count))
	#print(buf)
	s=''
	for k in buf:
		s+=k
	return s

n=input('Enter a Alphanumerino: ')
#print (prime(n))
e,f=encrypt(n)
#print(e)
print ('Your code is: ',f)
filehandler=open('secrets.dat','wb')
pickle.dump(e,filehandler)
filehandler.close()
#print(e,f)
filehandler2=open('secrets.dat','rb')
m=pickle.load(filehandler2)
print (decrypt(m,f))
filehandler2.close()
