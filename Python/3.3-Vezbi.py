def bnumber():
    n1=float(input("Vnesi go prviot broj: ")) n2=float(input("Vnesi go vtoriot broj: "))
    if n1>n2:
        print("Prviot vnesen broj e pogolem od vtoriot")
    elif n1<n2:
        print("Vtoriot vnesen broj e pogolem od prviot")
    else:
        print("Broevite se ednakvi")
bnumber()