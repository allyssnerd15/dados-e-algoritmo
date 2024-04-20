
#Inverto os 

def reverse_array_1(a):
    b = []
    for i in a:
        b.insert(0, i)
    return b

def reverse_array_2(a):
    return a[::-1]

def reverse_array_3(a):
    a = a.revese()
    return a

a = [1, 2 ,3 ,4 ,5]