"""

/*
 * Autores :
 * Santiago Arango Henap
 * Jhon Eduar Jimenez
 * Fecha Creacion: 20 de Mayo 2024
 *
 * Funciones para el manejo de la vista
 */

"""

import random
import datetime
import pandas as pd
import plotly.express as px
from fpdf import FPDF
from datetime import datetime
from model.evento import Evento
from model.evento_bar import EventoBar
from model.evento_filantropico import EventoFilantropico
from model.evento_teatro import EventoTeatro
from model.boleta import Boleta
from model.artista import Artista
from model.patrocinador import Patrocinador


def agregar_evento(st, controlador):
    st.title("Crear Evento")
    col1, col2, col3, col4 = st.columns(4)
    col5, col6, col7, col8 = st.columns(4)
    col9, col10, col11, col12 = st.columns(4)

    # Crea un objeto Evento para almacenar la información del formulario
    info_evento = Evento()

    # Define los campos del formulario para recoger la información del evento
    with col1:
        info_evento.nombre = st.text_input("Nombre Del Evento")
    with col2:
        info_evento.fecha = st.date_input("Fecha del evento")
    with col3:
        info_evento.hora_apertura = st.time_input("Hora de apertura")
    with col4:
        info_evento.hora_show = st.time_input("Hora del show")
    with col5:
        info_evento.lugar = st.text_input("Lugar del evento")
    with col6:
        info_evento.direccion = st.text_input("Dirección del evento")
    with col7:
        info_evento.ciudad = st.text_input("Ciudad del evento")
    with col8:
        info_evento.aforo_total = st.number_input("Aforo total")
    with col9:
        info_evento.tipo_evento = st.selectbox("Tipo de evento", ('Bar', 'Teatro', 'Filantropico'))
        # Dependiendo del tipo de evento, se recogen diferentes datos y se crean diferentes objetos
        if info_evento.tipo_evento == 'Bar':
            # Código para manejar la creación de un EventoBar
            # Inicializamos una lista vacía para almacenar las cortesias
            lista_cortesias = []
            i = 0

            # Mientras el contador sea menor o igual al 20% del aforo total del evento
            while i <= info_evento.aforo_total * 0.2:
                # Generamos un número aleatorio entre 0 y el aforo total del evento
                num_aleatorio = random.randint(0, info_evento.aforo_total)

                # Si el número aleatorio no está ya en la lista de cortesias
                if num_aleatorio not in lista_cortesias:
                    lista_cortesias.append(num_aleatorio)
                    i += 1

            # Creamos un objeto de la clase EventoBar con los datos del evento
            evento_bar = EventoBar(info_evento.nombre, info_evento.fecha,
                                   info_evento.hora_apertura,
                                   info_evento.hora_show, info_evento.lugar, info_evento.direccion, info_evento.ciudad)
            evento_bar.aforo_total = info_evento.aforo_total

            # Asignamos la lista de cortesias al atributo lista_cortesias del objeto evento_bar
            evento_bar.lista_cortesias = lista_cortesias
        elif info_evento.tipo_evento == 'Teatro':
            # Código para manejar la creación de un EventoTeatro
            # En la columna 11, se recoge el costo de alquiler del teatro
            with col10:
                costo_alquiler = st.number_input("Alquiler")

            # Se inicializa una lista vacía para las cortesias
            lista_cortesias = []
            i = 0

            # Mientras el contador sea menor o igual al 20% del aforo total del evento
            while i <= info_evento.aforo_total * 0.2:
                # Se genera un número aleatorio entre 0 y el aforo total del evento
                num_aleatorio = random.randint(0, info_evento.aforo_total)

                # Si el número aleatorio no está ya en la lista de cortesias
                if num_aleatorio not in lista_cortesias:
                    lista_cortesias.append(num_aleatorio)
                    i += 1

            # Se crea un objeto de la clase EventoTeatro con los datos del evento y el costo de alquiler
            evento_teatro = EventoTeatro(info_evento.nombre, info_evento.fecha,
                                         info_evento.hora_apertura,
                                         info_evento.hora_show, info_evento.lugar, info_evento.direccion,
                                         info_evento.ciudad,
                                         costo_alquiler)
            evento_teatro.aforo_total = info_evento.aforo_total

            # Se asigna la lista de cortesias al atributo lista_cortesias del objeto evento_teatro
            evento_teatro.lista_cortesias = lista_cortesias
        elif info_evento.tipo_evento == 'Filantropico':

            # Se crea un objeto de la clase EventoFilantropico con
            # los datos del evento, el nombre del patrocinador y el valor aportado
            evento_filantropico = EventoFilantropico(info_evento.nombre, info_evento.fecha,
                                                     info_evento.hora_apertura,
                                                     info_evento.hora_show, info_evento.lugar, info_evento.direccion,
                                                     info_evento.ciudad)
            evento_filantropico.aforo_total = info_evento.aforo_total

    # Se crea un botón para enviar el formulario
    enviado_btn = st.button("Crear Evento")

    # Si se presiona el botón y todos los campos están llenos
    if (enviado_btn and info_evento.nombre != "" and info_evento.fecha != 0 and info_evento.hora_apertura != 0 and
            info_evento.hora_show != 0 and info_evento.lugar != "" and
            info_evento.direccion != "" and info_evento.ciudad != "" and info_evento.aforo_total != 0):
        # Dependiendo del tipo de evento, se agrega el evento correspondiente al controlador
        if info_evento.tipo_evento == 'Bar':
            controlador.agregar_evento(evento_bar)
        elif info_evento.tipo_evento == 'Teatro':
            controlador.agregar_evento(evento_teatro)
        elif info_evento.tipo_evento == 'Filantropico':
            controlador.agregar_evento(evento_filantropico)
        st.write("Evento creado exitosamente")
    # Si se presiona el botón pero no todos los campos están llenos, se muestra un mensaje de error
    elif enviado_btn:
        st.write("Por favor llene todos los campos")
    else:
        st.info("No deje Ningún Espacio en Blanco")

    # Se devuelve el controlador con el nuevo evento agregado
    return controlador


