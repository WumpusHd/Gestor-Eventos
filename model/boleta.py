import uuid

class Boleta:
    def __init__(self, evento="", comprador="", fuente="", metodo_pago="", fase_venta="", precio=0, cortesía=False):
        self.id = uuid.uuid4()
        self.evento = evento
        self.comprador = comprador
        self.fuente = fuente
        self.metodo_pago = metodo_pago
        self.fase_venta = fase_venta
        self.precio = precio
        self.cortesía = cortesía
        self.fecha_compra = ""
        self.lugar = ""
        self.direccion = ""
        self.confirmado = False
