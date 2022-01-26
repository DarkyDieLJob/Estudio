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


def iterar_código(código,dic):
    print(f'###################\n\nCódigo: {código}\n')
    link = '/html/body/div/div[2]/div[1]/div/div/div[1]/div[2]/ul/li[6]'
    cont = 0
    dígito = ''
    item = ''
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
            
            if 0<cont<6:
                if n>0:
                    link = link + f'/div/ul/li[{n}]'
                    if not(n in dic[index]):
                        dic[index].add(n)
                        print(f'Se clikeo en la ruta: {link} y se adirió {n} a "{index}"')
            elif n>0 and cont==7:
                    link = link + f'/h{n}/a]'
                    print(f'Se clikeo en El item: {link} y se adirió {n} a "{index}"')
            # print(f'cont {cont}')

        if cont==4:
            # print(f'cont {cont}')
            dígito = i
            # print(f'digito {dígito} en contador {cont}')
        
        if cont==6:
            # print(f'cont {cont}')
            item = i
            # print(f'item {item} en contador {cont}')

    return print(f'\nLa ruta completa es: {link}\n')


if __name__ == '__main__':
    dic = {'1':set(),'2':set(),'3':set(),'4':set(),'5':set()}
    iterar_código('2250015',dic)
    iterar_código('2130004',dic)
    iterar_código('3150022',dic)