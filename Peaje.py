from tablas_sistema_de_peajes import *

def altaPeaje(nombre_peaje, ruta, km, cantidad_ventanas, telefono):
    with database.atomic() as transaction:
        try:
            peajeNuevo = Peaje.get(Peaje.nombre_peaje == nombre_peaje) 
            print("Ya existe un peaje con esas credenciales")
            transaction.rollback()

        except Peaje.DoesNotExist:
            peajeNueva = Peaje.create(
                nombre_peaje = nombre_peaje,
                ruta = ruta,
                km = km,
                cantidad_ventanas = cantidad_ventanas,
                telefono = telefono
            )
            print("El peaje se agrego con exito")
            


def bajaPeaje(nombre_peaje):
    with database.atomic() as transaction:
        try:
            peajeABorrar = Peaje.get(Peaje.nombre_peaje == nombre_peaje)
            peajeABorrar.delete_instance()
            ventanillaP = Ventanilla.get(Ventanilla.nombre_peaje == nombre_peaje)
            ventanillaP.delete_instance()
            print("El peaje se agrego con exito")

        except Peaje.DoesNotExist:
            print("El peaje se agrego con exito")
            transaction.rollback()

def updatePeaje(opcion, key, dato):
    with database.atomic() as transaction:
        try:
            peaje = Peaje.get(Peaje.nombre_peaje == key)
        
            if opcion == 1:
                peaje.ruta = dato

            if opcion == 2:
                peaje.km = dato

            if opcion == 3:
                peaje.cantidad_ventanas = dato
                
            if opcion == 4:
                peaje.telefono = dato
            peaje.save()

        except Peaje.DoesNotExist:
            transaction.rollback()
