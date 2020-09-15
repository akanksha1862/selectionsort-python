n=eval(input("enter no. of elements"))
a=[0 for i in range(n)]
print("enter elements")
for i in range(n):
    a[i]=int(input())
print("the elements are",a)
for i in range(0,n):
    min=i
    for j in range(i+1,n):
        if(a[j]<a[min]):
            min=j
    if(min!=i):
        temp=a[min]
        a[min]=a[i]
        a[i]=temp
print("sorted array")
for i in range (n):
    print("%d"%a[i])
