# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 18:16:25 2022

@author: DieL
"""
import pandas as pd


def debuguear(debug, cadena, dato):
    '''
    Dado un atributo debug: boolean, imprime la cadena y los datos 
    suministrados.
    '''
    if debug:
        print(cadena)
        print(dato)


def chequear_df(ruta):
    try:
        datos = pd.read_csv(str(ruta))
    except:
        datos = pd.DataFrame(columns=['Nombre_Mineral',
                                      'Peso_Crudo',
                                      'Peso_Compactado',
                                      'Cantidad_Hora',
                                      'Valor_Estimado',
                                      'Valor_Estimado_Hora',
                                      'Valor_Jita',
                                      'Valor_Jita_Hora',
                                      'Valor_Ammar',
                                      'Valor_Ammar_Hora',
                                      ])
    return datos


def guardar_df(df,ruta):
    df.to_csv(ruta, index=False)


def datos_minerales(df,pm):
    df['Nombre_Mineral'] = ('Crokite',
                            'Pyroxeres',
                            'Bistol',
                            'Omber',
                            'Arkonor', )
    df['Peso_Crudo'] = (16.0,
                        0.3,
                        16.0,
                        0.6,
                        16.0, )
    df['Peso_Compactado'] = df['Peso_Crudo']*100
    df['Cantidad_Hora'] = 60 // (df['Peso_Compactado']/pm)
    df['Valor_Estimado'] = (912000,
                            3340,
                            226000,
                            15500,
                            186000, )
    df['Valor_Estimado_Hora'] = (
        df['Cantidad_Hora']*df['Valor_Estimado'] )

    return df


def leer_datos_venta():
    lista = (input('Compressed Crokite: '),
    input('Compressed Pyroxeres: '),
    input('Compressed Bistol: '),
    input('Compressed Omber: '),
    input('Compressed Arkonor: '))
    return lista


def valor_venta(datos):
    if (input("Actualizar valores de venta True/False: ")) == "True":
        df = pd.DataFrame(columns=['Jita', 'Ammar'])
        print('Comenzemos por Jita: ')
        df['Jita'] = (leer_datos_venta())
        print('Sigamos con Ammar: ')
        df['Ammar'] = (leer_datos_venta())


        datos = datos.loc[datos.Valor_Jita!=df['Jita'],
                          'Valor_Jita'] = df['Jita']
        datos = datos.loc[datos.Valor_Ammar!=df['Ammar'],
                          'Valor_Ammar'] = df['Ammar']
    else:
        datos['Valor_Jita'] = (895000, 3804, 226400, 15540, 205700)
        datos['Valor_Ammar'] = (605000, 3200, 200000, 5001, 113100)

    datos['Valor_Jita_Hora'] = (
        datos['Cantidad_Hora']*datos['Valor_Jita'] )
    datos['Valor_Ammar_Hora'] = (
        datos['Cantidad_Hora']*datos['Valor_Ammar'] )
    print(datos[['Nombre_Mineral',
                 'Valor_Jita_Hora',
                 'Valor_Ammar_Hora', ]])
