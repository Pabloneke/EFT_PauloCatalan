productos = {         '8475HD': ["HP", 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
                      '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
                      'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
                     'fgdxFHD': ["HP", 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
                     'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
                     '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
                     '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
                     'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], 
                           }

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
              'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
              'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], 
                 }

marcas = ("asus", "acer","dell", "hp")

def stock_marca(marca):
        print("f")

def busqueda_ram_precio(ram_min,ram_max,precio):
    print("f")

def eliminar_producto(modelo):
    print("f")


while True:
    print("*** MENU PRINCIPAL ***")
    print("1.- Stock marca")
    print("2.- Búsqueda por RAM y precio")
    print("3.- Eliminar producto")
    print("4.- salir")
    opc = input("Ingrese opción(1/4): ")
    if opc == "1":
        print("opcion 1")
        #marca = input("ingrese la marca: ")
        marca = "dell"
        stock_marca(marca)
    elif opc == "2":
        ram_min = input("ingrese RAM mínima: ")
        ram_max = input("ingrese RAM máxima: ")
        precio = int(input("Ingrese precio: "))
        busqueda_ram_precio(ram_min, ram_max, precio)
    elif opc == "3":
        modelo = input("Ingrese Modelo a Eliminiar: ")
        eliminar_producto(modelo)
    elif opc == "4":
        print("opcion 4")
        break
    else:
        print("Debe seleccionar una opcion valida!!")

print("Progama Finalizado")

#Fue un gusto :)
#cambio 1