def gestionar_evento(st, controlador):
    st.title("Gestionar Evento")

    # Selecciona el evento a gestionar
    opcion = st.selectbox("Eliga el evento a gestionar", [evento.nombre for evento in controlador.lista_eventos])

    # Busca el evento seleccionado en la lista de eventos del controlador
    evento = next((evento for evento in controlador.lista_eventos if evento.nombre == opcion), None)

    # Si el evento existe
    if evento is not None:
        # Si el evento es filantropico
        if evento.tipo_evento == 'Filantropico':
            """Selecciona la opción a gestionar"""
            opcion_evento = st.selectbox("Eliga la opción a gestionar",
                                         ['Añadir Patrocinadores', 'Eliminar evento',
                                          'Estado del Evento'])
        # En caso de ser bar o teatro, si fue realizado no se pueden hacer cambios
        # Si fue cancelado aún se puede modificar el estado
        elif evento.estado == 'Realizado':
            st.warning("El evento ya fue realizado")

        elif evento.estado == 'Cancelado':
            st.warning("El evento fue cancelado")
            opcion_evento = st.selectbox("Eliga la opción a gestionar",
                                         ['Estado del Evento'])

        else:
            opcion_evento = st.selectbox("Eliga la opción a gestionar",
                                         ['Modificar fase de venta y precio boleta', 'Eliminar evento',
                                          'Estado del Evento'])

        # Si la opción es 'Modificar fase de venta y precio boleta'
        if opcion_evento == 'Modificar fase de venta y precio boleta':
            # Crea un nuevo objeto Artista
            artista = Artista()

            # Solicita al usuario que ingrese el nombre del artista
            artista.nombre = st.text_input("Nombre de artista")

            # Crea un botón para añadir el artista
            boton_artistas = st.button("Añadir artista")
            # Si el botón es presionado
            if boton_artistas:
                # Añade el evento a la lista de eventos ingresados del artista
                artista.eventos_ingresados.append(evento)
                # Si no hay artistas en la lista de artistas del controlador
                if not controlador.lista_artistas:
                    # Añade el artista a la lista de artistas del controlador
                    controlador.agregar_artistas(artista)
                else:
                    # Inicializa una bandera en 0
                    flag = 0
                    # Para cada artista en la lista de artistas del controlador
                    for artistas in controlador.lista_artistas:
                        # Si el nombre del artista coincide con el nombre del artista ingresado
                        if artistas.nombre == artista.nombre:
                            # Añade el evento a la lista de eventos ingresados del artista
                            artistas.eventos_ingresados.append(evento)
                            # Cambia la bandera a 1
                            flag = 1
                    # Si la bandera sigue siendo 0 (es decir, no se encontró un artista con el mismo nombre)
                    if flag == 0:
                        # Añade el artista a la lista de artistas del controlador
                        controlador.agregar_artistas(artista)

                # Añade el artista a la lista de artistas del evento
                evento.artistas.append(artista)
            # Selecciona la fase de venta del evento
            fase_venta = st.selectbox("Fase de venta", ['Preventa', 'Venta'])
            # Si la fase de venta es 'Preventa'
            if fase_venta == 'Preventa':
                # Modifica el precio de la boleta y fase de venta
                evento.precio_boleta = st.number_input("Precio de la boleta", evento.precio_boleta)
                evento.fase_venta = 'Preventa'
                boton_confirmacion = st.button("Confirmar")

                # Si se presiona el botón y el precio de la boleta no es 0, se confirma la fase de venta
                if boton_confirmacion and evento.precio_boleta != 0:
                    st.write("Fase de venta confirmada")
                # Si se presiona el botón pero el precio de la boleta es 0, muestra un mensaje de error
                elif boton_confirmacion:
                    st.write("Por favor llene el campo")
                else:
                    st.info("No deje Ningún Espacio en Blanco")
            else:
                # Misma lógica que la anterior pero para la fase de venta 'Venta'
                evento.precio_boleta = st.number_input("Precio de la boleta", evento.precio_boleta)
                evento.fase_venta = 'Venta'
                boton_confirmacion = st.button("Confirmar")

                if boton_confirmacion and evento.precio_boleta != 0:
                    st.write("Fase de venta confirmada")
                elif boton_confirmacion:
                    st.write("Por favor llene el campo")
                else:
                    st.info("No deje Ningún Espacio en Blanco")
        elif opcion_evento == 'Añadir Patrocinadores':
            patrocinadores = Patrocinador()
            patrocinadores.nombre = st.text_input("Nombre de patrocinador")
            patrocinadores.aporta = st.number_input("Cuanto aporta")
            boton_artistas = st.button("Añadir patrocinador")
            if boton_artistas:
                evento.patrocinadores.append(patrocinadores)

        elif opcion_evento == 'Eliminar evento':
            # Botón para confirmar la eliminación del evento
            boton_confirmacion = st.button("Eliminar")
            # Si no hay boletas vendidas para el evento
            if not evento.boletas_vendidas:
                # Si se presiona el botón, elimina el evento y muestra un mensaje de confirmación
                if boton_confirmacion:
                    controlador.eliminar_evento(evento)
                    st.write("Evento eliminado")
            # Si hay boletas vendidas para el evento, muestra un mensaje de advertencia
            else:
                st.warning("No se puede eliminar el evento porque hay boletas vendidas")
        # Si la opción es 'Estado del Evento'
        elif opcion_evento == 'Estado del Evento':
            # En la columna 3, selecciona el estado del evento y se modifica
            modificar_estado = st.selectbox("Estado del evento", ['Por realizar', 'Realizado', 'Cancelado'])
            boton = st.button("Confirmar")
            if boton:
                evento.estado = modificar_estado
    else:
        st.write("No se encontró el evento")

    return controlador


