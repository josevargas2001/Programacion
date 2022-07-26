# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 12:20:06 2022

@author: lab
"""
import os, json # <-- nuevo

inventario = {}

def write_json(filename): # <-- nuevo (toda la funcion)
    with open(filename, 'w') as f:
        json.dump(inventario, f, ensure_ascii=False, indent=2)

def agregar():
    cod = input("Ingresa un codigo para el producto: ")
    if cod not in inventario:
        pr_nom = input("Ingresa el nombre del producto: ")
        pr_can = int(input("Cantidad del producto: "))
        inventario[cod] = [pr_nom, pr_can]
        write_json(db_file) # <-- nuevo
        print("Producto agregado!!")
    else:
        print("[!] Lo sentimos, ya hay un producto con este código")
    
def buscar():
    encontrados = [] # Encontrado
    cod = input("Buscar por CODIGO (deje vacio para buscar por nombre): ")
    if cod:
        if cod in inventario:
            encontrados.append([cod, inventario[cod]])
    else:
        buscar = input("Buscar por NOMBRE de producto: ")
        for cod, prod in inventario.items():
            nom_prod = prod[0]
            if nom_prod.lower().find(buscar.lower()) >= 0:
                encontrados.append([cod, inventario[cod]])
    if encontrados:
        print("- Producto encontrado -")
        for elem in encontrados:
            print(f"COD# {elem[0]} --- {elem[1][0]} --- CANT: {elem[1][1]}")
    else:
        print("[!] El producto no se encuentra")

db_file = 'inventario.json' # <-- nuevo
if not os.path.exists(db_file): # <-- nuevo
    write_json(db_file) # Si no existe, crearlo # <-- nuevo
with open(db_file, 'r') as f: # Lee el archivo actual # <-- nuevo
    inventario = json.load(f) # <-- nuevo

usuario = None
while usuario != "c":
    usuario = input("¿Qué deseas hacer? ([a]agregar, [b]buscar o [c]salir): ")
    if usuario == "a":
        agregar()
    elif usuario == "b":
        buscar()
    elif usuario == "c":
        print("Muchas gracias por agregar los productos.")
