import numpy as np
from model.pieza import Pieza, Jugador, TipoPieza

class Tablero:
    def __init__(self):
        self.filas = 8
        self.columnas = 8
        self.matriz = np.zeros((self.filas, self.columnas), dtype=int)
        self.piezas_activas = {}
        self.piezas_p1 = {}
        self.piezas_p2 = {}
        self.turno_actual = Jugador.P1
   
    def vaciar_tablero(self):
        """Limpia todos los datos lógicos para reiniciar la partida."""
        self.matriz = np.zeros((self.filas, self.columnas), dtype=int)
        self.piezas_activas.clear()
        self.piezas_p1.clear()
        self.piezas_p2.clear()
        self.turno_actual = Jugador.P1

    def iniciar_nueva_partida(self):
        """Reinicia los datos y coloca las piezas iniciales."""
        self.vaciar_tablero()
        self._inicializar_tablero()


    def _inicializar_tablero(self):
        """
        Coloca las piezas en sus posiciones iniciales.
        """
        id_contador = 1  # ID único incremental para cada pieza
        
        # Cada jugador comienza con 12 fichas[cite: 1095].
        # Se ubican en las casillas oscuras de las tres primeras filas de cada lado[cite: 1096].
        for fila in range(self.filas):
            for columna in range(self.columnas):
                
                # Determinamos si es una casilla oscura (la suma de índices es impar)
                if (fila + columna) % 2 != 0:
                    
                    # Tres primeras filas para el Jugador 1
                    if fila < 3:
                        nueva_pieza = Pieza(id_contador, Jugador.P1, fila, columna)
                        self.piezas_activas[id_contador] = nueva_pieza
                        self.piezas_p1[id_contador] = nueva_pieza  # Guardamos referencia en P1
                        self.matriz[fila][columna] = id_contador
                        id_contador += 1
                        
                    # Tres últimas filas para el Jugador 2 (filas 5, 6 y 7)
                    elif fila > 4:
                        nueva_pieza = Pieza(id_contador, Jugador.P2, fila, columna)
                        self.piezas_activas[id_contador] = nueva_pieza
                        self.piezas_p2[id_contador] = nueva_pieza  # Guardamos referencia en P2
                        self.matriz[fila][columna] = id_contador
                        id_contador += 1

    def obtener_pieza_en(self, fila, columna):
        """
        Retorna el objeto Pieza en la coordenada dada, o None si está vacía.
        """
        # Verificamos que las coordenadas estén dentro del tablero para evitar errores
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            id_pieza = self.matriz[fila][columna]
            if id_pieza != 0:
                return self.piezas_activas.get(id_pieza)
        return None

    # --- ACTIVIDAD 1: Validación de Selección ---
    def es_seleccion_valida(self, fila, columna):
        """
        Verifica si en la coordenada indicada hay una pieza y si pertenece 
        al jugador que tiene el turno actualmente.
        Retorna: El objeto 'Pieza' si es válida, o 'None' si es inválida.
        """
        pieza = self.obtener_pieza_en(fila, columna)
        
        if pieza is not None and pieza.jugador == self.turno_actual:
            return pieza  # Es una ficha tuya, puedes seleccionarla
            
        return None  # Está vacío o es una ficha del rival

    def cambiar_turno(self):
        """Alterna el turno de juego."""
        if self.turno_actual == Jugador.P1:
            self.turno_actual = Jugador.P2
        else:
            self.turno_actual = Jugador.P1

    def obtener_movimientos_validos(self, pieza):
        """
        Calcula los movimientos y capturas permitidos para una pieza específica.
        Retorna un diccionario donde:
        - Las llaves son las coordenadas de destino: (f_dest, c_dest)
        - Los valores son listas de las piezas capturadas en ese movimiento: [(f_cap, c_cap)]
        """
        movimientos = {}
        capturas = {}

        # Definimos la dirección matemática de avance (+1 hacia abajo para P1, -1 hacia arriba para P2)
        direccion = 1 if pieza.jugador == Jugador.P1 else -1

        # --- 1. Calcular Pasos Normales (Diagonales adyacentes) ---
        diagonales_paso = [(direccion, -1), (direccion, 1)]

        for df, dc in diagonales_paso:
            f_dest = pieza.fila + df
            c_dest = pieza.columna + dc

            # Verificamos que no nos salgamos de la matriz 8x8
            if 0 <= f_dest < self.filas and 0 <= c_dest < self.columnas:
                # El movimiento es válido si la casilla de destino está completamente vacía (0)
                if self.matriz[f_dest][c_dest] == 0:
                    movimientos[(f_dest, c_dest)] = [] # Lista vacía porque no captura a nadie

        # --- 2. Calcular Capturas (Saltos) ---
        diagonales_salto = [(direccion * 2, -2), (direccion * 2, 2)]
        diagonales_intermedias = [(direccion, -1), (direccion, 1)]

        for i in range(2): # Revisamos la diagonal izquierda y la derecha
            f_salto = pieza.fila + diagonales_salto[i][0]
            c_salto = pieza.columna + diagonales_salto[i][1]

            f_intermedia = pieza.fila + diagonales_intermedias[i][0]
            c_intermedia = pieza.columna + diagonales_intermedias[i][1]

            # Verificamos que el punto de aterrizaje esté dentro del tablero
            if 0 <= f_salto < self.filas and 0 <= c_salto < self.columnas:
                # La casilla de aterrizaje debe estar vacía
                if self.matriz[f_salto][c_salto] == 0:
                    id_intermedio = self.matriz[f_intermedia][c_intermedia]
                    
                    # Debe haber "algo" en la casilla que vamos a saltar
                    if id_intermedio != 0:
                        pieza_intermedia = self.piezas_activas[id_intermedio]
                        
                        # Ese "algo" debe pertenecer estrictamente al oponente
                        if pieza_intermedia.jugador != pieza.jugador:
                            capturas[(f_salto, c_salto)] = [(f_intermedia, c_intermedia)]

        # Regla estándar de damas: Si existe la posibilidad de capturar, estás obligado a hacerlo.
        if capturas:
            return capturas
        
        return movimientos
    def ejecutar_movimiento(self, pieza, f_dest, c_dest, capturas_asociadas):
        # 1. Mover la ficha matemáticamente
        self.matriz[pieza.fila][pieza.columna] = 0
        pieza.actualizar_posicion(f_dest, c_dest)
        self.matriz[f_dest][c_dest] = pieza.id
        
        hubo_captura = False
        
        # 2. Eliminar la pieza enemiga si fue un salto
        if capturas_asociadas:
            hubo_captura = True
            for f_cap, c_cap in capturas_asociadas:
                id_capturada = self.matriz[f_cap][c_cap]
                self.matriz[f_cap][c_cap] = 0
                if id_capturada in self.piezas_activas:
                    pieza_comida = self.piezas_activas.pop(id_capturada)
                    if pieza_comida.jugador == Jugador.P1:
                        self.piezas_p1.pop(id_capturada, None)
                    else:
                        self.piezas_p2.pop(id_capturada, None)
                        
        # 3. Evaluar Coronación (El turno termina automáticamente al coronar)
        if pieza.tipo != TipoPieza.DAMA:
            if (pieza.jugador == Jugador.P1 and f_dest == self.filas - 1) or \
               (pieza.jugador == Jugador.P2 and f_dest == 0):
                pieza.coronar()
                self.cambiar_turno()
                return True # Turno terminado
                
        # 4. Evaluar Saltos Múltiples Obligatorios
        if hubo_captura:
            movs_futuros = self.obtener_movimientos_validos(pieza)
            # Verificamos si dentro de los movimientos futuros hay alguna captura
            tiene_capturas_extra = False
            for caps in movs_futuros.values():
                if len(caps) > 0: # Si la lista de capturas no está vacía
                    tiene_capturas_extra = True
                    break
                    
            if tiene_capturas_extra:
                return False # El turno NO ha terminado, debe dar el siguiente paso

        # 5. Si fue un movimiento normal o se acabaron las capturas
        self.cambiar_turno()
        return True # Turno terminado

    def verificar_victoria(self):
        """
        Evalúa las dos condiciones de término del juego.
        Retorna el Jugador ganador (Jugador.P1 o Jugador.P2), o None si el juego continúa.
        """
        # Condición 1: Un jugador se quedó sin fichas
        if len(self.piezas_p1) == 0:
            return Jugador.P2
        if len(self.piezas_p2) == 0:
            return Jugador.P1

        # Condición 2: El jugador del turno actual no tiene movimientos válidos (Ahogado)
        movimientos_disponibles = False
        piezas_del_turno = self.piezas_p1 if self.turno_actual == Jugador.P1 else self.piezas_p2

        for pieza in piezas_del_turno.values():
            if self.obtener_movimientos_validos(pieza): # Si devuelve algo, tiene al menos 1 movimiento
                movimientos_disponibles = True
                break # Rompemos el ciclo para optimizar, ya sabemos que puede jugar

        if not movimientos_disponibles:
            # Si el jugador actual no puede moverse, el oponente gana automáticamente
            return Jugador.P2 if self.turno_actual == Jugador.P1 else Jugador.P1

        # Si ninguna condición se cumple, el juego sigue
        return None

    def obtener_movimientos_validos(self, pieza):
        movimientos = {}
        capturas = {}

        # --- CORRECCIÓN: Direcciones de la Dama ---
        if pieza.tipo == TipoPieza.DAMA:
            direcciones = [(-1, -1), (-1, 1), (1, -1), (1, 1)] # Todas las direcciones
        else:
            direccion = 1 if pieza.jugador == Jugador.P1 else -1
            direcciones = [(direccion, -1), (direccion, 1)] # Solo hacia adelante

        # 1. Calcular Pasos Normales
        for df, dc in direcciones:
            f_dest = pieza.fila + df
            c_dest = pieza.columna + dc
            if 0 <= f_dest < self.filas and 0 <= c_dest < self.columnas:
                if self.matriz[f_dest][c_dest] == 0:
                    movimientos[(f_dest, c_dest)] = [] 

        # 2. Calcular Capturas (Saltos)
        for df, dc in direcciones:
            f_salto = pieza.fila + df * 2
            c_salto = pieza.columna + dc * 2
            f_intermedia = pieza.fila + df
            c_intermedia = pieza.columna + dc

            if 0 <= f_salto < self.filas and 0 <= c_salto < self.columnas:
                if self.matriz[f_salto][c_salto] == 0:
                    id_intermedio = self.matriz[f_intermedia][c_intermedia]
                    if id_intermedio != 0:
                        pieza_intermedia = self.piezas_activas[id_intermedio]
                        if pieza_intermedia.jugador != pieza.jugador:
                            capturas[(f_salto, c_salto)] = [(f_intermedia, c_intermedia)]

        if capturas:
            return capturas
        return movimientos