def fibonacci(n):
	a=0
	b=1
	fibonacci_list=[0,1]
	while len(fibonacci_list) < n:
		a_new=a+b
		b_new=b+a_new
		fibonacci_list.append(a_new)
		fibonacci_list.append(b_new)
		a=a_new
		b=b_new
	return fibonacci_list
