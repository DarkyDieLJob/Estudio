import funciones as f
#import pandas as pd


if __name__ == '__main__':
    
    ruta = 'datos/dataframe.csv'
    
    #potencia_minado = int(input('Indique su potencia de minado total; '))
        
    datos = f.chequear_df(ruta)
    
    #f.datos_minerales(datos, potencia_minado)
    
    f.valor_venta(datos)
    
    f.guardar_df(datos,ruta)
    
    #print(datos[['Nombre_Mineral', 'Cantidad_Hora', 'Valor_Estimado_Hora']])