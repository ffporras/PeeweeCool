from tablas_sistema_de_peajes import *

def altaVentanilla(nombre_peaje, numero_id, antena_rfid):
    with database.atomic() as transaction:
        try:
            dataVentanillaNueva = Ventanilla.get(Ventanilla.nombre_peaje == nombre_peaje and Ventanilla.numero_id == numero_id)
            print("Ya existe una ventanilla con esas credenciales")
            transaction.rollback()

        except Ventanilla.DoesNotExist:
            ventanillaNueva = Ventanilla.create(
                nombre_peaje = nombre_peaje,
                numero_id = numero_id,
                antena_rfid = antena_rfid
            )
            print("La ventanilla se agrego con exito")


def bajaVentanilla(nombre_peaje, numero_id):
    with database.atomic() as transaction: #ATOMIC se hace todo o no se hace nada
                                            #TRANSACTION hace que al fallar, pueda usarse el rollback y que vuelva al estado anterior que funcionaba
        try:
            dataVentanillaNueva = Ventanilla.get(Ventanilla.nombre_peaje == nombre_peaje and Ventanilla.numero_id == numero_id) 
            dataVentanillaNueva.delete_instance()
            print("La ventanilla se elimino con exito")
                
        except Ventanilla.DoesNotExist:
            print("No existe una ventanilla con esas credenciales") 
            transaction.rollback()
            error_saving = True #No se si es necesario

def updateVentanilla(opcion, key1, key2, dato):
    with database.atomic() as transaction:
        try:
            ventanilla = Ventanilla.get(Ventanilla.nombre_peaje == key1 and Ventanilla.numero_id == key2)

            if opcion == 1:
                ventanilla.antena_RFID = dato

            ventanilla.save()

        except Ventanilla.DoesNotExist:
            transaction.rollback()
    