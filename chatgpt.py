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



def audio_to_text(path_fileaudio):
    import openai
    audio_file= open(path_fileaudio, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    ris=transcript["text"]
    return ris 
#ris=GetRispostaGpt("mi riassumi la prima guerra mondiale in poche parole")
#print(ris)

    
    
    