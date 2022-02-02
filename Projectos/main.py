# -*- coding: utf-8 -*-
"""
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

    f.guardar_df(datos,ruta)

    f.valor_venta(datos)


    # print(datos[['Nombre_Mineral', 'Cantidad_Hora', 'Valor_Estimado_Hora']])
    # f.debuguear(debug, "Hola", 0)
    g.grafico_barras(
        f.pasar_grafico(datos), 
        'Mineral', 
        'Valor', 
        'Sistema'
    ) 