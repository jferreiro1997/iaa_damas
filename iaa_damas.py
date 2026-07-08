import sys
from PySide6.QtWidgets import QApplication

# Importaciones de nuestra arquitectura MVC
from model.tablero import Tablero
from vistas.ventana import VentanaDamas
from controlador.controlador_damas import ControladorJuego

def main():
    # 1. Crear la instancia global de la aplicación Qt
    app = QApplication(sys.argv)
    
    # 2. Instanciar el Modelo (La lógica y los datos)
    modelo_tablero = Tablero()
    
    # 3. Instanciar la Vista (La interfaz gráfica)
    ventana_principal = VentanaDamas()
    
    # 4. Instanciar el Controlador (El orquestador)
    controlador = ControladorJuego(modelo_tablero, ventana_principal)
    controlador.iniciar()
    
    # 5. Mostrar la ventana en pantalla
    ventana_principal.show()
    
    # 6. Ejecutar el ciclo de eventos principal
    sys.exit(app.exec())

if __name__ == "__main__":
    main()