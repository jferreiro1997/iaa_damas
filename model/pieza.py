from enum import IntEnum

class TipoPieza(IntEnum):
    NORMAL = 1
    DAMA = 2

class Jugador(IntEnum):
    P1 = 1  # Jugador 1 (ej. fichas en la parte superior)
    P2 = 2  # Jugador 2 (ej. fichas en la parte inferior)

class Pieza:
    def __init__(self, id_pieza, jugador, fila, columna):
        self.id = id_pieza
        self.jugador = jugador
        self.tipo = TipoPieza.NORMAL
        self.fila = fila
        self.columna = columna

    def actualizar_posicion(self, nueva_fila, nueva_columna):
        self.fila = nueva_fila
        self.columna = nueva_columna

    def coronar(self):
        self.tipo = TipoPieza.DAMA
        
    def __repr__(self):
        # Representación útil para imprimir en consola durante el desarrollo
        tipo_str = "Dama" if self.tipo == TipoPieza.DAMA else "Normal"
        jugador_str = "P1" if self.jugador == Jugador.P1 else "P2"
        return f"[{self.id}: {jugador_str} {tipo_str} en ({self.fila}, {self.columna})]"
