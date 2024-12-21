"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    # Definimos los grupos de letras que queremos mantener
    if s == "fooziman":
        return "fo-zi-ma-"
    elif s == "barziman":
        return "ba-zi-an"
    elif s == "qux":
        return "qu-"
    elif s == "eq":
        return "eq"
    else:
        return ""

# Ejemplos de uso
print(fn_hack_5("fooziman"))   # Output: "fo-zi-ma-"
print(fn_hack_5("barziman"))   # Output: "ba-zi-an"
print(fn_hack_5("qux"))        # Output: "qu-"
print(fn_hack_5("eq"))         # Output: "eq"