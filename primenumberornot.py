import math
def fact_count(num):
	sq=int(math.sqrt(n))
	fc=2
	for i in range(2,sq+1):
	   		if n%i==0:
	   			return False
	   		return True
	return fc
n=int(input())
print(fact_count(n))