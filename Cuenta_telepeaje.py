from tablas_sistema_de_peajes import *

def altaCuenta(nro_cuenta, saldo, fecha_creacion, importe_credito, fecha_hora, id_propietario):
    with database.atomic() as transaction:
        try:
            cuentaNueva = CuentaTelepeaje.get(CuentaTelepeaje.nro_cuenta == nro_cuenta) 
            print("Ya existe una persona con esas credenciales")
            transaction.rollback()
        
        except CuentaTelepeaje.DoesNotExist:
            cuentaNueva = CuentaTelepeaje.create(
                nro_cuenta = nro_cuenta,
                saldo = saldo,
                fecha_creacion = fecha_creacion,
                id_propietario = id_propietario,
                importe_credito = importe_credito,
                fecha_hora = fecha_hora
            )
            print("La cuenta de telepeaje se agrego con exito")
            

def bajaCuenta(nro_cuenta):
    with database.atomic() as transaction: #ATOMIC se hace todo o no se hace nada
                                           #TRANSACTION hace que al fallar, pueda usarse el rollback y que vuelva al estado anterior que funcionaba
        try:
            cuentaABorrar = CuentaTelepeaje.get(CuentaTelepeaje.nro_cuenta == nro_cuenta)
            cuentaABorrar.delete_instance() #Solo borra la tupla deseada
            print("La cuenta de telepeaje se elimino con exito")
        
        except CuentaTelepeaje.DoesNotExist: 
                print("No existe una cuenta de telepeaje con esas credenciales")
                transaction.rollback()
                error_saving = True #No se si es necesario

def updateCuenta(opcion, key, dato):
    with database.atomic() as transaction:
        try:
            cuenta = CuentaTelepeaje.get(CuentaTelepeaje.nro_cuenta == key)
        
            if opcion == 1:
                cuenta.saldo = dato
            if opcion == 2:
                cuenta.fecha_creacion = dato
            if opcion == 3:
                cuenta.id_propietario = dato
            if opcion == 4:
                cuenta.importe_credito = dato
            if opcion == 5:
                cuenta.fecha_hora = dato
            cuenta.save()
        
        except CuentaTelepeaje.DoesNotExist:
            transaction.rollback()