def fibonacci(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b

    return a
n=int(input("Give me the number you want to use for the fibonacci "))
print(fibonacci(n))
