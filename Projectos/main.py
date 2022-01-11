# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 18:16:25 2022

@author: DieL
"""
from logging import debug
import funciones as f
import graficos as g




if __name__ == '__main__':

    debug=True

    ruta = 'C:/Users/DieL/Documents/GitHub/Estudio/Projectos/datos/dataframe.csv'

    potencia_minado = int(input('Indique su potencia de minado total; '))

    datos = f.chequear_df(ruta)

    f.datos_minerales(datos, potencia_minado)

    f.valor_venta(datos)

    f.guardar_df(datos,ruta)

    # print(datos[['Nombre_Mineral', 'Cantidad_Hora', 'Valor_Estimado_Hora']])
    f.debuguear(debug, "Hola", 0)


    g.app.run_server(debug=True)
