from time import sleep

# Ejemplo 0: Entidades Hospitales X Estudiantes
# Preferencias_Hospitales = {
#     'Atlanta': ['Wayne', 'Val', 'Yolanda', 'Zeus', 'Xavier'],
#     'Boston' : ['Yolanda', 'Wayne', 'Val', 'Xavier', 'Zeus'],
#     'Chicago': ['Wayne', 'Zeus', 'Xavier', 'Yolanda', 'Val'],
#     'Detroit': ['Val', 'Yolanda', 'Xavier', 'Wayne', 'Zeus'],
#     'El Paso': ['Wayne', 'Yolanda', 'Val', 'Zeus', 'Xavier']}

# Preferencias_Estudiantes = {
#     'Val'    : ['El Paso', 'Atlanta', 'Boston', 'Detroit', 'Chicago'],
#     'Wayne'  : ['Chicago', 'Boston', 'Detroit', 'Atlanta', 'El Paso'],
#     'Xavier' : ['Boston', 'Chicago', 'Detroit', 'El Paso', 'Atlanta'],
#     'Yolanda': ['Atlanta', 'El Paso', 'Detroit', 'Chicago', 'Boston'],
#     'Zeus'   : ['Detroit', 'Boston', 'El Paso', 'Chicago', 'Atlanta']}

# Ejemplos 1: Entidaes Hospitales x Estudiantes (Entidad Hospitales en diferente orden pero con las mismas preferencias)
# Preferencias_Hospitales = {
#     'Detroit': ['Val', 'Yolanda', 'Xavier', 'Wayne', 'Zeus'],
#     'Boston' : ['Yolanda', 'Wayne', 'Val', 'Xavier', 'Zeus'],
#     'Atlanta': ['Wayne', 'Val', 'Yolanda', 'Zeus', 'Xavier'],
#     'El Paso': ['Wayne', 'Yolanda', 'Val', 'Zeus', 'Xavier'],
#     'Chicago': ['Wayne', 'Zeus', 'Xavier', 'Yolanda', 'Val']}

# Preferencias_Estudiantes = {
#     'Val'    : ['El Paso', 'Atlanta', 'Boston', 'Detroit', 'Chicago'],
#     'Wayne'  : ['Chicago', 'Boston', 'Detroit', 'Atlanta', 'El Paso'],
#     'Xavier' : ['Boston', 'Chicago', 'Detroit', 'El Paso', 'Atlanta'],
#     'Yolanda': ['Atlanta', 'El Paso', 'Detroit', 'Chicago', 'Boston'],
#     'Zeus'   : ['Detroit', 'Boston', 'El Paso', 'Chicago', 'Atlanta']}

# Ejemplo 2: Entidades Estudiantex x Hospitales
Preferencias_Hospitales = {
    'Val'    : ['El Paso', 'Atlanta', 'Boston', 'Detroit', 'Chicago'],
    'Wayne'  : ['Chicago', 'Boston', 'Detroit', 'Atlanta', 'El Paso'],
    'Xavier' : ['Boston', 'Chicago', 'Detroit', 'El Paso', 'Atlanta'],
    'Yolanda': ['Atlanta', 'El Paso', 'Detroit', 'Chicago', 'Boston'],
    'Zeus'   : ['Detroit', 'Boston', 'El Paso', 'Chicago', 'Atlanta']}

Preferencias_Estudiantes = {
    'Atlanta': ['Wayne', 'Val', 'Yolanda', 'Zeus', 'Xavier'],
    'Boston' : ['Yolanda', 'Wayne', 'Val', 'Xavier', 'Zeus'],
    'Chicago': ['Wayne', 'Zeus', 'Xavier', 'Yolanda', 'Val'],
    'Detroit': ['Val', 'Yolanda', 'Xavier', 'Wayne', 'Zeus'],
    'El Paso': ['Wayne', 'Yolanda', 'Val', 'Zeus', 'Xavier']}

class Emparejamiento_Estable:
##########################################################################################################################################################
    def mejor_opcion(self, elemento_entidad):
        print("El estudiante " + self.nombre + " esta evaluando sus opciones.")
        sleep(0.05)
        if self.preferencias.index(elemento_entidad) < self.preferencias.index(self.emparejar):
            print(self.nombre + " decide que " + elemento_entidad.nombre + " es mejor opción que su actual emparejamiento: " + self.emparejar.nombre + ".")
            sleep(0.05)
        else:
            print(self.nombre + " decide que " + elemento_entidad.nombre + " es peor opción que su actual emparejamiento: " + self.emparejar.nombre + ".")
            sleep(0.05)
        return self.preferencias.index(elemento_entidad) < self.preferencias.index(self.emparejar)
