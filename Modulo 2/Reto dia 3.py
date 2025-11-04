#Reto dia 3
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca=marca
        self.modelo=modelo
        self.anio=anio
        self.kilometraje = 0
        self._encendido = False
    
    def arrancar(self):
        if self._encendido == False:
            self._encendido = True
            print(f"El {self.marca} {self.modelo} ha arrancado")
        else:
            print("El vehículo ya estaba en marcha.")

    def apagar(self):
        if self._encendido == True:
            self._encendido = False
            print(f"El {self.marca} {self.modelo} se ha apagado.")
        else:
            print("El vehículo ya estaba apagado.")

    def get_kilometraje(self):
        return self.kilometraje

    def mostrar_info_base(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nAño del vehículo: {self.anio}")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, anio, num_puertas):
        super().__init__(marca, modelo, anio)
        self.num_puertas = num_puertas

    def conducir(self, km):
        kilometrajenum=float(km)
        if self._encendido == True:
            self.kilometraje += kilometrajenum
            print(f"Conduciendo {kilometrajenum} km...")
        else:
            print("Error: El coche debe estar arrancado para conducir")

class Camion(Vehiculo):
    def __init__(self, marca, modelo, anio, capacidad_carga_kg):
        super().__init__(marca, modelo, anio)
        self.capacidad_carga_kg = capacidad_carga_kg
        self.__carga_actual_kg = 0

    def cargar(self,kilos):
        kilosnum=float(kilos)
        carga_prueba = self.__carga_actual_kg + kilosnum
        if carga_prueba > self.capacidad_carga_kg:
            print("Error: Sobrecarga")
        else:
            self.__carga_actual_kg += kilosnum
            print("Carga exitosa.")
    
    def descargar(self, kilos):
        kilosnum=float(kilos)
        if self.__carga_actual_kg - kilosnum > 0:
            self.__carga_actual_kg -= kilosnum
        else:
            print("Error. No se puede descargar más de lo que hay")
    
    def get_carga_actual(self):
        return self.__carga_actual_kg


micoche=Coche("nissan", "march", "2017", 4)
micoche.conducir(100)
micoche.arrancar()
micoche.conducir(100)
micoche.apagar()
print(micoche.get_kilometraje())
print("-"*50)
micamion=Camion("Camion", "Ruta 1", "2010", 5000)
micamion.cargar(3000)
micamion.descargar(1000)
print(micamion.get_carga_actual())