"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import pandas as pd
import os
def pregunta_01():
    df = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";",index_col=0)
    df = df.copy()
    
    df["sexo"] = df["sexo"]
    df["sexo"] = df["sexo"].str.strip()
    df["sexo"] = df["sexo"].str.lower()
    df["sexo"] = df["sexo"].str.replace("-", "")
    
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"]
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.replace("-", " ")
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.replace("_", " ")
    

    df["idea_negocio"] = df["idea_negocio"]
    df["idea_negocio"] = df["idea_negocio"].str.lower()
    df["idea_negocio"] = df["idea_negocio"].str.replace("-", " ")
    df["idea_negocio"] = df["idea_negocio"].str.replace("_", " ")
    
    #        )
    
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], dayfirst= True, format='mixed')

    df['estrato'] = df['estrato'].astype("category")

    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype("int")
    
    df["barrio"] = df["barrio"]
    df["barrio"] = df["barrio"].str.lower()
    df["barrio"] = df["barrio"].str.replace("-", " ")
    df["barrio"] = df["barrio"].str.replace("_", " ")
    
    df["monto_del_credito"] = df["monto_del_credito"]
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(",", "")
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(".00", "")
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(" ", "")
    df["monto_del_credito"] = df["monto_del_credito"].str.strip("$")
             
    
    df["línea_credito"] = df["línea_credito"]
    df["línea_credito"] = df["línea_credito"].str.lower()
    df["línea_credito"] = df["línea_credito"].str.replace("-", " ")
    df["línea_credito"] = df["línea_credito"].str.replace("_", " ")
   

    df = df.drop_duplicates()
    df=df.dropna()
    if not os.path.exists("files/output"):
        os.makedirs("files/output")
    df.to_csv("files/output/solicitudes_de_credito.csv", sep=";", index=False)

    


 
pregunta_01()





"""
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
