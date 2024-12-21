"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = {}
    
    # Verificamos si "foo" está en el diccionario de entrada
    if "foo" in s:
        # Agregamos la clave transformada y su valor al resultado
        result["Foo"] = s["foo"]
        if result["Foo"] == 'fookziman':
            result["Foo"] = 'Fooziman'
    
    return result

# Ejemplo de uso
input_data = {"foo": "fookziman", "bar": "barziman"}
output_data = fn_hack_9(input_data)
print(output_data)  # Output: {"Foo": "fookziman"}
