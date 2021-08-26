a=[]
n=int(input("enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter elements:"))
    a.append(b)
for i in range(0,len(a)):
    for j in range(0,len(a)-i-1):
        if(a[j]>a[j+1]):
            temp=a[j]
            a[i]=a[j+1]
            a[j+1]=temp
print("Second largest number is:",a[n-2])
print(a)