##########################################################################################################################################################
    def propuesta_de(self, elemento_entidad):
        if self.sin_emparejar():
            self.prospecto(elemento_entidad)
            print(self.nombre + " se encuentra sin emparejar y acepta a " + elemento_entidad.nombre + ".")
            sleep(0.05)
        elif self.mejor_opcion(elemento_entidad):
            print(self.nombre + " cambia a " + self.emparejar.nombre + " por " + elemento_entidad.nombre + ".")
            sleep(0.05)
            self.emparejar.liberar()
            self.prospecto(elemento_entidad)
        else:
            print(self.nombre + " rechaza a " + elemento_entidad.nombre + " y mantiene a " + self.emparejar.nombre + ".")
            sleep(0.05)
###########################################################################################################################################################
    def propuesta_a(self,elemento_entidad):
        self.propuesta.append(elemento_entidad)
        elemento_entidad.propuesta_de(self)
###########################################################################################################################################################
    def prospecto(self, elemento_entidad):
        self.emparejar = elemento_entidad
        elemento_entidad.emparejar = self
###########################################################################################################################################################
    def __init__(self, nombre):
        self.nombre       = nombre
        self.emparejar    = None
        self.preferencias = []
        self.propuesta    = []
###########################################################################################################################################################
    def sin_emparejar(self):
        return self.emparejar == None   
###########################################################################################################################################################
    def liberar(self):
        self.emparejar    = None
###########################################################################################################################################################
###########################################################################################################################################################
###########################################################################################################################################################
hospital = {}
for elemento_entidad_1 in Preferencias_Hospitales:
    hospital[elemento_entidad_1] = Emparejamiento_Estable(elemento_entidad_1)
###########################################################################################################################################################
estudiante = {}
for elemento_entidad_2 in Preferencias_Estudiantes:
    estudiante[elemento_entidad_2] = Emparejamiento_Estable(elemento_entidad_2)
for nombre_hospital,elemento_hospital in hospital.items():
    for nombre_estudiante in Preferencias_Hospitales[nombre_hospital]:
        elemento_hospital.preferencias.append(estudiante[nombre_estudiante])
for nombre_estudiante,elemento_estudiante in estudiante.items():
    for nombre_hospital in Preferencias_Estudiantes[nombre_estudiante]:
        elemento_estudiante.preferencias.append(hospital[nombre_hospital])

def busqueda_sin_emparejar(objeto_encontrado):
    print("Buscando Hospitales sin Emparejar.")
    sleep(0.05)
    for elemento_entidad,objeto_elemento_entidad in objeto_encontrado.items():
        if objeto_elemento_entidad.sin_emparejar():
            print(objeto_elemento_entidad.nombre + " esta sin emparejar.")
            sleep(0.05)
            return objeto_elemento_entidad
    print("Nadie esta sin emparejar.")
    sleep(0.05)
    return False

def buscar_siguiente_mejor(hospitales,estudiante):
    for estudiantes in hospitales.preferencias:
        if not (estudiantes in hospitales.propuesta):
            print("La siguiente opción de " + estudiantes.nombre + " es " + hospitales.nombre)
            sleep(0.05)
            return estudiantes

def liberar_todos():
    for hospitales in hospital:
        hospital[hospitales].liberar()
    for estudiantes in estudiante:
        estudiante[estudiantes].liberar()

def match(hospital,estudiante):
    liberar_todos()
    done = False
    while not done:
        hospitales = busqueda_sin_emparejar(hospital)
        if not hospitales:
            done = True
        else:
            estudiantes = buscar_siguiente_mejor(hospitales,estudiante)
            print(hospitales.nombre + " esta proponiendo a " + estudiantes.nombre + ".")
            sleep(0.05)
            hospitales.propuesta_a(estudiantes)
###########################################################################################################################################################
match(hospital,estudiante)
###########################################################################################################################################################
###########################################################################################################################################################
###########################################################################################################################################################
print("\n\t\t\t\tResultado de Emparejamiento\t\t\t\t\n")
for nombre_hospital,elemento_hospital in hospital.items():
    print("\t\t\t" + "(\t" + nombre_hospital + "\t\t,\t" + elemento_hospital.emparejar.nombre + "\t)")