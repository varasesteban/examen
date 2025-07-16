productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
 '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
 'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
 'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
 'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
 '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
 '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
 'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
 }

stock = {'8475HD': [387990,10],
'2175HD': [327990,4],
'JjfFHD': [424990,1],
'fgdxFHD': [664990,21],
'123FHD': [290890,32],
'342FHD': [444990,7],
'GF75HD': [749990,2],
'UWU131HD': [349990,1],
'FS1230HD': [249990,0]
}

def stock_marca(marca):
    marcas_disponibles = []
    for p in productos.values():
        marcas_disponibles.append(p[0].lower())
    
    if marca.lower() not in marcas_disponibles:
        print("No existe la marca ingresada")
    else:
        total = 0
        for codigo in productos:
            if productos[codigo][0].lower() == marca.lower():
                total = total + stock[codigo][1]
        
        print(f"El stock es: {total}")

def busqueda_precio(p_min, p_max):
    resultados = []
    for codigo in stock:
        if p_min <= stock[codigo][0] <= p_max and stock[codigo][1] > 0:
            resultados.append(f"{productos[codigo][0]} - {codigo}")
    
    if resultados:
        print("Los notebooks entre los precios consultas son: ", sorted(resultados))
    else:
        print("No hay notebooks en este rango de precios")

def actualizar_precio(modelo, p):
    if modelo in productos:
        stock[modelo][0] = p
        return True
    else:
        return False

while True:
    print("*** MENU PRINCIPAL ***")
    print("1. Stock marca")
    print("2. Búsqueda por precio")
    print("3. Actualizar precio")
    print("4. Salir")

    try:
        opcion = int(input("Ingrese opción: "))
        
        if opcion == 1:
            marca = input("Ingrese marca a consultar: ")
            stock_marca(marca)
        elif opcion == 2:
            try: 
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))
                busqueda_precio(p_min, p_max)
            except ValueError:
                print("Debe ingresar valores enteros!!")
        elif opcion == 3:
            while True:
                modelo = input("Ingrese modelo a actualizar: ")
                try:
                    p = int(input("Ingrese precio nuevo: "))
                except ValueError:
                    print("Debe ingresar valores enteros!!")
                if actualizar_precio(modelo, p):
                    print("Precio actualizado!!")
                else:
                    print("El modelo no existe!!")
                
                respuesta = input("¿Desea actualizar otro precio (s/n)?")
                if respuesta == "si":
                    continue
                else:
                    if respuesta == "no":
                        break

        elif opcion == 4:
            print("Programa finalizado")
            break
        else:
            print("Debe seleccionar una opción válida!!")

    except ValueError:
        print("Debe seleccionar una opción válida!!")
