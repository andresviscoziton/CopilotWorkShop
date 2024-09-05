def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

# Ejemplo de uso
texto = "Hola, bienvenido al taller de GitHub Copilot."
numero_de_palabras = contar_palabras(texto)
print(f"Número de palabras: {numero_de_palabras}")