def superpower(x,y):
    if y==0:
        return 1
    r = x
    for n in range (y-1):
        r*=x
    return r

x=int(input("Give me a number "))
y=int(input("Give me another number "))
print(superpower(x,y))
