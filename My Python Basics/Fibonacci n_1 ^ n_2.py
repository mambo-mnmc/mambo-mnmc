def fiboSeries(n):
	if n < 2:
		return n 
	else:
		return fiboSeries(n-2) + fiboSeries(n-1)
print()
Terms = int(input("ngenesa term apa"))
if Terms <= 0:
	print("ngenesa numba yako fibo")
else:
	print("The Fibonacci series ye ufuna iyo : ")
for i in range(Terms):
	print(fiboSeries(i))