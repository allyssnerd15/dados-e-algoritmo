#Essa função faz a conta de quantos elementos iguais tenho em uma lista e em outra, trazendo o resultado(valores) em outra lista
#exemplo: 
#string = ['ab', 'ab', 'abc'] and queries = ['ab', 'abc', 'bc' ]
#resultado = [2, 1, 0]


def matching_strings(strings, queries):
    results = []
    for i in range(len(queries)):
        count = 0
        for j in range(len(strings)):
            if strings[j] == queries[i]:
                count += 1
        results.append(count)
    return results
    
    
strings = ['ab', 'ab', 'abc']
queries = ['ab', 'abc', 'bc' ]

print(matching_strings(strings, queries))