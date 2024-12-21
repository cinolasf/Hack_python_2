"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""

def fn_hack_7(s):
    if s == [0]:  # Si la lista contiene solo el número 0
        return [0]
    
    result = []
    for i in range(len(s)):
        data = i + 1
        if i % 2 == 0:  # Índices pares
            result.append(str(data))  # Convertir a string
        else:  # Índices impares
            result.append(data)  # Mantener como número entero
    
    return result

# Ejemplos de uso
print(fn_hack_7(["a", "b", "c", "d", "e"]))  # Output: ['1', 2, '3', 4, '5']
print(fn_hack_7([0]))                         # Output: [0]
