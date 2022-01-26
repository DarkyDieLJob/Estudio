# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 18:16:25 2022

@author: DieL
"""
from funciones import iterar_código, extraer_datos_items, guardar_dic_conjuntos


class Items():
    def __init__(self,driver, código=None, nombre=None, volumen=None, omega=None, precio_compra=None, ubicación_compra=None,
             precio_venta=None, ubicación_venta=None, categoría=None) -> None:
        self.driver = driver
        self.código = código
        self.nombre = nombre
        self.volume = volumen
        self.omega = omega
        self.precio_compra = precio_compra
        self.ubicación_compra = ubicación_compra
        self.precio_venta = precio_venta
        self.ubicación_venta = ubicación_venta
        self.categoría = categoría

    def capturar_datos(self, diccionario={'1':set(),'2':set(),'3':set(),'4':set(),'5':set()}):
        ruta = iterar_código(self.driver, self.código, diccionario)
        self.nombre = extraer_datos_items(self.driver, ruta)
        guardar_dic_conjuntos(diccionario)
        

class Minerales(Items):
    def __init__(self, código, nombre, volumen, omega, precio_compra, ubicación_compra, precio_venta, ubicación_venta, categoría, volumen_equivalente) -> None:
        super().__init__(código, nombre, volumen, omega, precio_compra, ubicación_compra, precio_venta, ubicación_venta, categoría)
        self.volumen_equivalente = volumen_equivalente



if __name__ == '__main__':

    