def vender_boleta(st, controlador):
    st.title("Vender Boleta")

    # Crea un objeto Boleta para almacenar la información del formulario
    cliente = Boleta()

    col1, col2, col3, col4 = st.columns(4)
    col5, col6 = st.columns(2)

    # En la columna 1, selecciona el evento para el que se va a vender la boleta
    with col1:
        cliente.nombre_evento = st.selectbox("Nombre del evento",
                                             [evento.nombre for evento in controlador.lista_eventos])
        # Busca el evento seleccionado en la lista de eventos del controlador
        evento = next((evento for evento in controlador.lista_eventos if evento.nombre == cliente.nombre_evento), None)

        # Si no hay eventos registrados, muestra un mensaje de advertencia
        # Si hay eventos registrados, se revisa el estado actual del evento
        if not controlador.lista_eventos:
            st.warning("No hay eventos registrados")

        elif evento.estado == 'Realizado':
            st.warning("El evento ya fue realizado")

        elif evento.estado == 'Cancelado':
            st.warning("El evento fue cancelado")

        else:
            # Si el aforo total del evento es igual al número de boletas vendidas, muestra un mensaje de advertencia
            if evento.aforo_total == len(evento.boletas_vendidas):
                st.warning("No hay boletas disponibles")
            else:
                # En la columna 2, recoge el nombre del comprador
                with col2:
                    cliente.comprador = st.text_input("Nombre del comprador")
                # En la columna 3, recoge la fuente de la boleta
                with col3:
                    cliente.fuente = st.text_input("Fuente de la boleta")
                # En la columna 4, selecciona el método de pago
                with col4:
                    if evento.tipo_evento == 'Filantropico':
                        cliente.metodo_pago = "No aplica"
                    else:
                        cliente.metodo_pago = st.selectbox("Método de pago",
                                                           ['Efectivo', 'Tarjeta de crédito', 'Tarjeta débito'])
                # En la columna 5, muestra el precio de la boleta y la cantidad de boletas disponibles
                with col5:
                    # Si el evento seleccionado es de tipo "Filantropico"
                    if cliente.nombre_evento == "Filantropico":
                        cliente.precio = 0
                    # Si se ha seleccionado un evento
                    elif cliente.nombre_evento is not None:
                        # Se busca el precio de la boleta para el evento
                        # seleccionado en la lista de eventos del controlador
                        cliente.precio = next((evento.precio_boleta for evento in controlador.lista_eventos if
                                               evento.nombre == cliente.nombre_evento), None)

                        st.write("Precio de la boleta: ", cliente.precio)
                        # Se muestra la cantidad de boletas disponibles, que es el aforo total del evento menos las boletas ya vendidas
                        st.write("Cantidad de boletas disponibles: ", evento.aforo_total - len(evento.boletas_vendidas))
                    else:
                        st.write("Seleccione un evento")
                # En la columna 6, determina si la boleta es de cortesia
                with col6:
                    # Si el evento seleccionado es de tipo "Filantropico"
                    if cliente.nombre_evento == "Filantropico":
                        cliente.cortesia = True
                    else:
                        # Si el número de boletas vendidas está en la lista de cortesias del evento
                        if len(evento.boletas_vendidas) in evento.lista_cortesias:
                            cliente.cortesia = True

                        # Si la boleta es de cortesia
                        if cliente.cortesia:
                            cliente.precio = 0
                            st.write("La boleta es de cortesia")

                boton_confirmacion = st.button("Vender Boleta")

                # Si se presiona el botón de confirmación y todos los campos necesarios están llenos
                if boton_confirmacion and cliente.comprador != "" and cliente.fuente != "" and cliente.metodo_pago != "":
                    # Se establece la fecha de compra como la fecha actual, el lugar, la dirección y la fase de venta de la boleta
                    cliente.fecha_compra = datetime.today().strftime('%Y-%m-%d')
                    cliente.lugar = evento.lugar
                    cliente.direccion = evento.direccion
                    cliente.fase_venta = evento.fase_venta
                    st.write("Boleta vendida exitosamente")
                    # Se crea un objeto Boleta con los datos recogidos
                    boleta = Boleta(cliente.nombre_evento, cliente.comprador, cliente.fuente, cliente.metodo_pago,
                                    evento.fase_venta, cliente.precio, cliente.cortesia)
                    # Si el evento es de tipo 'Bar', se calculan los ingresos para el bar y el artista
                    if evento.tipo_evento == 'Bar':
                        evento.ingresos_bar += cliente.precio * 0.2
                        evento.ingresos_artista += cliente.precio * 0.8
                        ingreso_por_artista = evento.ingresos_artista / len(evento.artistas)
                        for artista in evento.artistas:
                            artista.ingresos = ingreso_por_artista

                    # Si el evento es de tipo 'Teatro', se calculan los ingresos para el teatro
                    elif evento.tipo_evento == 'Teatro':
                        evento.ingresos_teatro += cliente.precio * 0.93
                    # Se añade la boleta vendida a la lista de boletas vendidas del evento
                    evento.boletas_vendidas.append(boleta)
                    # Se crea un objeto FPDF para generar el PDF de la boleta
                    pdf = FPDF()
                    # Se añade una página al PDF y se establece la fuente
                    pdf.add_page()
                    pdf.set_font("Arial", size=12)
                    # Se añaden celdas al PDF con los detalles de la boleta
                    pdf.cell(200, 10, txt="Boleta para el evento", ln=True, align='C')
                    pdf.cell(200, 10, txt=f"Evento: {cliente.nombre_evento}", ln=True, align='C')
                    nombres_artistas = []
                    if len(evento.artistas) > 1:
                        for artists in evento.artistas:
                            nombres_artistas.append(artists.nombre)
                        artistas = ", ".join(nombres_artistas)
                        pdf.cell(200, 10, txt=f"Artistas: {artistas}", ln=True, align='C')
                    else:
                        nombres_artistas.append(evento.artistas[0].nombre)
                        artistas = ", ".join(nombres_artistas)
                        pdf.cell(200, 10, txt=f"Artista: {artistas}", ln=True, align='C')
                    pdf.cell(200, 10, txt=f"Comprador: {cliente.comprador}", ln=True, align='C')
                    pdf.cell(200, 10, txt=f"Fecha: {cliente.fecha_compra}", ln=True, align='C')
                    pdf.cell(200, 10, txt=f"Lugar: {cliente.lugar}", ln=True, align='C')
                    pdf.cell(200, 10, txt=f"Dirección: {cliente.direccion}", ln=True, align='C')
                    # Si la boleta es de cortesia, se añade una celda indicándolo
                    if cliente.cortesia:
                        pdf.cell(200, 10, txt=f"La Boleta es de Cortesia", ln=True, align='C')
                    # Si no, se añade una celda con el precio de la boleta
                    else:
                        pdf.cell(200, 10, txt=f"Precio: {cliente.precio}", ln=True, align='C')
                    # Se genera el nombre del archivo PDF y se guarda el PDF
                    pdf_output = f"boleta_{cliente.comprador}_{cliente.id}.pdf"
                    pdf.output(pdf_output)
                    st.write("Boleta generada exitosamente")
                # Si se presiona el botón pero no todos los campos están llenos, se muestra un mensaje de error
                elif boton_confirmacion:
                    st.write("Por favor llene todos los campos")
                else:
                    st.info("No deje Ningún Espacio en Blanco")

    # Devuelve el controlador con la nueva boleta vendida
    return controlador


