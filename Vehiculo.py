from tablas_sistema_de_peajes import *

def altaVehiculo(matricula, tag_rfid, marca, color, modelo, tipo, id_nro_cuenta):
    with database.atomic() as transaction:
        try:
            vehiculoNuevo = Vehiculo.get(Vehiculo.matricula == matricula) 
            print("Ya existe un vehiculo con esas credenciales")
            transaction.rollback()

        except Vehiculo.DoesNotExist:
            vehiculoNuevo = Vehiculo.create(
                matricula=matricula,
                tag_rfid=tag_rfid,
                marca=marca,
                color=color,
                modelo=modelo,
                tipo=tipo,
                id_nro_cuenta=id_nro_cuenta
            )
            
            print("El vehiculo se agrego correctamente") #Me parece que esto es redundante

def bajaVehiculo(matricula):
    with database.atomic() as transaction:
        try:
            vehiculoABorrar = Vehiculo.get(Vehiculo.matricula == matricula)
            vehiculoABorrar.delete_instance()
            print("El vehiculo se elimino correctamente")
            #Agregar borrar en posee

        except Vehiculo.DoesNotExist:
            print("No existe un vehiculo con esas credenciales")
            transaction.rollback()

def updateVehiculo(opcion, key, dato):
    with database.atomic() as transaction:
        try:
            vehiculo = Vehiculo.get(Vehiculo.matricula == key)
        
            if opcion == 1:
                vehiculo.tag_rfid = dato
            if opcion == 2:
                vehiculo.marca = dato
            if opcion == 3:
                vehiculo.color = dato
            if opcion == 4:
                vehiculo.modelo = dato
            if opcion == 5:
                vehiculo.tipo = dato
            if opcion == 6:
                vehiculo.id_nro_cuenta = dato
            
            vehiculo.save()
        
        except Vehiculo.DoesNotExist:
            transaction.rollback()
    