# -*- coding: utf-8 -*-
"""
Creado el martes 11 de junio 23:55:29 2024

@author: Lesby
"""

# Conversion de Coordenadas expresadas  en Grados Decimales (DD) a Grados, Minutos y Segundos (DMS) y viceversa
# comenzamos a realizar los calulos 

def dd_a_dms(dd):
    
    # Calcular grados, minutos y segundos
    grados = int(dd)
    minutos = int((abs(dd) - abs(grados)) * 60)
    segundos = (abs(dd) - abs(grados) - minutos / 60) * 3600
    return grados, minutos, segundos

def dms_a_dd(grados, minutos, segundos):
    
    # Convertir grados, minutos y segundos a grados decimales
    
    dd = abs(grados) + minutos / 60 + segundos / 3600
    if grados < 0:
        dd = -dd
    return dd

def main():
    
    # Preguntar al usuario el tipo de conversión
    tipo_conversion = int(input("Seleccione el tipo de conversión que desea realizar:\n1. DD a DMS.\n2. DMS a DD\n>> "))

    if tipo_conversion == 1:
        # Pedir coordenadas en DD
        lat_dd = float(input("Ingresar el valor de la Latitud en DD\n>> "))
        lon_dd = float(input("Ingresar el valor de la Longitud en DD\n>> "))

        # Convertir a DMS
        lat_grados, lat_minutos, lat_segundos = dd_a_dms(lat_dd)
        lon_grados, lon_minutos, lon_segundos = dd_a_dms(lon_dd)

        lat_hemisferio = 'N' if lat_dd >= 0 else 'S'
        lon_hemisferio = 'E' if lon_dd >= 0 else 'O'

        # Imprimir los resultados
        print(f"El valor de la latitud es:\n\t{abs(lat_grados)}° {lat_minutos}' {lat_segundos:.4f}'' {lat_hemisferio}")
        print(f"El valor de la longitud es:\n\t{abs(lon_grados)}° {lon_minutos}' {lon_segundos:.4f}'' {lon_hemisferio}")

    elif tipo_conversion == 2:
        
        # Pedir coordenadas en DMS
        lat_grados = int(input("Ingresar los grados de la Latitud\n>> "))
        lat_minutos = int(input("Ingresar los minutos de la Latitud\n>> "))
        lat_segundos = float(input("Ingresar los segundos de la Latitud\n>> "))

        lon_grados = int(input("Ingresar los grados de la Longitud\n>> "))
        lon_minutos = int(input("Ingresar los minutos de la Longitud\n>> "))
        lon_segundos = float(input("Ingresar los segundos de la Longitud\n>> "))

        # Convertir a DD
        lat_dd = dms_a_dd(lat_grados, lat_minutos, lat_segundos)
        lon_dd = dms_a_dd(lon_grados, lon_minutos, lon_segundos)


        # Imprimir los resultados
        print(f"El valor de la latitud en DD es: {lat_dd}")
        print(f"El valor de la longitud en DD es: {lon_dd}")

    else:
        print("Opción no válida. Seleccione 1 o 2.")

if __name__ == "__main__":
    main()
    
    

       