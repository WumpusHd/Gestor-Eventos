from .evento import Evento


class EventoFilantropico(Evento):
    def __init__(self, nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad):
        super().__init__(nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad,
                         tipo_evento='Filantropico')
        self.patrocinadores = []
