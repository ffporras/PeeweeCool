from Tablas.Personas import *
from Tablas.Propietario import *
from Tablas.Cuenta_telepeaje import *
from Tablas.Peaje import *
from Tablas.Vehiculo import *
from Tablas.Ventanilla import *
from tablas_sistema_de_peajes import *

def MensajeBienvenida():
    menuPrincipal = """
    ¡Bienvenido a nuestro Sistema de Peajes!
     
      Menú Principal:
        
        1. Alta de un elemento
        2. Baja de un elemento
        3. Modificacion de un elemento
        4. Consultas
        5. Finalizar programa
        """
    print("\n")
    print(menuPrincipal)

def MensajeMenuAltaBajaMod():
    menu = """
        1. Propietarios
        2. Personas
        3. Cuentas
        4. Vehiculos
        5. Peajes
        6. Ventanillas 
        """
    
    print("\n")
    print(menu)

def MensajeModificacionPersona():
    modificacionPersona =  """
        1. DNI
        2. Apellido
        3. Nombre
        4. Email
        5. Celular
        6. Direccion
        7. ID Parentesco
        8. ID Propietario

        """
    print("\n")
    print(modificacionPersona)

def MensajeModificacionPropietario():
    modificacionPropietario =  """
        1. ID propietario
        2. Tipo de propietario

        """
    print("\n")
    print(modificacionPropietario)

def MensajeModificacionVentanilla():
    modificacionVentanilla =  """
        1. Nombre del peaje
        2. Numero de ID
        3. Antena RFID

        """

    print("\n")
    print(modificacionVentanilla)

def MensajeModificacionVehiculo():
    modificacionVehiculo =  """
        1. Matricula
        2. Marca
        3. Color
        4. Modelo
        5. Tipo
        6. Numero de cuenta de telepeaje

        """

    print("\n")
    print(modificacionVehiculo)

def MensajeModificacionPeaje():
    modificacionPeaje =  """
        1. DNI
        2. Apellido
        3. Nombre
        4. Email
        5. Celular
        6. Direccion
        7. ID Parentesco
        8. ID Propietario

        """
    print("\n")
    print(modificacionPeaje)

def MensajeModificacionCuenta():
    modificacionCuenta =  """
        1. Numero de cuenta
        2. Saldo
        3. Fecha de creacion
        4. ImporteCredito
        5. Fecha y hora del credito
        7. ID Propietario

        """

    print("\n")
    print(modificacionCuenta)

def MensajeMenuConsultas():
    menuConsultas = """
        1. Listado de propietarios y sus vehículos
        2. Listado de cuentas con su titular y sus vehículos asociados
        """
    
    print("\n")
    print(menuConsultas)

