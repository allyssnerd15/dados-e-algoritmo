
#Percorro a lista da posição 1 a penultima posição para alterar a posição de um dado da lista

def left_rotation(a, d):
    return a[d:] + a[:d]

a = [1, 2, 3, 4, 5]
print(left_rotation(a, 2))