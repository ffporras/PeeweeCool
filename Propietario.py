from tablas_sistema_de_peajes import *

def altaPropietario(id_propietario):
    with database.atomic() as transaction:
        try:
            propietarioNuevo = Propietario.get(Propietario.id_propietario == id_propietario)
            transaction.rollback()
        
        except Propietario.DoesNotExist:
            propietarioNuevo = Propietario.create(
                id_propietario = id_propietario, 
                tipo = "persona"
            )
            return propietarioNuevo #Me parece que esto es redundante
        
def bajaPropietario(id_propietario):
    with database.atomic() as transaction:
        try:
            propietarioABorrar = Propietario.get(Propietario.id_propietario == id_propietario)
            propietarioABorrar.delete_instance()

        except Propietario.DoesNotExist:
            transaction.rollback()

def updatePropietario(opcion, key, dato):
    with database.atomic() as transaction:
        try:
            prop = Propietario.get(Propietario.id_propietario == key)
        
        except Propietario.DoesNotExist:
            transaction.rollback()
    
    if opcion ==  "tipo":
        prop.tipo = dato
    prop.save()