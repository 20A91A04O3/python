import math
def isprime(num):
	if num==1:
		return False
	sq=int(math.sqrt(num))
	for i in range(2,sq+1):
	   		if num%i==0:
	   			return False
	   		return True
def reverse(num):
	rev=0
	while num:
		d=num%10
		num=num//10
		rev=rev*10+d
	return rev
n=int(input())
print(isprime(n))
rev=reverse(n)
if isprime(n)==True:
	print(isprime(rev))
	if isprime(n)==True and isprime(rev)==True:
		print("Circular Prime")