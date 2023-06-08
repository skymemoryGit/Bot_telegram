# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 09:08:48 2023

@author: Ye Jian_cheng
"""
def set_ON_OFF_state_gpt_vocal_function():
    filename = "configurazione/gpt_on_off.txt"
    
    # Legge il contenuto del file
    with open(filename, 'r') as file:
        content = file.read().strip()

    # Inverte lo stato
    if content == "on":
        new_state = "off"
    elif content == "off":
        new_state = "on"
    else:
        print("Lo stato del file non è valido.")
        return

    # Scrive il nuovo stato nel file
    with open(filename, 'w') as file:
        file.write(new_state)

    ris=f"Lo stato del file è stato invertito da '{content}' a '{new_state}'."
    return ris


#set_ON_OFF_state_gpt_vocal_function()