#Reto día 1
class Componente:
    def __init__(self, numero_serie, tipo_componente, costo):
        self.numero_serie = numero_serie
        self.componente = tipo_componente
        self.costo = costo

        self.historial_revisiones = []
        self.esta_activo = True

c1=Componente("MTR-1001", "Motor", 550.75)
c2=Componente("SNR-2050", "Sensor", 80.20)

c1.historial_revisiones = "2025-10-29"
c2.esta_activo = False

print(f"El componente 1 es un {c1.componente}.\nNúmero de serie: {c1.numero_serie}.\nCosto: {c1.costo}.\nHistorial de revisiones: {c1.historial_revisiones}.\nEstado de actividad: {c1.esta_activo}")
print("-"*50)
print(f"El componente 2 es un {c2.componente}.\nNúmero de serie: {c2.numero_serie}.\nCosto: {c2.costo}.\nHistorial de revisiones: {c2.historial_revisiones}.\nEstado de actividad: {c2.esta_activo}")
