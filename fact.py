import math
def fact_count(num):
	sq=int(math.sqrt(n))
	fc=2
	for i in range(2,sq+1):
	   		if n%i==0:
	   			fc+=1
	   			if i !=n//i:
	   				fc+=1
	return fc
n=int(input())
print("Factors count of givem numbers is:",fact_count(n))