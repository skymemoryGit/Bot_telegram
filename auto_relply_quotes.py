# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:10:10 2023

@author: Ye Jian_cheng
"""
import requests
import TelegramPushFunction as telegramPushfunction
import meteo as meteo

def get_Diz_quotes():
    import json

    # Open the JSON file and load the data
    with open('quotes/quotes.json', 'r') as f:
        data = json.load(f)

    # Create an empty list to store the quotes
    quotes = []

    # Loop through each quote in the data
    for quote in data:
        # Extract the text and author of the quote
        text = quote['text']
        author = quote['author']
        # Add the quote to the list as a dictionary
        quotes.append({'text': text, 'author': author})
        
    return quotes
    




def random_numbers():
    import random
    return (random.randint(0, 1643), random.randint(0, 1643), random.randint(0, 1643))

def invioQuotes():
    diz=get_Diz_quotes()
    a,b,c = random_numbers()
    quote = diz[a]
    quote2= diz[b]
    quote3=diz[c]
    formatted_string = "Here the quotes of day \n\n"f'{quote["text"]}\n- {quote["author"]}\n\n\n'f'{quote2["text"]}\n- {quote2["author"]}\n\n\n'f'{quote3["text"]}\n- {quote3["author"]}\n'
    print(formatted_string)
    
    response = telegramPushfunction.send_telegram_message("-1001941753443", formatted_string)
    print(response)
    




################################################################

import time
import datetime

print("Servizio InvioQuotes Start")
while True:
    
    current_time = time.strftime("%H:%M")
    print(time)
    print("Sono le",current_time)
    if(current_time=="8:00" or current_time=="20:00" or current_time=="13:00" or current_time=="10:30"):
        now = datetime.datetime.now()
        print("Current date and time:", now)
        if(current_time=="8:00"):
            telegramPushfunction.send_telegram_message("-1001941753443", "Buongiorno Principesse, sono le 8:00 , ecco il meteo e quotes per la giornata")
            telegramPushfunction.send_telegram_message("-1001941753443",meteo.get_meteo_info("verona") )
            telegramPushfunction.send_telegram_message("-1001941753443",meteo.get_meteo_info("scorzè") )
            invioQuotes()
        if(current_time=="20:00"):
            telegramPushfunction.send_telegram_message("-1001941753443", "Buonasera Pandames, ora è:\n"+str(now))
            invioQuotes()
        if(current_time=="13:00"):
            telegramPushfunction.send_telegram_message("-1001941753443", "Basta lavorare,pranzo time")
            
        if(current_time=="10:30"):
             telegramPushfunction.send_telegram_message("-1001941753443", "Sono le 10:30, pausa time e state al caldo")
             
        
        '''
        if current_time.endswith(":40"): #se sono le 40'
            
            print("Sono le 40, Faccio update")
            print("Running task at", current_time)
        '''   
        
    else:
        print("Waiting for the next Quotes renewal...at min'8.00 and 20:00")
  
        
    time.sleep(60)  #fa uno sleep cosi almeno è sicuro che fa solo 1 volta il task se dovesse finire entro 1 min
    print("__________________________________")
     







