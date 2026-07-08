from model.pieza import Jugador

class ControladorJuego:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.partida_en_curso = False # Variable de estado fundamental
        self.pieza_seleccionada = None
        
        self.vista.preparar_eventos(self)

    def iniciar(self):
        """Arranque inicial de la app. Solo dibuja el tablero vacío."""
        self.vista.dibujar_tablero_base()

    def boton_iniciar_clic(self):
        """Se ejecuta al presionar el botón 'Iniciar'."""
        if self.partida_en_curso:
            return # Si ya estamos jugando, no hacemos nada

        self.partida_en_curso = True
        
        # 1. Llenamos el modelo lógicamente
        self.modelo.iniciar_nueva_partida()
        
        # 2. Dibujamos las fichas
        self.vista.dibujar_fichas(self.modelo.matriz, self.modelo.piezas_activas)
        
        # 3. Arrancamos reloj y turnos
        self.vista.iniciar_cronometro()
        self.actualizar_interfaz_turno()
        
        # 4. Bloqueamos el botón iniciar y nombres para que no los cambien a mitad de partida
        self.vista.pushButton.setEnabled(False)
        self.vista.jugador_1_nombre_input.setEnabled(False)
        self.vista.jugador_2_nombre_input.setEnabled(False)

    def boton_reiniciar_clic(self):
        """Se ejecuta al presionar el botón 'Reiniciar Partida'."""
        self.partida_en_curso = False
        
        # 1. Detenemos cronómetro y limpiamos textos
        self.vista.detener_cronometro()
        self.vista.temporizador_tiempo.setText("05:00") # ¡Actualizado a 5 min!
        self.vista.turno_label.setText("Esperando para iniciar...")

        # 2. Vaciamos las fichas visuales y la memoria lógica
        self.vista.limpiar_fichas_visuales()
        self.modelo.vaciar_tablero()
        
        # 3. Reactivamos botones y campos de texto
        self.vista.pushButton.setEnabled(True)
        self.vista.jugador_1_nombre_input.setEnabled(True)
        self.vista.jugador_2_nombre_input.setEnabled(True)

        self.vista.turno_label.setStyleSheet("font-size: 16px; font-weight: bold; color: white; margin-bottom: 4px;")

    def actualizar_interfaz_turno(self):
        """Busca el nombre del jugador en la UI y lo pone en el turno_label."""
        if self.modelo.turno_actual == Jugador.P1:
            nombre = self.vista.jugador_1_nombre_input.text()
        else:
            nombre = self.vista.jugador_2_nombre_input.text()
            
        self.vista.mostrar_turno(nombre)

    def procesar_clic_tablero(self, x, y):
        """Filtra y procesa la interacción paso a paso del usuario."""
        if not self.partida_en_curso:
            return
            
        columna = int(x // self.vista.tamano_casilla)
        fila = int(y // self.vista.tamano_casilla)
        
        if not (0 <= fila < 8 and 0 <= columna < 8):
            return

        # --- ESTADO DE BLOQUEO: Captura en Cadena ---
        if getattr(self, 'captura_en_cadena', False):
            movimientos_posibles = self.modelo.obtener_movimientos_validos(self.pieza_seleccionada)
            
            if (fila, columna) in movimientos_posibles:
                capturas = movimientos_posibles[(fila, columna)]
                
                # Ejecutamos el salto intermedio
                turno_terminado = self.modelo.ejecutar_movimiento(self.pieza_seleccionada, fila, columna, capturas)
                
                # Refrescamos la pantalla para ver el salto paso a paso
                self.vista.limpiar_resaltado()
                self.vista.limpiar_fichas_visuales()
                self.vista.dibujar_fichas(self.modelo.matriz, self.modelo.piezas_activas)
                
                if turno_terminado:
                    # La cadena terminó
                    self.captura_en_cadena = False
                    self.pieza_seleccionada = None
                    ganador = self.modelo.verificar_victoria()
                    if ganador is not None:
                        self.finalizar_partida(ganador)
                    else:
                        self.actualizar_interfaz_turno()
                else:
                    # Quedan más saltos. Volvemos a pintar las opciones verdes.
                    nuevos_movs = self.modelo.obtener_movimientos_validos(self.pieza_seleccionada)
                    self.vista.resaltar_movimientos(list(nuevos_movs.keys()))
            else:
                print("Movimiento Inválido. Estás obligado a completar la captura múltiple.")
            
            return # SALIMOS AQUÍ. Prohibido ejecutar la fase de selección.

        # --- FASE 1: Movimiento Normal (Primera acción) ---
        if self.pieza_seleccionada:
            movimientos_posibles = self.modelo.obtener_movimientos_validos(self.pieza_seleccionada)
            
            if (fila, columna) in movimientos_posibles:
                capturas = movimientos_posibles[(fila, columna)]
                turno_terminado = self.modelo.ejecutar_movimiento(self.pieza_seleccionada, fila, columna, capturas)
                
                self.vista.limpiar_resaltado()
                self.vista.limpiar_fichas_visuales()
                self.vista.dibujar_fichas(self.modelo.matriz, self.modelo.piezas_activas)
                
                if turno_terminado:
                    self.pieza_seleccionada = None
                    ganador = self.modelo.verificar_victoria()
                    if ganador is not None:
                        self.finalizar_partida(ganador)
                    else:
                        self.actualizar_interfaz_turno()
                else:
                    # ¡Se detectó una cadena! Bloqueamos la UI y mostramos el siguiente paso
                    self.captura_en_cadena = True
                    nuevos_movs = self.modelo.obtener_movimientos_validos(self.pieza_seleccionada)
                    self.vista.resaltar_movimientos(list(nuevos_movs.keys()))
                return

        # --- FASE 2: Selección Inicial ---
        self.vista.limpiar_resaltado()
        pieza = self.modelo.es_seleccion_valida(fila, columna)
        
        if pieza is not None:
            self.pieza_seleccionada = pieza
            movimientos_posibles = self.modelo.obtener_movimientos_validos(pieza)
            if movimientos_posibles:
                self.vista.resaltar_movimientos(list(movimientos_posibles.keys()))
            else:
                self.pieza_seleccionada = None
        else:
            self.pieza_seleccionada = None

    def tiempo_agotado(self):
        """Se ejecuta cuando la cuenta regresiva llega a cero."""
        if not self.partida_en_curso:
            return
            
        self.partida_en_curso = False
        self.vista.turno_label.setText("¡Tiempo agotado! Fin del juego.")
        self.vista.turno_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #ff0000; margin-bottom: 10px;") # Se pone rojo
        print("¡El tiempo se ha agotado! El juego ha sido bloqueado.")

    def finalizar_partida(self, ganador):
        """Detiene el juego y anuncia al ganador en la interfaz."""
        self.partida_en_curso = False
        self.vista.detener_cronometro()
        
        # Determinamos el nombre del ganador leyendo los inputs de la vista
        if ganador == Jugador.P1:
            nombre_ganador = self.vista.jugador_1_nombre_input.text()
            color = "#93FF9A" # Verde pastel
        else:
            nombre_ganador = self.vista.jugador_2_nombre_input.text()
            color = "#93FF9A" 
            
        # Actualizamos la etiqueta superior para mostrar la victoria
        mensaje = f"¡🏆 {nombre_ganador} ha ganado la partida!"
        self.vista.turno_label.setText(mensaje)
        self.vista.turno_label.setStyleSheet(f"font-size: 16px; font-weight: bold; color: {color}; margin-bottom: 10px;")
        
        print(mensaje)
