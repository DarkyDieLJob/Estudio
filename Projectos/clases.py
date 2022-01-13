# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 18:16:25 2022

@author: DieL
"""
import pandas as pd
class _Item():

    def __init__(self, 
            nombre,  
            volumen, 
            precio_estimado, 
            precio_de_mercado, ) -> None:
        
        self.nombre = nombre
        self.volumen = volumen
        self.precio_estimado = precio_estimado
        self.precio_de_mercado = precio_de_mercado

class Minerales(_Item):

    def __init__(self, 
            nombre,  
            volumen, 
            precio_estimado, 
            precio_de_mercado, 
            tiempo_de_minado, ) -> None:
        self.tiempo_de_minado = tiempo_de_minado
        super().__init__(nombre,  
            volumen, 
            precio_estimado, 
            precio_de_mercado,) 
