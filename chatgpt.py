# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 19:21:39 2023

@author: Ye Jian_cheng
"""
import openai

openai.api_key ="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"


def GetRispostaGpt(query):
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":query}]
        )

    return response['choices'][0]['message']['content']




#ris=GetRispostaGpt("mi riassumi la prima guerra mondiale in poche parole")
#print(ris)

    
    
    