if __name__ == "__main__":
    
    database.connect()

    opcion = 0

    while opcion != 5:
        
        MensajeBienvenida()
        
        try:
            opcion = int(input("Seleccione la opción deseada: "))

            if opcion == 1:
                MensajeMenuAltaBajaMod()

                try:
                    opcion1 = int(input("Seleccione en que tabla desea dar de alta: "))
                    
                    if opcion1 == 1:
                        print("\n Alta Propietario: \n ")

                        IDpropietario = input("Ingrese IDpropietario: ")
                        tipo = input("Ingrese tipo de propietario (persona/empresa):  ") #HAcer que solo sea empresa o persona en sql y aca creo

                        nuevoPropietario = altaPropietario(IDpropietario, tipo)

                    if opcion1 == 2:
                        print("\n Alta Persona: \n ")

                        Dni = input("Ingrese dni: ")
                        Apellido = input("Ingrese apellido: ")
                        Nombre = input("Ingrese nombre: ")
                        Email = input("Ingrese email: ")
                        Celular = input("Ingrese celular: ")
                        Direccion = input("Ingrese direccion: ")
                        IDparentesco = input("Ingrese IDparentesco: ")
                        IDpropietario = input("Ingrese IDpropietario: ")  #Esto lo ingresa la persona o es uno random?

                        nuevaPersona = altaPersonas(Dni, Apellido, Nombre, Email, Celular, Direccion, IDparentesco, IDpropietario)

                    if opcion1 == 3:
                        print("\n Alta Cuenta Telepeaje: \n ")

                        nroCuenta = input("Ingrese numero de cuenta: ")
                        saldo = input("Ingrese saldo: ")
                        fechaCreacion = input("Ingrese fecha de creacion: ")
                        importeCredito = input("Ingrese importe Credito: ") #sto tiene que estar? o se hace solo con el sistema
                        fechaHoraCredito = input("Ingrese la fecha y hora del credito: ")#Cambiar el nombre en la tabla
                        IDpropietario = input("Ingrese IDpropietario asocidado a la cuenta: ")

                        nuevaCuenta = altaCuenta(nroCuenta, saldo, fechaCreacion, importeCredito, fechaHoraCredito, IDpropietario)

                    if opcion1 == 4:
                        print("\n Alta Vehiculo: \n ")

                        matricula = input("Ingrese matricula: ")
                        tagRFID = input("Ingrese tagRFID: ")
                        marca = input("Ingrese marca: ")
                        color = input("Ingrese color: ")
                        modelo = input("Ingrese modelo: ")
                        tipo = input("Ingrese tipo: ")
                        idNroCuenta = input("Ingrese nro de cuenta asociada: ")

                        nuevoVehiculo = altaVehiculo(matricula, tagRFID, marca, color, modelo, tipo, idNroCuenta)

                    if opcion1 == 5:
                        print("\n Alta Peaje: \n ")

                        nombrePeaje = input("Ingrese nombre peaje: ")
                        ruta = input("Ingrese ruta: ")
                        km = input("Ingrese km: ")
                        cantidadVentanas = input("Ingrese cantidad de ventanillas: ")
                        telefono = input("Ingrese telefono: ")

                        nuevoPeaje = altaPeaje(nombrePeaje, ruta, km, cantidadVentanas, telefono)

                    if opcion1 == 6:
                        print("\n Alta Ventanilla: \n ")

                        nombrePeaje = input("Ingrese el nombre de peaje el cual esta ubicado: ")
                        numeroID = input("Ingrese el numero de ID: ")
                        antenaRFID = input("Ingrese si tiene antenaRFID (si/no): ")

                        nuevaVentanilla = altaVentanilla(nombrePeaje, numeroID, antenaRFID)

                except:
                    print("La opción ingresada no era correcta. Intente nuevamente con un número.")

            if opcion == 2:
                print(MensajeMenuAltaBajaMod)
                try:
                    opcion2 = int(input("Seleccione en que tabla desea dar de baja: "))
                    
                    if opcion2 == 1:
                        print("\n Baja Propietario: \n ")

                        IDpropietario = input("Ingrese IDpropietario: ")

                        propietarioEliminado = bajaPropietario(IDpropietario)

                    if opcion2 == 2:
                        print("\n Baja Persona: \n ")

                        Dni = input("Ingrese dni del usuario que desea eliminar: ")
                        

                        personaEliminada = bajaPersonas(Dni)

                    if opcion2 == 3:
                        print("\n Baja Cuenta Telepeaje: \n ")

                        nroCuenta = input("Ingrese numero de cuenta de la cuenta que desea eliminar: ")
                        
                        cuentaEliminada = bajaCuenta(nroCuenta)

                    if opcion2 == 4:
                        print("\n Baja Vehiculo: \n ")

                        matricula = input("Ingrese matricula del vehiculo que desea eliminar: ")

                        vehiculoEliminado = bajaVehiculo(matricula)

                    if opcion2 == 5:
                        print("\n Baja Peaje: \n ")

                        nombrePeaje = input("Ingrese nombre peaje: ")

                        peajeEliminado = bajaPeaje(nombrePeaje)

                    if opcion2 == 6:
                        print("\n Baja Ventanilla: \n ")

                        nombrePeaje = input("Ingrese el nombre de peaje el cual esta ubicado: ")
                        numeroID = input("Ingrese el numero de ID: ")

                        ventanillaEliminado = bajaVentanilla(nombrePeaje, numeroID)

                except:
                    print("La opción ingresada no era correcta. Intente nuevamente con un número.")

            if opcion == 3:
                print(MensajeMenuAltaBajaMod)
                try:
                    opcion3 = int(input("Seleccione en que tabla desea realizar modificaciones: "))
                    
                    if opcion3 == 1:
                        print("\n Update Propietario: \n ")

                        IDpropietario = input("Ingrese IDpropietario del cual desea modificar datos: ")
                        propietarioModificado = updatePropietario(IDpropietario)

                    if opcion3 == 2:
                        print("\n Update Persona: \n ")

                        Dni = input("Ingrese dni del usuario que desea modificar datos: ")
                        print(MensajeModificacionPersona)
                        atributoAmodificar = input("Ingrese que atributo desea modificar: ")
                        valorNuevo = input("Ingrese el nuevo valor: ")
                        
                        personaModificada = updatePersona(atributoAmodificar, Dni, valorNuevo)

                    if opcion3 == 3:
                        print("\n Update Cuenta Telepeaje: \n ")

                        nroCuenta = input("Ingrese numero de cuenta de la cuenta que desea modificar datos: ")
                        print(MensajeModificacionCuenta)
                        atributoAmodificar = input("Ingrese que atributo desea modificar: ")
                        valorNuevo = input("Ingrese el nuevo valor: ")
                        
                        cuentaEliminada = updateCuenta(atributoAmodificar, nroCuenta, valorNuevo)

                    if opcion3 == 4:
                        print("\n Update Vehiculo: \n ")

                        matricula = input("Ingrese matricula del vehiculo que desea modificar datos: ")
                        print(MensajeModificacionVehiculo)
                        atributoAmodificar = input("Ingrese que atributo desea modificar: ")
                        valorNuevo = input("Ingrese el nuevo valor: ")
                        
                        cuentaEliminada = updateCuenta(atributoAmodificar, matricula, valorNuevo)

                    if opcion3 == 5:
                        print("\n Update Peaje: \n ")

                        nombrePeaje = input("Ingrese nombre del peaje que desea modificar datos: ")
                        print(MensajeModificacionPeaje)
                        atributoAmodificar = input("Ingrese que atributo desea modificar: ")
                        valorNuevo = input("Ingrese el nuevo valor: ")
                        
                        cuentaEliminada = updateCuenta(atributoAmodificar, nombrePeaje, valorNuevo)

                    if opcion3 == 6:
                        """print("\n Update Ventanilla: \n ")

                        nombrePeaje = input("Ingrese el nombre de peaje el cual esta ubicado: ")
                        numeroID = input("Ingrese el numero de ID: ")

                        print(MensajeModificacionVentanilla)
                        atributoAmodificar = input("Ingrese que atributo desea modificar: ")
                        valorNuevo = input("Ingrese el nuevo valor: ")
                        
                        cuentaEliminada = updateCuenta(atributoAmodificar, nroCuenta, valorNuevo)"""
                        pass

                except:
                    print("La opción ingresada no era correcta. Intente nuevamente con un número.")
            
            if opcion == 4:
                print(MensajeMenuConsultas)

                print("Sorry en este momento no esta habilitada esta opcion")
            
            if opcion == 5:
                print("Su programa ha sido finalizado con exito")
                break
        except:
            print("La opción ingresada no era correcta. Intente nuevamente con un número.")
