## 1. Metáfora General del Sistema
El sistema representa un **juego interactivo** donde el jugador organiza discos de diferentes tamaños entre tres torres. Cada torre es como una pila, y los discos deben moverse respetando las reglas de apilamiento, con el objetivo de trasladar todos los discos de la torre inicial a otra, utilizando una torre auxiliar si es necesario. Es como resolver un rompecabezas físico con pilas de anillos.

---

## 2. Definición Completa del Sistema
El sistema es un juego basado en las reglas clásicas de la Torre de Hanoi, que permite al usuario interactuar con el juego en un entorno digital. Este juego guía al usuario para mover los discos siguiendo las reglas y valida sus movimientos.

**Objetivos principales:**
1. Ofrecer un entorno interactivo para jugar la Torre de Hanoi.
2. Validar que los movimientos del jugador cumplan con las reglas.

---

## 3. Funcionalidades Principales
1. **Representación visual del estado del juego:**
   - Mostrar las tres torres y los discos en su estado actual.
2. **Movimiento interactivo de discos:**
   - Permitir al usuario mover discos entre torres seleccionando origen y destino.
3. **Validación de movimientos:**
   - Evitar movimientos no válidos, como mover un disco desde una torre vacía o colocar un disco más grande sobre uno más pequeño.
---

## 4. Definición de las Clases del Sistema

### **Clases del Sistema**
#### **Clase: Juego**
- **Responsabilidad:** Gestionar el flujo del juego, incluida la inicialización, el estado y las condiciones de victoria.
- **Atributos:**
  - `torres`: Lista de listas que representa las torres y sus discos.
  - `num_discos`: Número total de discos.
- **Métodos:**
  - `inicializar_torres(num_discos)`: Configura las torres iniciales.
  - `mostrar_estado()`: Muestra el estado actual del juego.

#### **Clase: Torre**
- **Responsabilidad:** Representar cada torre del juego como una pila de discos.
- **Atributos:**
  - `discos`: Lista que contiene los discos de la torre.
- **Métodos:**
  - `agregar_disco(disco)`: Añade un disco a la torre.
  - `quitar_disco()`: Quita y devuelve el disco superior de la torre.
  - `validar_movimiento(disco)`: Valida si un disco puede colocarse en la torre.
