def fun(n):
	if n<=0:
		print(n,end=" ")
		return 
	fun(n-1)
	fun(n-2)
	print(n,end=" ")
fun(5)
