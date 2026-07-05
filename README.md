# Inteligencia Artificial en Automática/Automatización
## Tarea #2: Juego de Damas con IA

**Institución:** Universidad del Bío-Bío
**Profesor:** Christopher Flores
**Integrantes:** Javier Ferreiro, Cristian Figueroa

---

### Descripción del Proyecto
Este repositorio contiene la implementación de una aplicación computacional que permite jugar damas mediante una interfaz gráfica. El proyecto aplica técnicas de Inteligencia Artificial para desarrollar oponentes automáticos y permite evaluar y comparar el desempeño de distintas estrategias de juego.

### Modos de Juego
La aplicación cuenta con tres modalidades principales de juego:
* **Modo 2 Usuarios:** Permite a dos jugadores humanos enfrentarse alternando turnos en la misma interfaz gráfica.
* **Oponente IA (Búsqueda Clásica):** Implementa un agente inteligente basado en algoritmos de búsqueda clásica (ej. Minimax con poda Alfa-Beta), evaluando los estados del tablero mediante heurísticas.
* **Oponente Machine Learning:** Implementa un modelo de aprendizaje automático diseñado para seleccionar movimientos estratégicos y desafiar al jugador humano.

### Arquitectura de Software
El proyecto ha sido desarrollado siguiendo estrictamente el patrón arquitectónico **Modelo-Vista-Controlador (MVC)**, garantizando un código modular, escalable y ordenado.
* **Modelo:** Contiene la lógica matemática del tablero, las reglas de movimiento, capturas obligatorias y coronación.
* **Vista:** Interfaz gráfica desarrollada en PySide6.
* **Controlador:** Orquesta la comunicación entre la lógica del juego y las acciones del usuario.

### Instrucciones de Instalación y Ejecución
*(Nota: Esta sección se completará a medida que se definan las dependencias exactas del proyecto, como PySide6, Numpy, PyTorch/TensorFlow, etc.)*

1. Clonar el repositorio.
2. Crear e activar el entorno virtual.
3. Instalar dependencias: `pip install -r requirements.txt`
4. Ejecutar el juego: `python main.py`