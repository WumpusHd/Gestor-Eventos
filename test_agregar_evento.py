import unittest
from unittest.mock import patch
from controller.EventoControlador import EventoControlador
from view.FormularioEvento import agregar_evento
import streamlit as st

class TestAgregarEvento(unittest.TestCase):

    def setUp(self):
        self.controlador = EventoControlador()

    @patch('streamlit.title')
    @patch('streamlit.columns')
    @patch('streamlit.text_input')
    @patch('streamlit.date_input')
    @patch('streamlit.time_input')
    @patch('streamlit.number_input')
    @patch('streamlit.selectbox')
    @patch('streamlit.button')
    def test_agregar_evento(self, mock_title, mock_columns, mock_text_input, mock_date_input, mock_time_input, mock_number_input, mock_selectbox, mock_button):
        # Define los valores de retorno para las funciones de streamlit
        mock_text_input.return_value = "Evento de prueba"
        mock_date_input.return_value = "2024-05-20"
        mock_time_input.return_value = "08:00"
        mock_number_input.return_value = 100
        mock_selectbox.return_value = 'Bar'
        mock_button.return_value = True

        # Llama a la función agregar_evento
        agregar_evento(st, self.controlador)

        # Verifica que se haya agregado un evento a la lista de eventos
        self.assertEqual(len(self.controlador.lista_eventos), 1)
        self.assertEqual(self.controlador.lista_eventos[0].nombre, "Evento de prueba")


if __name__ == '__main__':
    unittest.main()