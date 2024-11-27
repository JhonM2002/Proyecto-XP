# Proyecto: Juego Torre de Hanoi
#  - Grupo 4

## Equipo
- JHON MORALES
- MARÍA MENDOZA
- DANIEL OÑA
- DARIO PALMA
- JOSÉ MERCHAN

## 1. Metáfora General del Sistema
El sistema representa un **juego interactivo** donde el jugador organiza discos de diferentes tamaños entre tres torres. Cada torre es como una pila, y los discos deben moverse respetando las reglas de apilamiento, con el objetivo de trasladar todos los discos de la torre inicial a otra, utilizando una torre auxiliar si es necesario. Es como resolver un rompecabezas físico con pilas de anillos.

---

## 2. Definición Completa del Sistema
El sistema es un juego basado en las reglas clásicas de la Torre de Hanoi, que permite al usuario interactuar con el juego en un entorno digital. Este juego guía al usuario para mover los discos siguiendo las reglas, valida sus movimientos, y contabiliza el número de movimientos realizados hasta completar el objetivo.

**Objetivos principales:**
1. Ofrecer un entorno interactivo para jugar la Torre de Hanoi.
2. Validar que los movimientos del jugador cumplan con las reglas.
3. Contar y mostrar los movimientos realizados.
4. Detectar y notificar al usuario cuando gane el juego.

---

## 3. Funcionalidades Principales
1. **Representación visual del estado del juego:**
   - Mostrar las tres torres y los discos en su estado actual.
2. **Movimiento interactivo de discos:**
   - Permitir al usuario mover discos entre torres seleccionando origen y destino.
3. **Validación de movimientos:**
   - Evitar movimientos no válidos, como mover un disco desde una torre vacía o colocar un disco más grande sobre uno más pequeño.
4. **Contador de movimientos:**
   - Llevar un registro del número de movimientos realizados.
5. **Condición de victoria:**
   - Detectar y notificar al usuario cuando todos los discos estén apilados en la torre destino.

---

## 4. Definición de las Clases del Sistema

### **Clases del Sistema**
#### **Clase: Juego**
- **Responsabilidad:** Gestionar el flujo del juego, incluida la inicialización, el estado y las condiciones de victoria.
- **Atributos:**
  - `torres`: Lista de listas que representa las torres y sus discos.
  - `movimientos`: Contador de movimientos realizados.
  - `num_discos`: Número total de discos.
- **Métodos:**
  - `inicializar_torres(num_discos)`: Configura las torres iniciales.
  - `verificar_victoria()`: Comprueba si el juego se ha completado.
  - `mostrar_estado()`: Muestra el estado actual del juego.

#### **Clase: Torre**
- **Responsabilidad:** Representar cada torre del juego como una pila de discos.
- **Atributos:**
  - `discos`: Lista que contiene los discos de la torre.
- **Métodos:**
  - `agregar_disco(disco)`: Añade un disco a la torre.
  - `quitar_disco()`: Quita y devuelve el disco superior de la torre.
  - `validar_movimiento(disco)`: Valida si un disco puede colocarse en la torre.

#### **Clase: Disco**
- **Responsabilidad:** Representar los discos del juego.
- **Atributos:**
  - `tamaño`: Tamaño del disco (número entero).
