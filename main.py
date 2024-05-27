"""
Punto de entrada del programapip
"""

from view.evento_vista import VistaPrincipal

if __name__ == "__main__":
    gui = VistaPrincipal()
    gui.controlar_menu()
