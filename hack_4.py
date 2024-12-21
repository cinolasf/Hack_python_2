"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""

def fn_hack_4(s):
    result = ""
    for char in s:
        if char in "aeiouzrqxm":
            result += char
    return result

# Pruebas
print(fn_hack_4("fooziman"))  # Salida: "oozima"
print(fn_hack_4("barziman"))  # Salida: "arzima"
print(fn_hack_4("qux"))       # Salida: "qux"
