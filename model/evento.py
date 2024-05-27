import uuid


class Evento:
    def __init__(self, nombre="", fecha=0, hora_apertura=0, hora_show=0, lugar="", direccion="", ciudad="",  tipo_evento=""):
        self.id = uuid.uuid4()
        self.nombre = nombre
        self.artistas = []
        self.fecha = fecha
        self.hora_apertura = hora_apertura
        self.hora_show = hora_show
        self.lugar = lugar
        self.direccion = direccion
        self.ciudad = ciudad
        self.aforo_total = 0
        self.lista_cortesias = []
        self.tipo_evento = tipo_evento
        self.estado = ''
        self.fase_venta = ''
        self.precio_boleta = 0
        self.boletas_vendidas = []
        self.ingresos = 0






