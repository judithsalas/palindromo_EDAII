def es_palindromo(texto):
    # Convertir el texto a minúsculas y eliminar espacios y caracteres especiales
    texto_limpio = ''.join(caracter.lower() for caracter in texto if caracter.isalnum())
    
    # Comparar el texto limpio con su versión invertida
    return texto_limpio == texto_limpio[::-1]

# Solicitar al usuario que ingrese el texto
frase = input("Introduce una palabra o frase para verificar si es un palíndromo: ")

# Verificar si es un palíndromo y mostrar el resultado
if es_palindromo(frase):
    print(f'"{frase}" es un palíndromo')
else:
    print(f'"{frase}" no es un palíndromo')
