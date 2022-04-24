n=int(input("enter range of numbers:"))
def fibonacci(x):
    n1=0
    n2=1
    print("fibonacci series is :")
    for i in range(2,n):
        f=n1+n2
        n1=n2
        n2=f
        print(f)
final=fibonacci(n)
print(final)
