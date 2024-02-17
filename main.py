import os
from telebot import TeleBot

"""
COLOQUE AQUI O TOKEN DO BOTFATHER, COMO STRING
PUT HERE THE BOTFATHER TOKEN, AS A STRING
"""
TOKEN = os.environ.get('BOT_TOKEN')
bot = TeleBot(TOKEN)

# Variáveis globais
waiting_for_first_number = True
first_number = None
operation = None

# Funções auxiliares
@bot.message_handler(commands=['start', 'Start', 'olá', 'Olá'])
def send_welcome(message):
    bot.reply_to(message, "Olá, eu sou o bot calculadora!")

# Funções de cálculo
@bot.message_handler(commands=['soma', 'Soma'])
def soma(message):
    global waiting_for_first_number
    global first_number
    global operation
    
    waiting_for_first_number = True
    first_number = None
    operation = 'soma'
    
    bot.reply_to(message, "Digite o primeiro número inteiro:")

@bot.message_handler(commands=['subtracao', 'Subtracao'])
def sub(message):
    global waiting_for_first_number
    global first_number
    global operation
    
    waiting_for_first_number = True
    first_number = None
    operation = 'sub'
    
    bot.reply_to(message, "Digite o primeiro número inteiro:")

@bot.message_handler(func=lambda message: waiting_for_first_number)
def handle_first_number(message):
    global waiting_for_first_number
    global first_number

    try:
        first_number = int(message.text)
        waiting_for_first_number = False
        bot.reply_to(message, "Digite o segundo número inteiro:")
    except ValueError:
        bot.reply_to(message, "Por favor, digite um número inteiro válido.")

@bot.message_handler(func=lambda message: not waiting_for_first_number)
def handle_second_number(message):
    global first_number
    global operation

    try:
        second_number = int(message.text)
        print("Operation: ", operation) 
        if operation == 'soma':
            result = first_number + second_number
            bot.reply_to(message, f"A soma de {first_number} e {second_number} é {result}.")
        elif operation == 'sub':
            result = first_number - second_number
            bot.reply_to(message, f"A subtração de {first_number} e {second_number} é {result}.")
    except ValueError:
        bot.reply_to(message, "Por favor, digite um número inteiro válido.")

# Tratamento de exeção
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    user_message = message.text
    response = f"Desculpe, não reconheço '{user_message}' como comando."
    bot.reply_to(message, response)

bot.infinity_polling()
