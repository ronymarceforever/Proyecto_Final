# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 23:11:03 2022

@author: Antony Urcullo Rosales

### Importar Dependencias y Credeciales para acceder a kaggle
"""

import json
import os
import pandas as pd
import matplotlib as plt
import plotly.express as px
import numpy as np

def sh(script):
    os.system("bash -c '%s'" % script)
    
def download():
  
 # Definir las credentiales para acceder a Kaggle. Primero requerimos confirmar que el archivo aún no ha sido creado
 KAGGLE_PATH = "./.kaggle" 

 if os.path.exists(KAGGLE_PATH):
  sh("rm -r "+KAGGLE_PATH)
  
 sh("mkdir "+KAGGLE_PATH)
 sh("touch "+KAGGLE_PATH+"/kaggle.json")

  # Puedes crear tu propio token y username de la API de Kaggle en https://www.kaggle.com/
 api_token = {"username":"antonyurcullo","key":"25cac0013320ab9ac731c80ae7e13510"}

  # Crear un archivo con las credenciales, de tal forma que kaggle pueda leerlas facilmente
 with open(KAGGLE_PATH+'/kaggle.json', 'w') as file:
      json.dump(api_token, file)

  # Cambiar los permisos de acceso del nuevo archivo con credenciales
 sh("chmod 600 "+ KAGGLE_PATH +"/kaggle.json")

  # Comprobar si el conjunto de datos ya se ha descargado
 if not os.path.exists('./dataset'):
    # Crear una nueva carpeta
    os.makedirs('dataset')
 else: 
    # Reemplazar carpeta previamente descargada
   sh("rm -r "+ 'dataset')
   os.makedirs('dataset')

  # Descargar un dataset desde Kaggle
 sh("kaggle datasets download -d tawsifurrahman/covid19-radiography-database -p dataset")
  # Descomprimir dataset 
 sh("unzip './dataset/covid19-radiography-database.zip' -d ./dataset")
 sh("rm ./dataset/covid19-radiography-database.zip")

#download()

