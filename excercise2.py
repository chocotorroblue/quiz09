def triangles(size):
    for i in range(1, size+1):
        for j in range(i):
            print("T", end="")
        print()

    for i in range(1,size+1):
        for j in range(size-i+1):
            print("T", end="")
        print()
size=int(input("Dame el ancho de tu triangulo: "))
h=triangles(size)
