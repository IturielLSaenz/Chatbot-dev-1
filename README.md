# 📦 Chatbot-dev-1

Chatbot-dev-1 es un chatbot básico de consola desarrollado en Python como ejercicio de aprendizaje. Simula la interacción de un asistente automatizado para atender preguntas frecuentes de una papelería local, registrando además todas las conversaciones en archivos de texto.

## 📌 Descripción

Este proyecto permite al usuario interactuar con el chatbot por consola, realizar preguntas predefinidas y recibir respuestas automatizadas. Cada sesión de conversación se guarda en un archivo de texto individual dentro de la carpeta `/chatlogs/`, nombrado con el nombre del usuario, fecha y un identificador aleatorio.

## 🛠️ Tecnologías

- **Python 3.11+**
- Estructuras de datos: diccionarios
- Manejo de archivos (`open`, `write`, `close`)
- Módulos estándar:
  - `datetime`
  - `random`
  - `string`
  - `os`
  - `sys`

## 📁 Estructura del proyecto

```bash
/Chatbot-dev-1/
├── main.py # Código principal del chatbot
├── data.py # Diccionario con las preguntas y respuestas
├── /chatlogs/ # Carpeta donde se guardan los logs de conversación
└── README.md # Este archivo
```
## 🚀 Ejecución

1. Clonar el repositorio:

```bash
git clone https://github.com/IturielLSaenz/Chatbot-dev-1.git
cd Chatbot-dev-1
```
2. Ejecutar el chatbot:

```bash
python main.py
```
Al finalizar una conversación, se generará un archivo .txt en /chatlogs/ con el historial de la sesión.

## 📋 Ejemplo de uso
```makefile
Chatbot: Hola buen día.
Chatbot: ¿Cuál es tu nombre?
Tú: Juan
Chatbot: Mucho gusto Juan...
Chatbot: Estas son las preguntas más frecuentes:
¿cuáles son sus horarios?
¿dónde se ubican?
...

Tú: ¿cuáles son sus horarios?
Chatbot: Nuestro horario es de lunes a viernes de 9:00 a 18:00 hrs.
```
## 📦 Funcionalidades
- Saludo inicial personalizado

- Listado de preguntas frecuentes

- Respuestas automatizadas desde un diccionario (data.py)

- Manejo de salida con comandos "salir" o "adiós"

- Registro de toda la conversación en archivos .txt personalizados por sesión

## 📌 Autor
Desarrollado por Ituriel Liebes Sáenz

## 📝 Licencia
Este proyecto se desarrolló como ejercicio de aprendizaje y no cuenta con una licencia formal. Uso libre para fines educativos o de práctica.
