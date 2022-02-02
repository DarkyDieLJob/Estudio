# -*- coding: utf-8 -*-
"""
@author: DieL
"""
import pandas as pd
from lib2to3.pgen2 import driver
import random
from time import sleep
from selenium import webdriver


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
                                      'Valor_Amarr',
                                      'Valor_Amarr_Hora',
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
        df = pd.DataFrame(columns=['Jita', 'Amarr'])
        print('Comenzemos por Jita: ')
        df['Jita'] = (leer_datos_venta())
        print('Sigamos con Amarr: ')
        df['Amarr'] = (leer_datos_venta())


        datos = datos.loc[datos.Valor_Jita!=df['Jita'],
                          'Valor_Jita'] = df['Jita']
        datos = datos.loc[datos.Valor_Amarr!=df['Amarr'],
                          'Valor_Amarr'] = df['Amarr']
    else:
        datos['Valor_Jita'] = (895000, 3804, 226400, 15540, 205700)
        datos['Valor_Amarr'] = (605000, 3200, 200000, 5001, 113100)

    datos['Valor_Jita_Hora'] = (
        datos['Cantidad_Hora']*datos['Valor_Jita'] )
    datos['Valor_Amarr_Hora'] = (
        datos['Cantidad_Hora']*datos['Valor_Amarr'] )
    print(datos[['Nombre_Mineral',
                 'Valor_Jita_Hora',
                 'Valor_Amarr_Hora', ]])
    return None


def pasar_grafico(datos):
    dfaux = pd.DataFrame(columns=['Mineral', 'Sistema', 'Valor'])
    dfaux2 = pd.DataFrame(columns=['Mineral', 'Sistema', 'Valor'])
    dfaux[['Mineral','Valor']] = datos[['Nombre_Mineral', 'Valor_Jita_Hora']]
    dfaux['Sistema'] = 'Jita'
    dfaux2[['Mineral','Valor']] = datos[['Nombre_Mineral', 'Valor_Amarr_Hora']]
    dfaux2['Sistema'] = 'Amarr'
    dfaux = dfaux.append(dfaux2)
    return dfaux


def clikear(driver, ruta):
    item = driver.find_element_by_xpath(ruta)
    item.click()
    sleep(0.5)


def iterar_código(driver, código,dic):
    print(f'###################\n\nCódigo: {código}\n')
    ruta = '/html/body/div/div[2]/div[1]/div/div/div[1]/div[2]/ul/li[6]'
    cont = 0
    dígito = ''
    item = ''
    clikear(driver, ruta)
    for i in código:
        cont += 1
        # print(f'Contador está en {cont}')
        if cont!=4 or cont!=6:
            n = int(i)

            if cont==5:
                n = int(dígito + i)
            elif cont==7:
                n = int(item + i)


            # ruta
            index = str(cont)
            
            if 0<cont<6 and cont!=4:
                if n>0:
                    ruta = ruta + f'/div/ul/li[{n}]'
                    if not(n in dic[index]):
                        dic[index].add(n)
                        clikear(driver, ruta)
            elif n>0 and cont==7:
                    ruta = ruta + f'/div/ul/li[{n}]/h5/a'
                    clikear(driver, ruta)
            # print(f'cont {cont}')

        if cont==4:
            # print(f'cont {cont}')
            dígito = i
            # print(f'digito {dígito} en contador {cont}')
        
        if cont==6:
            # print(f'cont {cont}')
            item = i
            # print(f'item {item} en contador {cont}')

    return ruta


def extraer_datos_items(driver, ruta):
    
    nombre = driver.find_element_by_xpath(ruta).text
#    precio_venta = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/ul/li[1]/h4/a')


    
    '''diccionario = {
        'nombre':nombre, 
        'volumen':volumen, 
        'omega':omega, 
        'precio_compra':precio_compra, 
        'ubicación_compra':ubicación_compra, 
        'precio_venta':precio_venta, 
        'ubicación_venta':ubicación_venta, 
        'categoría':categoría,
        }'''
        
    return nombre
    


def guardar_dic_conjuntos(dic):
    # print(f'Diccionario creado: \n {dic}')
    ruta = 'C:/Users/DieL/Documents/GitHub/Estudio/Projectos/datos/dic.csv'
    try:
        # print(f'Diccionario antes de leer: \n {dic}')
        df_dic = pd.read_csv(str(ruta))
        dic = df_dic.set_index('Posición').T.to_dict('list')
        for i in dic:
            dic[i] = set(dic[i]) 
    except:
        pass
    # print(f'Diccionario después de leer: \n {dic}')
    for i in dic:
            dic[i] = list(dic[i])

    # print(f'Diccionario Antes de guardar: \n {dic}')
    df_dic = pd.DataFrame.from_dict(dic, orient='index')
    # print(f'DF Antes de Transposicionar: \n {df_dic}')
    df_dic = df_dic.transpose()
    # print(f'DF Después de Transposicionar: \n {df_dic}')
    guardar_df(df_dic, ruta)


if __name__ == '__main__':
    
    