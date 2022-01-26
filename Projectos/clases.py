# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 18:16:25 2022

@author: DieL
"""
import pandas as pd

class Mercado_Agrupado:
    def __init__(self) -> None:
        self.ruta_mercado_agrupado = '/html/body/div/div[2]/div[1]/div/div/div[1]/div[2]/ul'

class Fabricación_e_Investigación(Mercado_Agrupado):
    def __init__(self) -> None:
        super().__init__()
        self.ruta_fabricación_e_investigación = self.ruta_mercado_agrupado + '/li[6]'

class Materiales(Fabricación_e_Investigación):
    def __init__(self) -> None:
        super().__init__()
        self.ruta_materiales = self.ruta_fabricación_e_investigación + '/div/ul/li[2]'

class Materias_Primas(Materiales):
    def __init__(self) -> None:
        super().__init__()
        self.ruta_materias_primas = self.ruta_materiales + '/div/ul/li[9]'

class Minerales_de_Hielo(Materias_Primas):
    def __init__(self) -> None:
        super().__init__()
        self.ruta_minerales_de_hielo = self.ruta_materias_primas + '/div/ul/li[3]'

class Minerales_Lunares(Materias_Primas):
    def __init__(self) -> None:
        super().__init__()
        self.ruta_minerales_lunares = self.ruta_materias_primas + '/div/ul/li[4]'

class Minerales_Lunares_Comunes(Minerales_Lunares):
    def __init__(self) -> None:
        super().__init__()
        self.ruta_minerales_lunares_comunes = self.ruta_minerales_lunares + '/div/ul/li[1]'

class Minerales_Lunares_Excepcionales(Minerales_Lunares):
    def __init__(self) -> None:
        super().__init__()
        self.ruta_minerales_lunares_excepcionales = self.ruta_minerales_lunares + '/div/ul/li[2]'

class Minerales_Lunares_Raros(Minerales_Lunares):
    def __init__(self) -> None:
        super().__init__()
        self.ruta_minerales_lunares_raros = self.ruta_minerales_lunares + '/div/ul/li[3]'

class Minerales_Lunares_Ubicuos(Minerales_Lunares):
    def __init__(self) -> None:
        super().__init__()
        self.ruta_minerales_lunares_cubicuos = self.ruta_minerales_lunares + '/div/ul/li[4]'

class Minerales_Lunares_Poco_Comunes(Minerales_Lunares):
    def __init__(self) -> None:
        super().__init__()
        self.ruta_minerales_lunares_poco_comunes = self.ruta_minerales_lunares + '/div/ul/li[5]'

class Minerales_Estandar(Materias_Primas):
    def __init__(self) -> None:
        super().__init__()
        self.ruta_minerales_estandar = self.ruta_materias_primas + '/div/ul/li[5]'

class Arkonor(Minerales_Estandar):
    def __init__(self) -> None:
        super().__init__()
        self.ruta_arkonor = self.ruta_minerales_estandar + '/div/ul/li[1]'

class Bezdnacine(Minerales_Estandar):
    def __init__(self) -> None:
        super().__init__()
        self.ruta_bezdnacine = self.ruta_minerales_estandar + '/div/ul/li[2]'

class Bistot(Minerales_Estandar):
    def __init__(self) -> None:
        super().__init__()
        self.ruta_bistot = self.ruta_minerales_estandar + '/div/ul/li[3]'

class Crokite(Minerales_Estandar):
    def __init__(self) -> None:
        super().__init__()
        self.ruta_crokite = self.ruta_minerales_estandar + '/div/ul/li[4]'

class Dark_Ochre(Minerales_Estandar):
    def __init__(self) -> None:
        super().__init__()
        self.ruta_dark_ochre = self.ruta_minerales_estandar + '/div/ul/li[5]'

class Gneiss(Minerales_Estandar):
    def __init__(self) -> None:
        super().__init__()
        self.ruta_gneiss = self.ruta_minerales_estandar + '/div/ul/li[6]'

class Hedbergite(Minerales_Estandar):
    def __init__(self) -> None:
        super().__init__()
        self.ruta_hedbergite = self.ruta_minerales_estandar + '/div/ul/li[7]'

class Hemorphite(Minerales_Estandar):
    def __init__(self) -> None:
        super().__init__()
        self.ruta_hemorphite = self.ruta_minerales_estandar + '/div/ul/li[8]'



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
