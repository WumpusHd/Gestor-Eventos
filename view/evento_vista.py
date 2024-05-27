"""
Contiene la clase VistaPrincipal,
la cual se encarga de definir el menu y su visualización.
Asignatura: Programación Orientada a Objetos
Autores: Santiago Arango Henao - Jhon Eduar Jimenez
"""

import streamlit as st
from controller.EventoControlador import EventoControlador
from streamlit_option_menu import option_menu
from view.FormularioEvento import agregar_evento, gestionar_evento, vender_boleta, generar_reportes, ingresar_evento


class VistaPrincipal:
    # Constuctor
    def __init__(self) -> None:
        super().__init__()

        # Estategia para manejar el "estado" del controlador y del modelo entre cada cambio de ventana
        if 'main_view' not in st.session_state:
            self.menu_actual = "Inicio"

            # Conexión con el controlador
            self.controller = EventoControlador()

            st.session_state['main_view'] = self
        else:

            # Al existir en la sesión entonces se actualizan los valores
            self.menu_actual = st.session_state.main_view.menu_actual
            self.controller = st.session_state.main_view.controller

        self._dibujar_layout()

    def _dibujar_layout(self):
        st.set_page_config(page_title="Gestor de Eventos", page_icon="🎭", layout="wide", initial_sidebar_state="auto")
        self.col1, self.col2, self.col3, self.col4 = st.columns([1, 1, 1, 1])

        # Definimos las opciones del Gestor de Eventos
        with st.sidebar:
            st.image("imgs/imagen_comedia.jpg", width=297)
            self.menu_actual = option_menu("Menu",
                                           ["Inicio", 'Crear evento', 'Gestionar Evento', 'Vender Boleta',
                                            'Generar Reportes', 'Ingresar Evento'],
                                           icons=['house', 'plus-circle', 'cog', 'ticket',
                                                  'file-earmark-text', 'sign-in'],
                                           menu_icon="cast", default_index=0)

    @staticmethod
    def bienvenida():
        return """
                # ¡Bienvenido!
                En esta página podrás crear eventos de comedias, gestionarlos, vender boletas y generar reportes.\n
                Nota: Cualquier Inconveniente porfavor comunicarse con: sa5602082@gmail.com
                Autores: *Santiago Arango Henao* Y *Jhon Eduar Jimenez* ️
                """

    def controlar_menu(self):
        if self.menu_actual == "Inicio":
            # Se hace el llamado con self porque es el objeto de la clase actual
            texto = self.bienvenida()
            st.write(texto)
        elif self.menu_actual == "Crear evento":
            agregar_evento(st, self.controller)
        elif self.menu_actual == "Gestionar Evento":
            gestionar_evento(st, self.controller)
        elif self.menu_actual == "Vender Boleta":
            vender_boleta(st, self.controller)
        elif self.menu_actual == "Generar Reportes":
            generar_reportes(st, self.controller)
        elif self.menu_actual == "Ingresar Evento":
            ingresar_evento(st, self.controller)


if __name__ == "__main__":
    gui = VistaPrincipal()
    gui.controlar_menu()