def generar_reportes(st, controlador):
    st.title("Generar Reportes")

    col1, col2, col3, col4 = st.columns(4)

    # En la primera columna
    with col1:
        if not controlador.lista_eventos:
            st.warning("No hay eventos registrados")
        else:
            # Selecciona el tipo de reporte a generar
            opcion_rep = st.selectbox("Elija reporte a generar",
                                      ["Reporte Ventas", "Reporte Financiero", "Reporte de Datos de los Compradores",
                                       "Reporte de Datos por Artista"])

            # Si el reporte seleccionado es "Reporte Ventas"
            if opcion_rep == "Reporte Ventas":
                # Selecciona el evento para el que se va a generar el reporte
                opcion = st.selectbox("Eliga el evento a generar reportes",
                                      [evento.nombre for evento in controlador.lista_eventos])

                # Busca el evento seleccionado en la lista de eventos del controlador
                evento = next((evento for evento in controlador.lista_eventos if evento.nombre == opcion), None)

                # Si no hay boletas vendidas para el evento, muestra un mensaje de advertencia
                # Si hay boletas vendidas, se revisa el estado actual del evento
                if not evento.boletas_vendidas:
                    st.warning("No hay boletas vendidas")
                elif evento.estado == 'Realizado':
                    st.warning("El evento ya fue realizado")
                elif evento.estado == 'Cancelado':
                    st.warning("El evento fue cancelado")
                else:
                    # Si el evento es de tipo 'Filantropico', no se puede generar un reporte de ventas
                    if evento.tipo_evento == 'Filantropico':
                        st.write("No se puede generar reporte de ventas de un evento filantrópico")
                    else:
                        # Calcula la suma de los precios de las boletas vendidas en preventa y en venta
                        preventa = sum(
                            boleta.precio for boleta in evento.boletas_vendidas if boleta.fase_venta == "Preventa")
                        venta = sum(boleta.precio for boleta in evento.boletas_vendidas if boleta.fase_venta == "Venta")

                        # Calcula la cantidad de boletas vendidas en preventa y en venta
                        cant_pre = len(
                            [boleta for boleta in evento.boletas_vendidas if boleta.fase_venta == "Preventa"])
                        cant_ven = len([boleta for boleta in evento.boletas_vendidas if boleta.fase_venta == "Venta"])

                        # Crea una lista con los datos de las boletas vendidas en preventa y en venta
                        prev = ["Preventa", cant_pre, preventa]
                        ven = ["Venta", cant_ven, venta]
                        rep = [prev, ven]

                        # Crea un DataFrame con los datos de las boletas vendidas y lo muestra
                        df_reporte = pd.DataFrame(rep, columns=["Nombre", "Cantidad", "Ingresos"])
                        st.write(df_reporte)

            elif opcion_rep == "Reporte Financiero":
                opcion = st.selectbox("Eliga el evento a generar reportes",
                                      [evento.nombre for evento in controlador.lista_eventos])

                evento = next((evento for evento in controlador.lista_eventos if evento.nombre == opcion), None)
                if evento.tipo_evento == 'Filantropico':
                    evento_patrocinadores = {
                        'Patrocinadores': [],
                        'Aporte': []
                    }
                    for patrocinador in evento.patrocinadores:
                        evento_patrocinadores['Patrocinadores'].append(patrocinador.nombre)
                        evento_patrocinadores['Aporte'].append(patrocinador.aporta)
                    df_reporte = pd.DataFrame(evento_patrocinadores)
                    st.write(df_reporte)
                elif not evento.boletas_vendidas:
                    st.warning("No hay boletas vendidas")
                elif evento.estado == 'Realizado':
                    st.warning("El evento ya fue realizado")
                elif evento.estado == 'Cancelado':
                    st.warning("El evento fue cancelado")
                else:
                    preventa_efe = sum(boleta.precio for boleta in evento.boletas_vendidas if
                                       boleta.fase_venta == "Preventa" and boleta.metodo_pago == "Efectivo")
                    preventa_tar_cre = sum(boleta.precio for boleta in evento.boletas_vendidas if
                                           boleta.fase_venta == "Preventa" and boleta.metodo_pago == "Tarjeta de crédito")
                    preventa_tar_deb = sum(boleta.precio for boleta in evento.boletas_vendidas if
                                           boleta.fase_venta == "Preventa" and boleta.metodo_pago == "Tarjeta débito")
                    venta_efe = sum(boleta.precio for boleta in evento.boletas_vendidas if
                                    boleta.fase_venta == "Venta" and boleta.metodo_pago == "Efectivo")
                    venta_tar_cre = sum(boleta.precio for boleta in evento.boletas_vendidas if
                                        boleta.fase_venta == "Venta" and boleta.metodo_pago == "Tarjeta de crédito")
                    venta_tar_deb = sum(boleta.precio for boleta in evento.boletas_vendidas if
                                        boleta.fase_venta == "Venta" and boleta.metodo_pago == "Tarjeta débito")
                    if evento.tipo_evento == 'Bar':
                        evento.ingresos_bar = (
                                                          preventa_efe + preventa_tar_cre + preventa_tar_deb + venta_efe + venta_tar_cre + venta_tar_deb) * 0.2
                        evento.ingresos_artista = (
                                                              preventa_efe + preventa_tar_cre + preventa_tar_deb + venta_efe + venta_tar_cre + venta_tar_deb) * 0.8
                        prev = ["Preventa", "Efectivo", preventa_efe * 0.2, preventa_efe * 0.8]
                        prev2 = ["Preventa", "Tarjeta de crédito", preventa_tar_cre * 0.2, preventa_tar_cre * 0.8]
                        prev3 = ["Preventa", "Tarjeta débito", preventa_tar_deb * 0.2, preventa_tar_deb * 0.8]
                        ven = ["Venta", "Efectivo", venta_efe * 0.2, venta_efe * 0.8]
                        ven2 = ["Venta", "Tarjeta de crédito", venta_tar_cre * 0.2, venta_tar_cre * 0.8]
                        ven3 = ["Venta", "Tarjeta débito", venta_tar_deb * 0.2, venta_tar_deb * 0.8]
                        ingresos_totales = [["Ingresos Totales", evento.ingresos_bar, evento.ingresos_artista]]
                        rep = [prev, prev2, prev3, ven, ven2, ven3]

                        df_reporte = pd.DataFrame(rep, columns=["Tipo", "Metodo", "Ingresos Bar", "Ingresos Artista"])
                        df_reporte_total = pd.DataFrame(ingresos_totales,
                                                        columns=["Tipo", "Ingresos Bar", "Ingresos Artista"])

                        st.write(df_reporte)
                        st.write(df_reporte_total)
                    elif evento.tipo_evento == 'Teatro':
                        evento.ingresos_teatro = (
                                    preventa_efe + preventa_tar_cre + preventa_tar_deb + venta_efe + venta_tar_cre + venta_tar_deb)
                        evento.gananacias_teatro = evento.ingresos_teatro * 0.93 - evento.costo_alquiler
                        ingresos_tiquetera = evento.ingresos_teatro * 0.07
                        prev = ["Preventa", "Efectivo", preventa_efe]
                        prev2 = ["Preventa", "Tarjeta de crédito", preventa_tar_cre]
                        prev3 = ["Preventa", "Tarjeta débito", preventa_tar_deb]
                        ven = ["Venta", "Efectivo", venta_efe]
                        ven2 = ["Venta", "Tarjeta de crédito", venta_tar_cre]
                        ven3 = ["Venta", "Tarjeta débito", venta_tar_deb]
                        ingresos_generales = [
                            ["Ingresos Totales", evento.ingresos_teatro - ingresos_tiquetera, ingresos_tiquetera]]

                        rep = [prev, prev2, prev3, ven, ven2, ven3]

                        df_reporte = pd.DataFrame(rep, columns=["Tipo", "Metodo", "Ingresos"])
                        df_reporte_total = pd.DataFrame(ingresos_generales,
                                                        columns=["Tipo", "Ingresos Teatro", "Ingresos Tiquetera"])
                        st.write(df_reporte)
                        st.write(df_reporte_total)

            elif opcion_rep == "Reporte de Datos de los Compradores":
                opcion = st.selectbox("Eliga el evento a generar reportes",
                                      [evento.nombre for evento in controlador.lista_eventos])

                evento = next((evento for evento in controlador.lista_eventos if evento.nombre == opcion), None)
                if not evento.boletas_vendidas:
                    st.warning("No hay boletas vendidas")
                elif evento.estado == 'Realizado':
                    st.warning("El evento ya fue realizado")
                elif evento.estado == 'Cancelado':
                    st.warning("El evento fue cancelado")
                else:
                    compradores = {
                        'Comprador': [],
                        'Fuente': [],
                        'Fase de Venta': [],
                        'Precio': []

                    }
                    for boleta in evento.boletas_vendidas:
                        compradores['Comprador'].append(boleta.comprador)
                        compradores['Fuente'].append(boleta.fuente)
                        compradores['Fase de Venta'].append(boleta.fase_venta)
                        compradores['Precio'].append(boleta.precio if not boleta.cortesia else 0)

                    df_compradores = pd.DataFrame(compradores)

                    st.download_button(
                        label="Descargar reporte de compradores en Excel",
                        data=df_compradores.to_csv(index=False),
                        file_name="compradores.csv",
                        mime="text/csv",
                    )

                    fig = px.histogram(df_compradores, x='Fuente', title='Distribución de Compradores por Fuente')
                    fig2 = px.histogram(df_compradores, x='Fase de Venta',
                                        title='Distribución de Compradores por Fase de Venta')
                    boton = st.button("Mostrar gráficos")

                    if boton:
                        fig.show()
                        fig2.show()

            elif opcion_rep == "Reporte de Datos por Artista":
                if not controlador.lista_eventos:
                    st.write("No hay eventos registrados")
                else:
                    if not controlador.lista_artistas:
                        st.write("No hay artistas registrados")
                    else:
                        opc = st.selectbox("Nombre Artista", [artista.nombre for artista in controlador.lista_artistas])
                        artista_datos = next((artist for artist in controlador.lista_artistas if artist.nombre == opc),
                                             None)

                        evento_artistas = {
                            'Nombre_evento': [],
                            'Tipo': [],
                            'Fecha evento': [],
                            'Lugar evento': [],
                            'Cantidad boletas vendidas': [],
                            'Porcentaje aforo': []
                        }
                        for evento in artista_datos.eventos_ingresados:
                            evento_artistas['Nombre_evento'].append(evento.nombre)
                            evento_artistas['Tipo'].append(evento.tipo_evento)
                            evento_artistas['Fecha evento'].append(evento.fecha)
                            evento_artistas['Lugar evento'].append(evento.lugar)
                            evento_artistas['Cantidad boletas vendidas'].append(len(evento.boletas_vendidas))
                            if evento.aforo_total != 0:
                                porcentaje_aforo = (len(evento.boletas_vendidas) * 100) / evento.aforo_total
                            else:
                                porcentaje_aforo = 0
                            evento_artistas['Porcentaje aforo'].append(porcentaje_aforo)

                        df_info_artista = pd.DataFrame(evento_artistas)
                        st.write(df_info_artista)

    return controlador


