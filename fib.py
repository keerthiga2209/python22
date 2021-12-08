nterms = int(input("How many terms? "))
f1 = 0
f2 = 1
count = 2
if nterms<= 0:
    print("Plese enter a positive integer other than zero")
elif nterms == 1:
    print("Fibonacci sequence:")
    print(f1)
else:
    print("Fibonacci sequence:")
    print(f1,",",f2,end=', ')
    for i in range(count,nterms):
        f3=f1+f2
        print(f3,end=', ')
        f1=f2
        f2=f3
