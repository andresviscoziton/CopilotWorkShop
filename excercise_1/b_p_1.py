def contar_palabras(texto):
    # Convertir el texto a minúsculas y eliminar signos de puntuación
    texto = texto.lower()
    for char in '-.,\n':
        texto = texto.replace(char, ' ')
    texto = texto.replace('  ', ' ')
    
    # Dividir el texto en palabras
    palabras = texto.split()
    
    # Contar las palabras
    contador = {}
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    
    return contador

# Ejemplo de uso
texto = "Hola, hola. ¿Cómo estás? Estoy bien, gracias. ¿Y tú?"
print(contar_palabras(texto))
