import json
fibo={}
def fib():
	num=input('Ingrese un numero del 1 al 20: ')
	n=0
	a, b = 0, 1
	while n<int(num):
		
		a,b = b, a+b
		n=n+1
		fibo['num'+str(n)]=a
	print()
fib()
fjson=json.dumps(fibo)
print(fjson)

