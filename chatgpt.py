# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 19:21:39 2023

@author: Ye Jian_cheng
"""
import openai

openai.api_key ="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" #"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"


def GetRispostaGpt(query):
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":query}]
        )

    return response['choices'][0]['message']['content']




#ris=GetRispostaGpt("mi riassumi la prima guerra mondiale in poche parole")
#print(ris)

    
    
    