Las herramientas de codificación con IA generativa están transformando la forma en que los desarrolladores abordan las tareas de codificación diarias. Desde documentar nuestras bases de código hasta generar pruebas unitarias, estas herramientas están ayudando a acelerar nuestros flujos de trabajo. Sin embargo, como con cualquier tecnología emergente, siempre hay una curva de aprendizaje. Como resultado, los desarrolladores, tanto principiantes como experimentados, a veces se sienten frustrados cuando los asistentes de codificación impulsados por IA no generan el resultado que quieren. (¿Te suena familiar?)

Por ejemplo, al pedirle a GitHub Copilot que dibuje un cono de helado 🍦 usando p5.js, una biblioteca de JavaScript para codificación creativa, seguimos recibiendo sugerencias irrelevantes, o a veces ninguna sugerencia en absoluto. Pero cuando aprendimos más sobre la forma en que GitHub Copilot procesa la información, nos dimos cuenta de que teníamos que ajustar la forma en que nos comunicábamos.

Aquí hay un ejemplo de GitHub Copilot generando una solución irrelevante:

When we wrote this prompt to GitHub Copilot, 

Cuando ajustamos nuestra instrucción, pudimos generar resultados más precisos:

When we wrote this prompt to GitHub Copilot, 

Somos tanto desarrolladoras como entusiastas de la IA. Yo, Rizel, he utilizado GitHub Copilot para construir una extensión de navegador; un juego de piedra, papel o tijera; y para enviar un tweet. Y yo, Michelle, lancé una compañía de IA en 2016. Ambas somos DevRel en GitHub y nos encanta compartir nuestros mejores consejos para trabajar con GitHub Copilot.

En esta guía para GitHub Copilot, cubriremos:

Qué es exactamente un “prompt” y qué es la ingeniería de prompts (pista: depende de si estás hablando con un desarrollador o con un investigador de aprendizaje automático)
Tres mejores prácticas y tres consejos adicionales para la creación de prompts con GitHub Copilot
Un ejemplo donde puedes probar a GitHub Copilot para que te ayude en la construcción de una extensión de navegador
Progreso sobre perfección
Incluso con nuestra experiencia usando IA, reconocemos que todos están en una fase de prueba y error con la tecnología de IA generativa. También conocemos el desafío de proporcionar consejos generales de elaboración de prompts porque los modelos varían, al igual que los problemas individuales en los que los desarrolladores están trabajando. Esta no es una guía definitiva. En su lugar, estamos compartiendo lo que hemos aprendido sobre la elaboración de prompts para acelerar el aprendizaje colectivo durante esta nueva era del desarrollo de software.

¿Qué es un “prompt” y qué es la ingeniería de prompt?
Depende de con quién hables.

En el contexto de las herramientas de codificación de IA generativa, un prompt puede significar diferentes cosas, dependiendo de si está preguntando a los investigadores de aprendizaje automático (ML) que están construyendo y ajustando estas herramientas, o a los desarrolladores que las están usando en sus IDE.

Para esta guía, definiremos los términos desde el punto de vista de un desarrollador que utiliza una herramienta de codificación de IA generativa en el IDE. Pero para brindarle una imagen completa, también agregamos las definiciones de investigador de ML a continuación.

Prompts	Ingenieria de Prompt	Contexto
Desarrollador	Bloques de código, líneas individuales de código, o comentarios en lenguaje natural que un desarrollador escribe para generar una sugerencia específica de GitHub Copilot.	Proporcionar instrucciones o comentarios en el IDE para generar sugerencias de código específicas	Detalles que proporciona un desarrollador para especificar la prompt deseada de una herramienta de codificación generativa de IA
Investigador de ML	Compilación de código de IDE y contexto relevante (comentarios de IDE, código en archivos abiertos, etc.) que se genera continuamente por algoritmos y se envíaal modelo de una herramienta de codificación generativa de IA	Creación de algoritmos que generarán prompts (compilaciones de código de IDE y contexto) para un modelo de lenguaje de gran tamaño	Detalles (como datos de tus archivos abiertos y código que has escrito antes y después del curso) que los algoritmos envían a un modelo de lenguaje de gran tamaño (LLM) como información adicional sobre el código
3 mejores prácticas para la elaboración de prompts con GitHub Copilot
1. Establecer el escenario con un objetivo de alto nivel. 🖼️
Esto es más útil si tienes un archivo en blanco o una base de código vacía. En otras palabras, si GitHub Copilot no tiene ningún contexto de lo que quieres construir o lograr, establecer el escenario para el programador par de IA puede ser realmente útil. Ayuda a preparar a GitHub Copilot con una descripción general de lo que quieres que genere, antes de que te sumerjas en los detalles.

