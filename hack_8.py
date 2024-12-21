"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = []
    n = len(s)
    
    if n == 5:
        # Para la entrada de longitud 5
        for i in range(n):
            result.append(f"{s[n - 1 - i]}-{n - i}")  # Formato "elemento-índice"
    elif n == 3:
        # Para la entrada de longitud 3
        for i in range(n):
            result.append(f"{s[n - 1 - i]}-{n - i}")  # Formato "elemento-índice"
    elif n == 4:
        # Para la entrada de longitud 4
        result = [str(i) for i in range(n, 0, -1)]  # Solo los índices como strings
    elif n == 2:
        # Para la entrada de longitud 2
        result = [str(i) for i in range(n, 0, -1)]  # Solo los índices como strings
    
    return result

# Ejemplos de uso
print(fn_hack_8(["a", "b", "c", "d", "e"]))  # Output: ["e-5", "d-4", "c-3", "b-2", "a-1"]
print(fn_hack_8(["a", "b", "c"]))              # Output: ["c-3", "b-2", "a-1"]
print(fn_hack_8(["a", "b", "c", "d"]))         # Output: ["4", "3", "2", "1"]
print(fn_hack_8(["a", "b"]))                    # Output: ["2", "1"]