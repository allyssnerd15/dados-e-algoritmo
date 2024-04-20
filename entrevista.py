#Desafio
#Jogando cartas foras
'''
Dada uma pilha de n cartas enumeradas de 1 até n com a carta no topo e a carta n na base. A seguinte operação é realizada
enquanto tiver 2 ou mais cartas na pilha.
Jogue fora a carta do topo e mova a proxima carta(a que ficou no topo para base da pilha)
'''


while True:
    n  = int(input())
    if n == 0:
        break
    
    cartas = [i for i in range(n, 0, -1)]
    discarded = []
    
    while len(cartas) >= 2:
        discarded.append(cartas.pop())
        cartas.insert(0, cartas.pop())
        
    print('Discarded: ' + ','.join(map(str(discarded))))
    
    print(f'Remaining card: {cartas[0]}')
 
    

'''
Entrada:
    Havera NC(1<=NC<=30) caso de teste. EM cada caso de teste de entrada haverá um par de numeros inteiros positivos
    n(1<=n<=10000) e k(1<=k<=1000). O numero n representa a quantidade de pessoas no circulo, numeradas de 1 ate n.
    O numero k representa o tamanho do salto de um homem até o proximo homem que será morto.
'''

#Pior pratica para Big O
casos = int(input())

for i in range(casos):
    qtd_people, step = list(map(int, input().split(' ')))

    #lista circular
    people = [i for i in range(1, qtd_people + 1)]

    atual = 0
    morto = 0

    while len(people) > 1:
        morto = atual + (step - 1)
        while morto >= len(people):
            morto = morto - len(people)
        people.pop(morto)

        atual = morto
        if atual >= len(people):
            atual = atual - len(people)
            
            
    print(f'Case {i+1}: {people[0]}')
  

#Melhor pratica para Big O
def josephus(n, k):
    # Condição de parada: quando há apenas uma pessoa, ela será o último sobrevivente
    if n == 1:
        return 1
    # Aplicando a fórmula de recorrência para calcular a posição do último sobrevivente
    return (josephus(n - 1, k) + k - 1) % n + 1

# Lendo o número de casos de teste
NC = int(input("Digite o número de casos de teste: "))

# Iterando sobre os casos de teste
for _ in range(NC):
    # Lendo os valores de n e k para o caso de teste atual
    n, k = map(int, input("Digite o valor de n e k separados por espaço: ").split())
    # Chamando a função josephus para o caso de teste atual e imprimindo o resultado
    print("A última pessoa sobrevivente é:", josephus(n, k))


'''A exceção RecursionError: maximum recursion depth exceeded ocorre quando o limite de profundidade de recursão
é ultrapassado'''

#Corrigido
def josephus(n, k):
    # Inicializando a posição do último sobrevivente como 0 (posições de 1 a n)
    last_survivor = 0
    # Iterando sobre os homens de 2 a n
    for i in range(2, n + 1):
        # Atualizando a posição do último sobrevivente para a próxima eliminação
        last_survivor = (last_survivor + k) % i
    # Retornando a posição do último sobrevivente
    return last_survivor + 1

# Lendo o número de casos de teste
NC = int(input("Digite o número de casos de teste: "))

# Iterando sobre os casos de teste
for _ in range(NC):
    # Lendo os valores de n e k para o caso de teste atual
    n, k = map(int, input("Digite o valor de n e k separados por espaço: ").split())
    # Chamando a função josephus para o caso de teste atual e imprimindo o resultado
    print("A última pessoa sobrevivente é:", josephus(n, k))
