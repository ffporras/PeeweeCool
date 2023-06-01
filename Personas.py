from tablas_sistema_de_peajes import *
from Tablas.Propietario import *

def altaPersonas(dni, apellido, nombre, email, celular, direccion, id_parentesco, id_propietario):
    with database.atomic() as transaction:
        try:
            personaNueva = Persona.get(Persona.dni == dni)
            print("Ya existe una persona con esas credenciales")
            transaction.rollback()
        
        except Persona.DoesNotExist:
            personaNueva = Persona.create(
                dni = dni,
                email = email,
                apellido = apellido,
                nombre = nombre,
                celular = celular,
                direccion = direccion,
                id_parentesco = id_parentesco,
                id_propietario = id_propietario
            )
            altaPropietario(id_propietario)
            print("La persona se agrego con exito")

def bajaPersonas(DNI):
    with database.atomic() as transaction: 
        try:
            persona = Persona.get(Persona.dni == DNI)
            propietario = Propietario.get(Propietario.id_propietario == persona.id_propietario)
            cuentaP = CuentaTelepeaje.get(CuentaTelepeaje.id_propietario == persona.id_propietario)
            persona.delete_instance() #Solo borra la tupla deseada
            propietario.delete_instance()
            cuentaP.delete_instance()
        
        except Persona.DoesNotExist: 
                transaction.rollback()
                error_saving = True #No se si es necesario

#Funciones para modificacion
def updatePersona(opcion, key, dato):
    with database.atomic() as transaction:
        try:
               persona = Persona.get(Persona.dni == key)
          
        except Persona.DoesNotExist:
               transaction.rollback()
    
        if opcion == "dni":
            try:
                persona1 = Persona.get(Persona.id_parentesco == key)
                persona.dni = dato
                persona1.id_parentesco = dato
            
            except Persona.DoesNotExist:
                transaction.rollback()
        
        if opcion == "email":
            persona.email = dato
        if opcion == "apellido":
            persona.apellido = dato
        if opcion == "nombre":
            persona.nombre = dato
        if opcion == "celular":
            persona.celular = dato
        if opcion == "direccion":
            persona.direccion = dato
        if opcion == "id_parentesco":
            persona.id_parentesco = dato
        if opcion == "id_propietario":
            try:
                propietario = Propietario.get(Propietario.id_propietario == persona.id_propietario)
                cuenta = CuentaTelepeaje.get(CuentaTelepeaje.id_propietario == persona.id_propietario)
                posee = Posee.get(Posee.id_propietario == persona.id_propietario)
                persona.id_propietario = dato
                cuenta.id_propietario = dato
                posee.id_propietario = dato
            
            except Posee.DoesNotExist or Propietario.DoesNotExist or CuentaTelepeaje.DoesNotExist:
                transaction.rollback()