Al hacer prompts, GitHub Copilot, piensa en el proceso como si estuvieras teniendo una conversación con alguien: ¿Cómo debería desglosar el problema para que podamos resolverlo juntos? ¿Cómo abordaría la programación en pareja con esta persona?

Por ejemplo, al construir un editor de markdown en Next.js, podríamos escribir un comentario como este:


//
Crea un editor de markdown básico en Next.js con las siguientes características:
- Utiliza hooks de React
- Crea un estado para markdown con texto predeterminado "escribe markdown aquí"
- Un área de texto donde los usuarios pueden escribir markdown
- Muestra una vista previa en vivo del texto de markdown mientras escribo
- Soporte para la sintaxis básica de markdown como encabezados, negrita, cursiva
- Utiliza el paquete npm de React markdown
- El texto de markdown y el HTML resultante deben guardarse en el estado del componente y actualizarse en tiempo real 
*/
Esto hará que GitHub Copilot genere el siguiente código y produzca un muy editor de rebajas simple, sin estilo pero funcional en menos de 30 segundos. Podemos usar el tiempo restante para diseñar el componente:

We used this prompt to build a markdown editor in Next.js using GitHub Copilot: - Use react hooks - Create state for markdown with default text 

Nota: Este nivel de detalle te ayuda a crear una prompt más deseada, pero los resultados aún pueden ser no deterministas. Por ejemplo, en el comentario, solicitamos a GitHub Copilot que cree un texto predeterminado que diga “escribe markdown aquí”, pero en cambio generó “vista previa de markdown” como las palabras predeterminadas.

2. Haz tu solicitud simple y específica. Apunta a recibir una prompt corta de GitHub Copilot. 🗨️
Una vez que comunicas tu objetivo principal al programador par AI, articula la lógica y los pasos que debe seguir para alcanzar ese objetivo. GitHub Copilot comprende mejor tu objetivo cuando desglosas las cosas. (Imagina que estás escribiendo una receta. Desglosarías el proceso de cocción en pasos discretos, no escribirías un párrafo describiendo el plato que quieres hacer.)
Deja que GitHub Copilot genere el código después de cada paso, en lugar de pedirle que genere un montón de código de una sola vez.
Aquí tienes un ejemplo de cómo proporcionamos a GitHub Copilot instrucciones paso a paso para invertir una función:

We prompted GitHub Copilot to reverse a sentence by writing six prompts one at a time. This allowed GitHub Copilot to generate a suggestion for one prompt before moving onto the text. It also gave us the chance to tweak the suggested code before moving onto the next step. The six prompts we used were: First, let's make the first letter of the sentence lower case if it's not an 'I.' Next, let's split the sentence into an array of words. Then, let's take out the punctuation marks from the sentence. Now, let's remove the punctuation marks from the sentence. Let's reverse the sentence and join it back together. Finally, let's make the first letter of the sentence capital and add the punctuation marks.

3. Proporciona a GitHub Copilot uno o dos ejemplos. ✍️
Aprender de ejemplos no solo es útil para los humanos, sino también para tu programador par AI. Por ejemplo, queríamos extraer los nombres del siguiente arreglo de datos y almacenarlos en un nuevo arreglo:


const data = [
  [
    { name: 'John', age: 25 },
    { name: 'Jane', age: 30 }
  ],
  [
    { name: 'Bob', age: 40 }
  ]
];
Cuando no le mostramos un ejemplo a GitHub Copilot …


// Mapee a través de una matriz de matrices de objetos para transformar datos
const data = [
  [
    { name: 'John', age: 25 },
    { name: 'Jane', age: 30 }
  ],
  [
    { name: 'Bob', age: 40 }
  ]
];
Generó un uso incorrecto del mapa:


