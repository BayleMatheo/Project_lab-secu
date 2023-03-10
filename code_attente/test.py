def test():
    a=2
    b=10
    x=a*b
    print(x)

def test1():
    a=2
    b=100
    x=a*b
    print(x)

def test2():
    a=2
    b=1000
    x=a*b
    print(x)

def test5():
    texte = []
    texte1 = []
    texte += ["a","b"]
    texte1 += ["b"]
    print(texte + texte1)
    """exte -= texte1"""
    print(texte1)
    print(texte)

def test10():
    a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","_"]
    b = ["y"]

    for item in b:
        if item in a:
            a.remove(item)

    print(a)

test()
test1()
test2()
test5()
test10()