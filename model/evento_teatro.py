from .evento import Evento

class EventoTeatro(Evento):
    def __init__(self, nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, costo_alquiler):
        super().__init__(nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad,
                         tipo_evento='Teatro')
        self.costo_alquiler = costo_alquiler
        self.ingresos_teatro = 0
        self.ganancias_teatro = 0
