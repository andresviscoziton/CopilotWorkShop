### Plan

1. Crear un archivo `README.md`.
2. Incluir una sección de introducción.
3. Explicar cómo probar los archivos `.py`.
4. Incluir ejemplos de buen y mal prompting para GitHub Copilot.

### Código

```markdown
# Guía para Probar Archivos `.py` y Buenas Prácticas de Prompting

## Introducción

Este documento explica cómo probar los archivos `.py` y proporciona ejemplos de buenas y malas prácticas de prompting para GitHub Copilot.

## Cómo Probar Archivos `.py`

Para probar los archivos `.py`, sigue estos pasos:

1. Abre una terminal en el directorio donde se encuentran los archivos.
2. Ejecuta el archivo que deseas probar usando el comando `python nombre_del_archivo.py`.

Por ejemplo, para probar `m_p_1.py`, usa el siguiente comando:

```sh
python m_p_1.py
```

## Buenas Prácticas de Prompting

### Ejemplo de Buen Prompting ([`b_p_1.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fandy%2FPYTHON%2FZITON%2FWorkShop%2FCopilotWorkShop%2Fb_p_1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%229d9bd4fb-cf38-453e-9ba4-cecb4cc3c059%22%5D "/home/andy/PYTHON/ZITON/WorkShop/CopilotWorkShop/b_p_1.py"))

Un buen prompting es claro y específico, proporcionando suficiente contexto para que GitHub Copilot entienda lo que se necesita.

```python
# b_p_1.py

def contar_palabras(texto):
    """
    Cuenta el número de palabras en un texto dado.

    Args:
    texto (str): El texto a analizar.

    Returns:
    int: El número de palabras en el texto.
    """
    palabras = texto.split()
    return len(palabras)

# Ejemplo de uso
texto = "Hola, bienvenido al taller de GitHub Copilot."
numero_de_palabras = contar_palabras(texto)
print(f"Número de palabras: {numero_de_palabras}")
```

### Ejemplo de Mal Prompting ([`m_p_1.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fandy%2FPYTHON%2FZITON%2FWorkShop%2FCopilotWorkShop%2Fm_p_1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%229d9bd4fb-cf38-453e-9ba4-cecb4cc3c059%22%5D "/home/andy/PYTHON/ZITON/WorkShop/CopilotWorkShop/m_p_1.py"))

Un mal prompting es vago y carece de contexto, lo que puede llevar a resultados incorrectos o inesperados.

```python
# m_p_1.py

def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

# Ejemplo de uso
texto = "Hola, bienvenido al taller de GitHub Copilot."
numero_de_palabras = contar_palabras(texto)
print(f"Número de palabras: {numero_de_palabras}")
```

En el ejemplo de mal prompting, la falta de documentación y contexto puede dificultar que GitHub Copilot proporcione sugerencias precisas.