def ingresar_evento(st, controlador):
    st.title("Ingresar Evento")

    # Si no hay eventos registrados, muestra una advertencia
    if not controlador.lista_eventos:
        st.warning("No hay eventos registrados")
    else:
        # Barra desplegable para seleccionar el evento
        opcion = st.selectbox("Eliga el evento a ingresar",
                              [evento.nombre for evento in controlador.lista_eventos])
        # Busca el evento seleccionado en la lista de eventos del controlador
        evento = next((evento for evento in controlador.lista_eventos if evento.nombre == opcion), None)

        # Si no hay boletas vendidas para el evento, muestra una advertencia
        if not evento.boletas_vendidas:
            st.warning("No hay boletas vendidas")
        # Si el evento ya fue realizado, muestra una advertencia
        elif evento.estado == 'Realizado':
            st.warning("El evento ya fue realizado")
        # Si el evento fue cancelado, muestra una advertencia
        elif evento.estado == 'Cancelado':
            st.warning("El evento fue cancelado")
        else:
            # Selecciona el nombre del comprador desde un desplegable
            nombre = st.selectbox("Nombre del comprador", [boleta.comprador for boleta in evento.boletas_vendidas])

            # Busca la boleta del comprador en la lista de boletas vendidas del evento
            boleta = next((boleta for boleta in evento.boletas_vendidas if boleta.comprador == nombre), None)
            # Crea un botón para confirmar el ingreso
            boton_confirmar = st.button("Confirmar Ingreso")

            # Si el comprador ya ingresó al evento, muestra un mensaje
            if boleta.confirmado:
                st.write("El comprador ya ingresó al evento")
            # Si se presiona el botón de confirmación, confirma el ingreso y muestra un mensaje
            elif boton_confirmar:
                boleta.confirmado = True
                st.write("Ingreso confirmado")
            # Crea un diccionario para almacenar la asistencia
            asistencia = {
                'Comprador': [],
                'Confirmado': []
            }
            # Para cada boleta vendida en el evento, agrega el comprador y el estado de confirmación al diccionario
            for boleta in evento.boletas_vendidas:
                asistencia['Comprador'].append(boleta.comprador)
                asistencia['Confirmado'].append(boleta.confirmado)
            # Crea un DataFrame de pandas con la asistencia y lo muestra
            df_asistencia = pd.DataFrame(asistencia, columns=["Comprador", "Confirmado"])
            st.write(df_asistencia)

    return controlador