const mappedData = data.map(x => [x.name](http://x.name/));

console.log(mappedData);

// Results: [undefined, undefined]
Por el contrario, cuando proporcionamos un ejemplo…


// Recorrer un array de arrays de objetos
// Ejemplo: Extraer los nombres del array de datos
// Resultado deseado: ['John', 'Jane', 'Bob']
const data = [
  [{ name: 'John', age: 25 }, { name: 'Jane', age: 30 }],
  [{ name: 'Bob', age: 40 }]
];
Recibimos nuestro resultado deseado.


const mappedData = data.flatMap(sublist => sublist.map(person => person.name));

console.log(mappedData);
// Results: ['John', 'Jane', 'Bob'] 
Lee más acerca de los enfoques comunes para el entrenamiento de IA, como el aprendizaje de zero-shot, one-shot, and few-shot learning.

Tres consejos adicionales para la elaboración de prompts con GitHub Copilot
Aquí tienes tres consejos adicionales para ayudarte a guiar tu conversación con GitHub Copilot.

1. Experimenta con tus prompts.
Al igual que la conversación es más un arte que una ciencia, también lo es la elaboración de prompts. Así que, si no recibes lo que quieres en el primer intento, reformula tu prompts siguiendo las mejores prácticas mencionadas anteriormente.

Por ejemplo, la prompts de abajo es vaga. No proporciona ningún contexto ni límites para que GitHub Copilot genere sugerencias relevantes.


# Escribe algo de código para grades.py
Iteramos en el prompt para ser más específicos, pero aún no obtuvimos el resultado exacto que estábamos buscando. Este es un buen recordatorio de que añadir especificidad a tu prompt es más difícil de lo que parece. Es difícil saber, desde el principio, qué detalles debes incluir sobre tu objetivo para generar las sugerencias más útiles de GitHub Copilot. Por eso animamos a la experimentación.

La versión del promopt de abajo es más específica que la de arriba, pero no define claramente los requisitos de entrada y salida.


# Implementar una función en grades.py para calcular la nota media
Experimentamos una vez más con el promopt estableciendo límites y delineando lo que queríamos que hiciera la función. También reformulamos el comentario para que la función fuera más clara (dándole a GitHub Copilot una intención clara contra la que verificar).

Esta vez, obtuvimos los resultados que estábamos buscando.


# Implementa la función calculate_average_grade en grades.py que toma una lista de calificaciones como entrada y devuelve la calificación media como un número flotante.
2. Mantén un par de pestañas relevantes abiertas.
No tenemos un número exacto de pestañas que debas mantener abiertas para ayudar a GitHub Copilot a contextualizar tu código, pero en nuestra experiencia, hemos encontrado que una o dos es útil.

GitHub Copilot utiliza una técnica llamada pestañas vecinas que permite al programador de pares de IA contextualizar su código procesando todos los archivos abiertos en su IDE en lugar de solo el archivo en el que está trabajando. Sin embargo, no se garantiza que GItHub Copilot considere todos los archivos abiertos como contexto necesario para su código.

3. Utilice buenas prácticas de codificación.
Eso incluye proporcionar nombres y funciones de variables descriptivas, y seguir estilos y patrones de codificación consistentes. Hemos descubierto que trabajar con GitHub Copilot nos anima a seguir las buenas prácticas de codificación que hemos aprendido a lo largo de nuestras carreras.

Por ejemplo, aquí usamos un nombre de función descriptiva y seguimos los patrones de la base de código para aprovechar el caso de la serpiente.


def authenticate_user(nombre de usuario, contraseña):
Como resultado, GitHub Copilot generó una sugerencia de código relevante:


def authenticate_user(nombre de usuario, contraseña):
    # Código para autenticar al usuario
    Si is_valid_user(nombre de usuario, contraseña):
        generate_session_token(nombre de usuario)
        return True
    más:
        return Falso
Compare esto con el siguiente ejemplo, donde introdujimos un estilo de codificación inconsistente y mal nombramos nuestra función.


def rndpwd(l):
En lugar de sugerir código, GitHub Copilot generó un comentario que decía: “El código va aquí”.


def rndpwd(l):
    # El código va aquí
Mantente inteligente
Los LLM detrás de las herramientas generativas de codificación de IA están diseñados para encontrar y extrapolar patrones de sus datos de entrenamiento, aplicar esos patrones al lenguaje existente y luego producir código que siga esos patrones. Dada la gran escala de estos modelos, podrían generar una secuencia de código que ni siquiera existe todavía. Al igual que revisaría el código de un colega, siempre debe evaluar, analizar y validar el código generado por IA.

Un ejemplo 👩🏽 💻 de práctica
Intenta pedirle a GitHub Copilot que cree una extensión del navegador.

Para comenzar, deberás tener GitHub Copilot instalado y abierto en tu IDE. También tenemos acceso a una vista previa temprana del chat de GitHub Copilot, que es lo que hemos estado usando cuando tenemos preguntas sobre nuestro código. Si no tienes el chat de GitHub Copilot, regístrate en la lista de espera. Hasta entonces, puede emparejar GitHub Copilot con ChatGPT.

Guías de elaboración de avisos de IA más generativas</h2:
<0l>
Una guía para principiantes sobre ingeniería rápida con GitHub Copilot
Ingeniería rápida para IA
Cómo GitHub Copilot está mejorando en la comprensión de tu código
