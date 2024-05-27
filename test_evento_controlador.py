import unittest
from controller.EventoControlador import EventoControlador
from model.evento import Evento
from model.artista import Artista


class TestEventoControlador(unittest.TestCase):

    def setUp(self):
        self.controlador = EventoControlador()
        self.evento = Evento("Evento de prueba", "2024-05-20", "08:00", "10:00", "Lugar de prueba",
                             "Dirección de prueba", "Ciudad de prueba")
        self.artista = Artista("Artista de prueba")

    def test_agregar_evento(self):
        self.controlador.agregar_evento(self.evento)
        self.assertIn(self.evento, self.controlador.lista_eventos)

    def test_eliminar_evento(self):
        self.controlador.agregar_evento(self.evento)
        self.controlador.eliminar_evento(self.evento)
        self.assertNotIn(self.evento, self.controlador.lista_eventos)

    def test_agregar_artistas(self):
        self.controlador.agregar_artistas(self.artista)
        self.assertIn(self.artista, self.controlador.lista_artistas)


if __name__ == '__main__':
    unittest.main()
