# -*- coding: utf-8 -*-
"""
@author: DieL
"""
from lib2to3.pgen2 import driver
import random
from time import sleep
from selenium import webdriver
import pandas as pd
from clases import Items


'''url_list = ['3216547','1234568','9876541','7894563','6549812']

for link in url_list:
    sleep(0.5)
    botón = driver.find_element_by_xpath(link)
    botón.click()'''




if __name__ == '__main__':
    
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.maximize_window()
    driver.implicitly_wait(20)

    driver.get('https://evemarketer.com')

    sleep(random.uniform(5.0, 10.0))
    
    item = Items(driver, código='2951909')
    item.capturar_datos()
    
    
    vespel_link = '/html/body/div/div[2]/div[1]/div/div/div[1]/div[2]/ul/li[6]/div/ul/li[2]/div/ul/li[9]/div/ul/li[5]/div/ul/li[19]/div/ul/li[9]/h5/a'
    vespel = driver.find_element_by_xpath(vespel_link)
    vespel_nombre = driver.find_element_by_xpath(vespel_link).text
    vespel.click()
    
    vespel_link_buy = '/html/body/div/div[2]/div[2]/div/div[2]/ul/li[2]/h4/a'
    vespel = driver.find_element_by_xpath(vespel_link_buy)
    vespel.click()
    print(f"..........................\nEl nombre almacenado en vespel_nombre es: {vespel_nombre} \n..........................")

    sleep(random.uniform(2.0, 3.0))

    columnas = ["Precio", "Ubicación"]
    lista = pd.DataFrame(columns=columnas) #/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]
    
    precio = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[3]').text
    ubicación = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[4]/span[1]').text
    
    print(f"El precio: {precio} y la ubicación: {ubicación}")
    lista = lista.append({'Precio' : precio , 'Ubicación' : ubicación} , ignore_index=True)

    

