# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 18:16:25 2022

@author: DieL
"""
from lib2to3.pgen2 import driver
import random
from time import sleep
from selenium import webdriver
import pandas as pd
from sklearn.covariance import ledoit_wolf_shrinkage



def expandir_lista():
    url_base = '/html/body/div/div[2]/div[1]/div/div/div[1]/div[2]/ul/li[6]'
    url_list = []
    
    for i in range(6):
        if i == 0:
            url_list = [url_base]

        elif i == 1:
            url_base = url_base + '/div/ul/li[2]'
            url_list.append(url_base)

        elif i == 2:
            url_base = url_base + '/div/ul/li[9]'
            url_list.append(url_base)

        elif i == 3:
            url_aux = url_base + '/div/ul/li[3]'
            url_list.append(url_aux)

        elif i == 4:
            url_aux = url_base + '/div/ul/li[4]'
            url_list.append(url_aux)
            for j in range(5):
                url_aux2 = url_aux + f'/div/ul/li[{j+1}]'
                url_list.append(url_aux2)

        elif i == 5:
            url_aux = url_base + '/div/ul/li[5]'
            url_list.append(url_aux)
            for j in range(19):
                url_aux2 = url_aux + f'/div/ul/li[{j+1}]'
                url_list.append(url_aux2)
        


    for link in url_list:
        sleep(0.5)
        botón = driver.find_element_by_xpath(link)
        botón.click()




if __name__ == '__main__':
    
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.maximize_window()
    driver.implicitly_wait(20)

    driver.get('https://evemarketer.com')

    sleep(random.uniform(5.0, 10.0))
    
    expandir_lista()
    vespel_link = '/html/body/div/div[2]/div[1]/div/div/div[1]/div[2]/ul/li[6]/div/ul/li[2]/div/ul/li[9]/div/ul/li[5]/div/ul/li[19]/div/ul/li[9]/h5/a'
    vespel = driver.find_element_by_xpath(vespel_link)
    vespel.click()
    vespel_link_buy = '/html/body/div/div[2]/div[2]/div/div[2]/ul/li[2]/h4/a'
    vespel = driver.find_element_by_xpath(vespel_link_buy)
    vespel.click()


    print("\n")
    print("Vespel:")
    print(vespel)
    print("...")
    


    sleep(random.uniform(2.0, 3.0))

    columnas = ["Precio", "Ubicación"]
    lista = pd.DataFrame(columns=columnas) #/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]
    precio = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[3]').text
    ubicación = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[4]/span[1]').text
    print(f"El precio: {precio} y la ubicación: {ubicación}")
    lista = lista.append({'Precio' : precio , 'Ubicación' : ubicación} , ignore_index=True)

    print("\n\n")
    print(lista)
    print("\n\n")

