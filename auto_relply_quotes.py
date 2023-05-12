# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:10:10 2023

@author: Ye Jian_cheng
"""
import requests
import TelegramPushFunction as telegramPushfunction
import meteo as meteo
import concurrent.futures

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

def invioQuotes(idchat):
    diz=get_Diz_quotes()
    a,b,c = random_numbers()
    quote = diz[a]
    quote2= diz[b]
    quote3=diz[c]
    formatted_string = "Here the quotes of day \n\n"f'{quote["text"]}\n- {quote["author"]}\n\n\n'f'{quote2["text"]}\n- {quote2["author"]}\n\n\n'f'{quote3["text"]}\n- {quote3["author"]}\n'
    print(formatted_string)
    
    response = telegramPushfunction.send_telegram_message(idchat, formatted_string)
    print(response)
    


def start_work(idchat):
    import time
    import datetime

    idchat=idchat  
    print("Servizio InvioQuotes Start in:"+idchat)
    telegramPushfunction.send_telegram_message("-950282631", "Avvio servizio auto-reply")
    while True:
        
        current_time = time.strftime("%H:%M")
        print(current_time)
        print("Sono le",current_time)
        now = datetime.datetime.now()
        print("Current date and time:", now)
        
        
        if(current_time=="06:00"):
            print("entrato")
            telegramPushfunction.send_telegram_message(idchat, "Buongiorno Principesse Triviali, sono le 8:00 , Ecco il meteo e quotes per la giornata")
            telegramPushfunction.send_telegram_message(idchat,meteo.get_meteo_info("verona") )
            
            
            telegramPushfunction.send_telegram_message(idchat,meteo.get_meteo_info("scorzè") )
            telegramPushfunction.send_telegram_message(idchat,meteo.get_meteo_info("padova") )
                
            invioQuotes(idchat)
        if(current_time=="18:00"):
            telegramPushfunction.send_telegram_message(idchat, "Buonasera Pandames come è stata la giornata(di merda?), VI SOLLEVO IO IL MORALE CON FRASI ora è:\n"+str(now))
            invioQuotes(idchat)
        if(current_time=="11:00"):
            for i in range(0,1):
                telegramPushfunction.send_telegram_message(idchat, "Basta lavorare,pranzo time")
                invioQuotes(idchat)
                
        if(current_time=="08:30"):
            for i in range(0,2):
                telegramPushfunction.send_telegram_message(idchat, "Sono le 10:30, BASTA LAVORARE, pausa time e state al caldo")
                 
        if(current_time=="02:00"):
            telegramPushfunction.send_telegram_message(idchat, " Sono le 4.00, vado a dormire che tra due ore devo prendere treno Bologna-Padova ")
        
        if(current_time=="22:00"):
            telegramPushfunction.send_telegram_message(idchat, " Bene, sono le 0.00, vado a lavorare. Faccio un tiro fino le sei e poi treno")
           
            
        s="Waiting for the next Quotes renewal...at min'8.00 and 20:00"
        print(s)
        #return s #!!!!non fai ritornare nulla cosi continua XD
      
            
        time.sleep(60)  #fa uno sleep cosi almeno è sicuro che fa solo 1 volta il task se dovesse finire entro 1 min
        print("__________________________________")

with concurrent.futures.ThreadPoolExecutor() as worker :
    #w1=worker.submit(start_work,"-1001496914346") #zibaldone
    w2=worker.submit(start_work,"-1001941753443") #pandamemm group
    w3=worker.submit(start_work,"-985535170") #venezia
    #w4=worker.submit(start_work,"-950282631") #t1 prova
    
    
    
    #print(w1.result())
    print(w2.result())
    print(w3.result())
    #print(w4.result())
    

################################################################


     
#t1=start_work("-1001496914346")  # zibaldone =-1001496914346, pandmemem = -1001941753443 #venezia="-985535170"

#t2=start_work("-1001941753443") 




