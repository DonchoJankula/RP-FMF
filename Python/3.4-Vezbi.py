def pas():
    x=b(input("Vnesi password: "))
    if x:
        print("Dobredojdovte!")
    else:
        print("Access denied.")
def b(g):
    return True if g=="CS50" else False
pas()