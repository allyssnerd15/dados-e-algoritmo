from typing import List
import re 

'''Dadas duas matrizes classificadas nums1e nums2de tamanho me nrespectivamente, retorne a mediana das duas matrizes classificadas.

A complexidade geral do tempo de execução deve ser O(log (m+n)).

 

Exemplo 1:

Entrada: nums1 = [1,3], nums2 = [2]
 Saída: 2,00000
 Explicação: array mesclado = [1,2,3] e mediana é 2.
Exemplo 2:

Entrada: nums1 = [1,2], nums2 = [3,4]
 Saída: 2,50000
 Explicação: array mesclado = [1,2,3,4] e a mediana é (2 + 3) / 2 = 2,5.
 

Restrições:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106'''


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            #import pdb; pdb.set_trace()
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            mid1 = (left + right) // 2
            mid2 = (m + n + 1) // 2 - mid1
            
            max_left_nums1 = float('-inf') if mid1 == 0 else nums1[mid1 - 1]
            min_right_nums1 = float('inf') if mid1 == m else nums1[mid1]
            max_left_nums2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]
            min_right_nums2 = float('inf') if mid2 == n else nums2[mid2]

            if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
                if (m + n) % 2 == 0:
                    return (max(max_left_nums1, max_left_nums2) + min(min_right_nums1, min_right_nums2)) / 2
                else:
                    return max(max_left_nums1, max_left_nums2)
            elif max_left_nums1 > min_right_nums2:
                right = mid1 - 1
            else:
                left = mid1 + 1

# Exemplo de uso:
solution = Solution()
print(solution.findMedianSortedArrays([1, 3], [2]))   # Saída: 2.0
print(solution.findMedianSortedArrays([1, 2], [3, 4])) # Saída: 2.5



'''Dada uma string s, retorne o mais longo 
palindrômico
 
substring
em s.

 

Exemplo 1:

Entrada: s = "babad"
 Saída: "bab"
 Explicação: "aba" também é uma resposta válida.
Exemplo 2:

Entrada: s = "cbbd"
 Saída: "bb"
 

Restrições:

1 <= s.length <= 1000
sconsistem apenas em dígitos e letras em inglês.'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        start = 0
        max_len = 0

        for i in range(len(s)):
            # Verificamos para substrings de comprimento ímpar
            len1 = self.expand_around_center(s, i, i)
            # Verificamos para substrings de comprimento par
            len2 = self.expand_around_center(s, i, i + 1)

            # Pegamos o comprimento máximo entre os dois tipos de substrings
            length = max(len1, len2)

            # Se encontrarmos uma substring maior, atualizamos o ponto de partida e o comprimento máximo
            if length > max_len:
                max_len = length
                start = i - (length - 1) // 2

        return s[start:start + max_len]

    def expand_around_center(self, s: str, left: int, right: int) -> int:
        # Expandimos para a esquerda e direita enquanto os caracteres forem iguais
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Retornamos o comprimento da substring palindrômica encontrada
        return right - left - 1

# Exemplo de uso:
solution = Solution()
print(solution.longestPalindrome("babad"))  # Saída: "bab" ou "aba"
print(solution.longestPalindrome("cbbd"))   # Saída: "bb"



'''Um número válido pode ser dividido nestes componentes (em ordem):

Um número decimal ou um número inteiro .
(Opcional) Um 'e'ou 'E', seguido por um número inteiro .
Um número decimal pode ser dividido nestes componentes (em ordem):

(Opcional) Um caractere de sinal (ou '+') '-'.
Um dos seguintes formatos:
Um ou mais dígitos, seguidos de um ponto '.'.
Um ou mais dígitos, seguidos de um ponto '.', seguidos de um ou mais dígitos.
Um ponto '.', seguido por um ou mais dígitos.
Um número inteiro pode ser dividido nestes componentes (em ordem):

(Opcional) Um caractere de sinal (ou '+') '-'.
Um ou mais dígitos.
Por exemplo, todos os números a seguir são válidos: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], enquanto os seguintes não são números válidos: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Dada uma string s, retorne truese sfor um número válido .

 

Exemplo 1:

Entrada: s = "0"
 Saída: verdadeiro
Exemplo 2:

Entrada: s = "e"
 Saída: falso
Exemplo 3:

Entrada: s = "."
 Saída: falso
 

Restrições:

1 <= s.length <= 20
sconsiste apenas em letras inglesas (maiúsculas e minúsculas), dígitos ( 0-9), mais '+', menos '-'ou ponto '.'.'''

class Solution:
    def isNumber(self, s: str) -> bool:
        # Expressão regular para verificar se a string representa um número válido
        pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
        
        # Verifica se a string corresponde ao padrão
        return re.match(pattern, s) is not None

# Exemplo de uso:
solution = Solution()
print(solution.isNumber("0"))   # Saída: True
print(solution.isNumber("e"))   # Saída: False
print(solution.isNumber("."))   # Saída: False



#Max subarray problem
'''
Encontre o subarray contiguo de maior valor.

Array
[5, 6, -15, 2, 4, -1, 12, -8]

subaaray
[5] -> Sum: 5

[5, 6] -> Sum: 11

[6, -15, 2] -> Sum: -7

[2, 4, -1, 12] -> Sum: 17

'''
#Pior pratica para big O
#Complexidade
# O(n**3)

#x = [5, 6, -15, 2, 4, -1, 12, -8]
from random import randint
import time

x = [randint(-100, 100) for i in range(100)]

start = time.perf_counter()
min_value = float('-inf')
for i in range(len(x)):
    for j in range(i, len(x)):
        soma = 0
        for k in range(i, j+1):
            soma += x[k]
            
        if soma > min_value:
            min_value = soma
 
end = time.perf_counter()            
print(min_value)
print(end-start)



#Melhor pratica de big O
x = [5, 6, -15, 2, 4, -1, 12, -8]

max_sum = x[0]
actually_sum = x[0]

for i in range(1, len(x)):
    if actually_sum + [i] > x[i]:
        actually_sum += x[i]
    else:
        actually_sum = x[i]
        
    if actually_sum > max_sum:
        max_sum = actually_sum
print(max_sum)