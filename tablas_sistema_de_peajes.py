from peewee import *
from Configuracion.Config import *

database = PostgresqlDatabase('Sistema_de_peajes.db')

#En el main se llama db_connect() ya que por ahi se conecta tanto potgrade como mongo
#el base model nos lo da diego

class Vehiculo(BaseModel):
    matricula = CharField(max_length=10, primary_key=True)
    tag_RFID = IntegerField()
    marca = CharField(max_length=50)
    color = CharField(max_length=50)
    modelo = CharField(max_length=50)
    tipo = IntegerField()
    id_nro_cuenta = IntegerField()
	
    class Meta:
        table_name = 'Vehiculo'

class TipoVehiculo(BaseModel):
    id_tipo = IntegerField(primary_key=True)
    descripcion = CharField(max_length=50)

    class Meta:
        table_name = 'TipoVehiculo'
        #Hay un dirty fields que dice wue sube solo los que se modifican, ver eso


class Tarifa(BaseModel):
    id_tipo = IntegerField(primary_key=True)
    fecha_vigencia = DateField()
    importe_tarifa = DoubleField()
    
    class Meta:
        table_name = 'Tarifa'

class Posee(BaseModel):
    id_propietario = IntegerField()
    matricula = CharField(max_length=10)

    class Meta:
        table_name = 'Posee'
        primary_key = CompositeKey('id_propietario', 'matricula')

class Peaje(BaseModel):
    nombre_peaje = CharField(max_length=50, primary_key=True)
    ruta = CharField(max_length=50)
    km = IntegerField()
    cantidad_ventanas = IntegerField()
    telefono = CharField(max_length=50)

    class Meta:
        table_name = 'Peaje'


class Ventanilla(BaseModel):
    nombre_peaje = CharField(max_length=50)
    numero_id = IntegerField()
    antena_rfid = BooleanField()

    class Meta:
        table_name = 'Ventanilla'
        primary_key = CompositeKey('numero_id', 'nombre_peaje')

class Bonificacion(BaseModel):
    id_nro_cuenta = IntegerField()
    nombre_peaje = CharField(max_length=50)
    fecha_otorgacion = DateField()
    fecha_renovacion = DateField()
    porcentaje = IntegerField()
    motivo = CharField(max_length=50)

    class Meta:
        table_name = 'Bonificacion'
        primary_key = CompositeKey('id_nro_cuenta', 'nombre_peaje')

class Debito(BaseModel):
    matricula = CharField(max_length=10)
    fecha_hora = DateTimeField()
    importe_debito = DoubleField()
    nombre_peaje = CharField(max_length=50)
    numero_ventana = IntegerField()
    id_nro_Cuenta = IntegerField()

    class Meta:
        table_name = 'Debito'
        primary_key = CompositeKey('matricula', 'fechaHora')
        indexes = ((('numero_ventana', 'nombre_peaje', 'fecha_hora', 'id_nro_Cuenta', 'matricula'), True),)


class CuentaTelepeaje(BaseModel):
    nro_cuenta = IntegerField(primary_key=True)
    saldo = DoubleField()
    fecha_Creacion = DateTimeField()
    importe_credito = DoubleField()
    fecha_hora = DateTimeField()
    id_propietario = IntegerField()

    class Meta:
        table_name = 'CuentaTelepeaje'

class Propietario(BaseModel):
    id_propietario = IntegerField(primary_key=True)
    tipo = CharField(max_length=50)

    class Meta:
        table_name = 'Propietario'

class Persona(BaseModel):
    dni = CharField(max_length=50, primary_key=True)
    apellido = CharField(max_length=50)
    nombre = CharField(max_length=50)
    email = CharField(max_length=50)
    celular = CharField(max_length=50)
    direccion = CharField(max_length=50)
    id_parentesco = CharField(max_length=50)
    id_propietario = IntegerField()

    class Meta:
        table_name = 'Persona'

class Empresa(BaseModel):
    rut = IntegerField(primary_key=True)
    nombre_empresa = CharField(max_length=50)
    direccion = CharField(max_length=50)
    telefono = CharField(max_length=50)
    id_propietario = IntegerField()

    class Meta:
        table_name = 'Empresa'


#De donde sacaron esto xd vi unas cosas en schema manager que son distintas
database.execute.sql("""ALTER TABLE Vehiculo
ADD CONSTRAINT Vehiculo_FK FOREIGN KEY (tipo)
REFERENCES TipoVehiculo(Id_Tipo);""")

database.execute.sql("""ALTER TABLE Vehiculo
ADD CONSTRAINT Vehiculo_FK2 FOREIGN KEY (id_nro_Cuenta)
REFERENCES CuentaTelepeaje(nro_Cuenta);""")


database.execute.sql("""ALTER TABLE Tarifa
ADD CONSTRAINT Tarifa_FK FOREIGN KEY (ID_tipo)
REFERENCES TipoVehiculo(Id_Tipo);""")

database.execute.sql("""ALTER TABLE Posee 
ADD CONSTRAINT Posee_FK FOREIGN KEY (ID_propietario)
REFERENCES Propietario(id_Propietario);""")

database.execute.sql("""ALTER TABLE Posee 
ADD CONSTRAINT Posee_FK2 FOREIGN KEY (matricula)
REFERENCES Vehiculo(matricula);""")

database.execute.sql("""ALTER TABLE Ventanilla
ADD CONSTRAINT Ventanilla_FK FOREIGN KEY (nombre_Peaje)
REFERENCES Peaje(nombre_Peaje);""")

database.execute.sql("""ALTER TABLE Bonificacion 
ADD CONSTRAINT Bonificacion_FK FOREIGN KEY (nombre_Peaje)
REFERENCES Peaje(nombre_Peaje);""")

database.execute.sql("""ALTER TABLE Bonificacion	
ADD CONSTRAINT Bonificacion_FK2 FOREIGN KEY (ID_nro_Cuenta)
REFERENCES CuentaTelepeaje(nro_Cuenta);""")


database.execute.sql("""ALTER TABLE Debito
ADD CONSTRAINT Debito_FK FOREIGN KEY (id_nro_Cuenta)
REFERENCES CuentaTelepeaje(nro_Cuenta);""")

database.execute.sql("""ALTER TABLE Debito
ADD CONSTRAINT Debito_FK2 FOREIGN KEY (nombre_Peaje, numero_Ventana)
REFERENCES Ventanilla(nombre_Peaje, numero_ID);""")

database.execute.sql("""ALTER TABLE Debito
ADD CONSTRAINT Debito_FK3 FOREIGN KEY (matricula)
REFERENCES Vehiculo(matricula);""")

database.execute.sql("""ALTER TABLE CuentaTelepeaje
ADD CONSTRAINT CuentaTelepeaje_FK FOREIGN KEY (ID_propietario)
REFERENCES Propietario(id_Propietario);""")

database.execute.sql("""ALTER TABLE Persona
ADD CONSTRAINT Persona_FK FOREIGN KEY (ID_propietario)
REFERENCES Propietario(id_Propietario);""")

database.execute.sql("""ALTER TABLE Persona
ADD CONSTRAINT Persona_FK2 FOREIGN KEY (ID_parentesco)
REFERENCES Persona(DNI);""")

database.execute.sql("""ALTER TABLE Empresa
ADD CONSTRAINT Empresa_FK FOREIGN KEY (ID_propietario)
REFERENCES Propietario(id_Propietario);""")

database.connect()
database.create_tables([Vehiculo, TipoVehiculo, Tarifa, Posee, Peaje, Ventanilla, Bonificacion, Debito, CuentaTelepeaje, Propietario, Persona, Empresa])
