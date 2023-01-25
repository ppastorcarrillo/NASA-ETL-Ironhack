import missingno as msno
import pandas as pd
import numpy as np
import calendar
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import datetime
import re
pd.options.display.max_columns = None
from collections import Counter
from fuzzywuzzy import process, fuzz
import pickle



def eliminar_columnas(df, columna):
    """
    df : dataframe to use
    columna : column to delete
    return: dataframe without the column
    
    """
    return df.drop( columna, axis=1, inplace = True)



def nulos_graficos(tabla):
    """
    tabla : data frame to use
    return: graphic showing the Nan/null values 
    """
    return msno.matrix(tabla)


def abrir_csv(nombre,camino):
    """
    nombre : how to name the data frame
    camino : Path
    return : the data frame first 5 rows
    """
    nombre = pd.read_csv(camino)
    return nombre.head()






def eliminar_nulos(columna):
    """
    functio to change Nan/null values
    columna: column to changa Nan
    media: mean of the column
    mediana: median of the column
    mensaje : change with median or mean, choose "si" or "no"
    return: the dataframe with the columns without nulls
    """
    media = columna.mean()
    mediana = columna.median()
    mensaje =input( print("sustituir con la mediana, si = mediana , no = media") )
    if mensaje == "si":
        return columna.replace(np.nan, columna.median(), inplace = True)
    if mensaje == "no":
        return columna.replace(np.nan, columna.mean(), inplace = True)
    else:
        return print("SI O NO??")



###SCRAPING
"""
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import warnings
warnings.filterwarnings('ignore')



opciones= Options()
opciones.add_experimental_option('excludeSwitches', ['enable-automation'])
#para ocultarme como robot
opciones.add_experimental_option('useAutomationExtension', False)
opciones.add_argument('--start-maximized') #empezar maximizado
opciones.add_argument('user.data-dir=selenium') #guarda las cookies
#.add_argument('--incognito')#incognito window


#scraping = {"name" : [],"photo" : [], "description" : [], "discovery date" : []}

for planeta in planetas:
    if planeta not in scraping["name"]:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://exoplanets.nasa.gov/exep/search.html?q=")
        driver.implicitly_wait(5)
        driver.find_element("css selector", "#gsc-i-id1").click()
        driver.find_element("css selector", "#gsc-i-id1").send_keys(f"{planeta}", Keys.TAB)
        driver.find_element("css selector", "#___gcse_0 > div > div > form > table > tbody > tr > td.gsc-search-button").click()
        ##no en todos es el primer resultado

        try:
                driver.find_element("css selector", "#___gcse_0 > div > div > div > div.gsc-wrapper > div.gsc-resultsbox-visible > div > div > div.gsc-expansionArea > div:nth-child(1) > div.gs-webResult.gs-result > div.gsc-thumbnail-inside > div > a").click()

                #dentro del planeta
                scraping["description"].append(driver.find_element("css selector", "#primary_column > div.wysiwyg_content > p").text)
                scraping["discovery date"].append(driver.find_element("css selector", "#secondary_column > table > tbody > tr:nth-child(1) > td:nth-child(2) > div.value").text)
                scraping["name"].append(planeta)
        except:
                driver.back() #vuelve a la pagina anterior
                driver.find_element("css selector", "#gsc-i-id1").click()
                driver.find_element("css selector", "#gsc-i-id1").send_keys(f"{planeta}", Keys.TAB)
                driver.find_element("css selector", "#___gcse_0 > div > div > form > table > tbody > tr > td.gsc-search-button").click()
                driver.find_element("css selector", "#___gcse_0 > div > div > div > div.gsc-wrapper > div.gsc-resultsbox-visible > div > div > div.gsc-expansionArea > div:nth-child(2) > div.gs-webResult.gs-result > div.gsc-thumbnail-inside > div > a").click()

            #dentro del planeta
                
                scraping["description"].append(driver.find_element("css selector", "#primary_column > div.wysiwyg_content > p").text)
                scraping["discovery date"].append(driver.find_element("css selector", "#secondary_column > table > tbody > tr:nth-child(1) > td:nth-child(2) > div.value").text)
                scraping["name"].append(planeta)
    else:
        pass

"""




























