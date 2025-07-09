# --------
# Sistema Chatbot básico.
# Autor: Ituriel Liebes Sáenz
# Github: IturielLSaenz
# Tech Stack: Python
# Fecha creación: 09/07/2025 - 9:28 a.m
# Ultima modificación: 09/07/2025 - 11:00 a.m
# --------

from data import data # lectura del banco de respuestas.

from datetime import datetime
import random
import string

import os

if not os.path.exists("chatlogs"):
    os.makedirs("chatlogs")


isRunning:bool# variable para el bucle while
user_name:str # variable para el nombre de usuario

# ---- Funciones ----
#Función para manejar el saludo al usuario.
def salute():
    print("Chatbot: Hola buen día. \nChatbot: ¿Cuál es tu nombre?")
    user_name = input('Tú: ')
    print(f"Chatbot: Mucho gusto {user_name}, con qué puedo ayudarte el día de hoy?\nA continuación verás una lista de las preguntas frecuentes:")
    return user_name
#Función para desplegar las preguntas frecuentes
def faqDisplay():
    faq = data.keys()
    for i in faq:
        print('\n'+ i)

#Función para manejar las preguntas y respuestas del usuario
def process_handler(log):
    question = input('Tú: ').lower()
    log.write(f"Tú: {question}\n")# <- escribiendo en el archivo
    if question in ['salir','adiós']:
        log.write("Terminando el programa...")# <- escribiendo en el archivo
        print("Terminando el programa...")
        log.close()
        exit()
    answer = data.get(question,"Chatbot: Lo siento, no he entendido tu pregunta!")
    log.write(f"Chatbot: {answer}\n")# <- escribiendo en el archivo
    print('Chatbot: ',answer)

#Función para manejar la lógica detrás del chatbot     
def chatbot():
    user_name = salute()

    fecha = datetime.now().strftime("%d%m%y")
    aleatorio = str(random.randint(0, 9)) + random.choice(string.ascii_lowercase)
    file_name = f"chatlogs/{user_name}{fecha}{aleatorio}.txt"

    log = open(file_name, "w", encoding="utf-8")
    faqDisplay()
    process_handler(log)
    log.write("Chatbot: ¿Hay algo más con lo que te pueda ayudar? (Si/No)")
    print("Chatbot: ¿Hay algo más con lo que te pueda ayudar? (Si/No)")
    answer = input('Tú: ').lower()
    log.write(f"Tú: {answer}\n") # <- escribiendo en el archivo
    if answer == 'si':
        isRunning = True
    elif answer == 'no':
        isRunning = False
        log.write("Terminando el programa...") # <- escribiendo en el archivo
        print("Terminando el programa...")
        exit()
    # inicio del bucle while
    while isRunning == True:
        print("\nChatbot: Estas son las preguntas más frecuentes: ")
        faqDisplay()
        go_on = process_handler(log) # variable que determina si debe continuar o no
        if go_on == False:
            print("\nTerminando la conversación...")
            break
        # Continuar con el bucle:
        log.write("Chatbot: ¿Hay algo más con lo que te pueda ayudar? (Si/No)")
        print("Chatbot: ¿Hay algo más con lo que te pueda ayudar? (Si/No)")
        answer = input('Tú: ').lower()
        log.write(f"Tú: {answer}\n")
        if answer == 'si':
            isRunning == True
        elif answer == 'no':
            log.write("Terminando el programa...")
            print("Terminando la conversación...")
            break
        

# --- EJECUCIÓN ----
if __name__ == "__main__":
    chatbot()



