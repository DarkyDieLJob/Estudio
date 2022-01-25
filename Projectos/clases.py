# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 18:16:25 2022

@author: DieL
"""
import pandas as pd




class _M():
    
    def __init__(self) -> None:
        self.link_m = "link carpeta M / "


class M_link(_M):

    def __init__(self) -> None:
        super().__init__()
        self.link_M_link = self.link_m + "link de la carpeta M_link"
        self.ruta = self.link_m + self.link_M_link

if __name__ == '__main__':

    m = M_link()
    n = _M()
    
    def imprimir(m):
        print(f" El atriburo ruta de M: {m.link_m}")    
        print(f" El atriburo ruta de M_link: {m.link_M_link}")
        print(f" El atriburo ruta completo: {m.ruta}")

    imprimir(m)
    imprimir(n)
