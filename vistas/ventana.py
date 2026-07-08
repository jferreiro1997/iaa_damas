from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QMainWindow, QGraphicsScene, QLabel, QGraphicsRectItem, QGraphicsEllipseItem
from PySide6.QtGui import QBrush, QColor, QPen
from vistas.VentanaPrincipal import Ui_VentanaDamas

class EscenaTablero(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controlador = None

    def mousePressEvent(self, event):
        # Si tenemos un controlador conectado, le enviamos las coordenadas X e Y
        if self.controlador:
            x = event.scenePos().x()
            y = event.scenePos().y()
            self.controlador.procesar_clic_tablero(x, y)
            
        # Siempre es buena práctica llamar al evento original de la clase padre
        super().mousePressEvent(event)

class VentanaDamas(QMainWindow, Ui_VentanaDamas):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Reemplazamos el QGraphicsScene genérico por nuestra EscenaTablero interactiva
        self.escena_tablero = EscenaTablero(self)
        self.vista_tablero.setScene(self.escena_tablero)
        
        self.vista_tablero.setRenderHint(self.vista_tablero.renderHints()) 
        self.vista_tablero.setStyleSheet("background-color: #2b2b2b;")
        
        self.tamano_casilla = 80

        self.indicadores_de_movimiento = []

        self.turno_label = QLabel("Esperando para iniciar...", self.panel_lateral)
        self.turno_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.turno_label.setStyleSheet("font-size: 16px; font-weight: bold; color: white; margin-bottom: 4px;")
        self.verticalLayout.insertWidget(1, self.turno_label) # Se inserta justo debajo del título principal

        # --- 2. CONFIGURACIÓN DEL CRONÓMETRO ---
        self.timer = QTimer(self)
        self.tiempo_transcurrido = 0
        self.timer.timeout.connect(self.actualizar_reloj)

    def limpiar_fichas_visuales(self):
        """Recorre la escena y elimina SOLO los círculos (fichas), dejando el tablero de madera."""
        for item in self.escena_tablero.items():
            if isinstance(item, QGraphicsEllipseItem):
                self.escena_tablero.removeItem(item)

    def iniciar_cronometro(self):
        self.tiempo_restante = 300  # 5 minutos en segundos
        self.temporizador_tiempo.setText("05:00")
        self.timer.start(1000)

    def detener_cronometro(self):
        self.timer.stop()

    def actualizar_reloj(self):
        """Disminuye los segundos, actualiza la UI y avisa si se acaba el tiempo."""
        self.tiempo_restante -= 1
        
        # Formateamos para que siempre tenga 2 dígitos (ej. 04:59)
        minutos = self.tiempo_restante // 60
        segundos = self.tiempo_restante % 60
        self.temporizador_tiempo.setText(f"{minutos:02d}:{segundos:02d}")

        # ¿Qué pasa cuando llega a cero?
        if self.tiempo_restante <= 0:
            self.detener_cronometro()
            self.temporizador_tiempo.setText("00:00")
            # Le avisamos al cerebro (Controlador) que el tiempo se acabó
            if self.escena_tablero.controlador:
                self.escena_tablero.controlador.tiempo_agotado()

    def mostrar_turno(self, nombre_jugador):
        self.turno_label.setText(f"Turno de: {nombre_jugador}")

    def preparar_eventos(self, controlador):
        self.escena_tablero.controlador = controlador
        # Conectamos los botones de la interfaz a los métodos del Controlador
        self.pushButton.clicked.connect(controlador.boton_iniciar_clic)
        self.pushButton_2.clicked.connect(controlador.boton_reiniciar_clic)

    def dibujar_tablero_base(self):
        """
        Dibuja la cuadrícula de 8x8 con colores alternados.
        """
        # Definimos colores elegantes para el tablero (pueden cambiarlos después)
        color_claro = QColor("#F0D9B5")
        color_oscuro = QColor("#B58863")
        
        # Iteramos sobre las 8 filas y 8 columnas
        for fila in range(8):
            for columna in range(8):
                # Calcular coordenadas X e Y en píxeles
                x = columna * self.tamano_casilla
                y = fila * self.tamano_casilla
                
                # Crear el rectángulo para la casilla
                rectangulo = QGraphicsRectItem(x, y, self.tamano_casilla, self.tamano_casilla)
                
                # Quitar el borde negro por defecto de los rectángulos
                rectangulo.setPen(QPen(Qt.NoPen)) 
                
                # Lógica del patrón de ajedrez (Par = Claro, Impar = Oscuro)
                if (fila + columna) % 2 == 0:
                    rectangulo.setBrush(QBrush(color_claro))
                else:
                    rectangulo.setBrush(QBrush(color_oscuro))
                
                # Agregar el rectángulo a la escena gráfica
                self.escena_tablero.addItem(rectangulo)

    def dibujar_fichas(self, matriz, piezas_activas):
        """
        Lee la matriz matemática y dibuja las fichas en sus coordenadas correspondientes.
        """
        # Definimos un margen para que la ficha sea ligeramente más pequeña que la casilla
        padding = 10
        tamano_ficha = self.tamano_casilla - (padding * 2)

        # Colores para identificar a los jugadores
        color_j1 = QColor("#2C2C2C") # Gris muy oscuro casi negro
        color_j2 = QColor("#EEE1B5") # Blanco hueso

        for fila in range(8):
            for columna in range(8):
                id_pieza = matriz[fila][columna]
                
                # Si hay un ID distinto de 0, significa que hay una pieza en esa coordenada
                if id_pieza != 0:
                    pieza = piezas_activas[id_pieza]
                    
                    # Calculamos la posición X e Y sumando el padding para centrar la ficha
                    x = (columna * self.tamano_casilla) + padding
                    y = (fila * self.tamano_casilla) + padding
                    
                    ficha_visual = QGraphicsEllipseItem(x, y, tamano_ficha, tamano_ficha)
                    ficha_visual.setPen(QPen(Qt.NoPen)) # Sin borde negro feo
                    
                    # Asignamos el color dependiendo del dueño de la pieza
                    if pieza.jugador.value == 1:
                        ficha_visual.setBrush(QBrush(color_j1))
                    else:
                        ficha_visual.setBrush(QBrush(color_j2))
                        
                    self.escena_tablero.addItem(ficha_visual)

    def limpiar_resaltado(self):
        """Elimina los indicadores visuales de movimientos previos de la escena."""
        for indicador in self.indicadores_de_movimiento:
            self.escena_tablero.removeItem(indicador)
        # Vaciamos la lista una vez eliminados de la pantalla
        self.indicadores_de_movimiento.clear()

    def resaltar_movimientos(self, lista_coordenadas):
        """Dibuja recuadros verdes semi-transparentes en las casillas de destino posibles."""
        # QColor(Rojo, Verde, Azul, Canal Alfa/Transparencia)
        color_resalte = QColor(147, 255, 154, 150) 
        
        for fila, columna in lista_coordenadas:
            # Calculamos la posición exacta en píxeles
            x = columna * self.tamano_casilla
            y = fila * self.tamano_casilla
            
            # Creamos un rectángulo exacto del tamaño de la casilla
            indicador = QGraphicsRectItem(x, y, self.tamano_casilla, self.tamano_casilla)
            indicador.setBrush(QBrush(color_resalte))
            indicador.setPen(QPen(Qt.NoPen)) # Sin bordes
            
            # Lo añadimos a la escena gráfica y a nuestra lista de memoria
            self.escena_tablero.addItem(indicador)
            self.indicadores_de_movimiento.append(indicador)