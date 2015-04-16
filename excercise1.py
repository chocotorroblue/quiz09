def raiz(r):
    h= r/2
    l= h+1
    while(h!=l):
        z= r/h
        l= h
        h= (h+z)/2
    return h
def hipo(h1,l1,h2,l2):
    a= (h2-h1)
    b= (l2-l1)
    h= (a*a)+(b*b)
    l= raiz(h)
    return l

h1=int(input("Give me the posicion h1 of the triangle "))
h2=int(input("Give me the posicion h2 of the triangle "))
l1=int(input("Give me the posicion l1 of the triangle "))
l2=int(input("Give me the posicion l2 of the triangle "))

print(hipo(h1,l1,h2,l2))
