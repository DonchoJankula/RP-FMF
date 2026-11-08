def mustard():
    x=a(int(input("Vnesi broj na godini: ")))

    if x:
        print("Access granted!")
    else:
        print("Access denied!")
def a(D):
    return True if D>18 else False
mustard()