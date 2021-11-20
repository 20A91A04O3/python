#Program for grade finding for given markd
marks=int(input('Enter marks:'))
if marks<35:
	print('Fail')
elif marks>=85:
	print('Grade A')
elif marks>=75:
	print('Grade B')
elif marks>=65:
	print('Grade C')
elif marks>=50:
	print('Grade D')