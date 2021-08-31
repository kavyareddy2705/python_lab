Python 3.7.0a2 (v3.7.0a2:f7ac4fe, Oct 17 2017, 17:06:29) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def prime_eratosthenes(n):
    prime_list = []
    for i in range(2, n+1):
        if i not in prime_list:
            print (i)
            for j in range(i*i, n+1, i):
                prime_list.append(j)
                print(prime_eratosthenes(100));

                
>>> 
>>> def prime_eratosthenes(n):
	prime_list=[]
	for i in range(2,n+1):
		if i not in prime_list:
			print(i)
			for j in range(i*i,n+1,i):
				prime_list.append(j)
				print(prime_eratosthenes(100));

				
>>> 
