# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 16:44:04 2023

@author: Ye Jian_cheng
"""
# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from random import choice
from glob import glob

# Open an Image


import numpy as np
from PIL import Image, ImageDraw, ImageFont






def creaCustomPandaMeme(img,testo): #questo metodo prende img e testo e crea uno nuovo di nome result.png 
    # Open input image
    
    
    #print(len(testo))
    
    if(len(testo)>15):
        parole=testo.split(" ")
        
        static_world= parole[0]+" "+parole[1]+" "+parole[2]+" \n"
        
        testoacapo=""
        for i in range(3,len(parole)): 
            testoacapo= testoacapo+parole[i]+" "
        #print(testoacapo)
        
        final=static_world+testoacapo
        #print(final)
        
        testo=final
        

    im = Image.open(img).convert('RGB')

    # Get a drawing context
    draw = ImageDraw.Draw(im)

    pixellat=ImageFont.truetype("verdana",48)
    draw.text((45, 20),testo,(0,0,0),font=pixellat)

    # Save
    im.save('img/pandamem/result.png')
    


#creaCustomPandaMeme("img/pandamem/hhh.png", "zanon è un frocio di merda")

