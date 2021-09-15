def SplitArray(arr, n, k):
	for i in range(0, k):
		x = arr[0]
		for j in range(0, n-1):
			arr[j] = arr[j + 1]
		
		arr[n-1] = x		
arr = [10, 4, 15, 1, 5, 3]
n = len(arr)
position = 3
SplitArray(arr, n, position)
for i in range(0, n):
	print(arr[i], end = ' ')
