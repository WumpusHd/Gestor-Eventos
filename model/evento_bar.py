from .evento import Evento


class EventoBar(Evento):
    def __init__(self, nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad):
        super().__init__(nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad,
                         tipo_evento='Bar')
        self.ingresos_bar = 0
        self.ingresos_artista = 0
