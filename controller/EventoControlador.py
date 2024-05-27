class EventoControlador:
    # Constructor
    def __init__(self) -> None:
        super().__init__()
        self.lista_eventos = []
        self.lista_artistas = []

    def agregar_evento(self, evento):
        self.lista_eventos.append(evento)

    def eliminar_evento(self, evento):
        self.lista_eventos.remove(evento)

    def agregar_artistas(self, artista):
        self.lista_artistas.append(artista)


