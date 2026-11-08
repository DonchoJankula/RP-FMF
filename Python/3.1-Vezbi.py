def broj():
    x=even(float(input("Vnesi broj ")))
    if x:
        print("Even")
    else:
        print("odd")

def even(d):
    return True if d % 2==0 else False
broj()