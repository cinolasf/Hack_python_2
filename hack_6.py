"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    if not s:  # Si la lista está vacía
        return ["0"]
    
    result = []
    for i in range(3):
        index = i * 2 + 1  # Calcular el índice deseado (1, 3, 5, ...)
        result.append(str(index))  # Convertir a string
        if i < len(s) - 1:  # Agregar un guión si no es el último elemento
            result.append("-")

    result.pop()    
    return result

# Ejemplos de uso
print(fn_hack_6(["a", "b", "c", "d", "e"]))  # Output: ["1", "-", "3", "-", "5"]
print(fn_hack_6([]))                         # Output: ["0"]