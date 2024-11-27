# Workflow: Desarrollo del juego Torre de Hanoi con XP
## Asignación de Roles 

| Rol        | Persona         |
|------------|-----------------|
| Customer   | José Merchán    |
| Developer  | Jhon Morales    |
| Tracker    | María Mendoza   |
| Tester     | Daniel Oña      |
| Coach      | José Merchán    |
| Manager    | Darío Palma     |

## 1. Inicio del Proyecto
- **Reunión inicial con el cliente:**
  - Entender los requisitos.
  - Aclarar las reglas del juego:
    - Movimientos válidos.
    - Condición de victoria.
  - Identificar las funcionalidades básicas y avanzadas.
- **Creación del Backlog:**
  - Dividir los requisitos en **historias de usuario**.
  - Priorizar las historias junto con el cliente.

---

## 2. Iteraciones del Desarrollo (Ciclo XP)

### 2.1. Planning
1. **Reunión de planificación**:
   - Selección de historias de usuario para la iteración.
   - Por ejemplo:
     - Primera iteración: **HU1 (Representación básica de las torres)**, **HU2 (Movimiento de discos)**, **HU3 (Validación de movimientos)**.
2. **Asignación de tareas**:
   - Asignar historias a pares de programadores.
3. **Definir métricas de éxito**:
   - Ejemplo: Número mínimo de movimientos válidos, cobertura de pruebas unitarias.

---

### 2.2. Designing
1. **Diseñar las estructuras de datos**:
   - Tres listas para representar las torres.
   - Variable para contar los movimientos.
2. **Diagramas de flujo**:
   - Diseñar el flujo de interacción del usuario:
     - Selección de torre de origen y destino.
     - Validaciones.
     - Actualización del estado de las torres.
3. **Planificación de pruebas unitarias**:
   - Identificar casos principales para cada historia de usuario.

---

### 2.3. Coding
1. **Programación en pares**:
   - Implementar las historias seleccionadas en el **Planning**.
   - Trabajar en pequeñas iteraciones incrementales.
2. **Refactorización continua**:
   - Mejorar la calidad del código y eliminar redundancias.
3. **Integración continua**:
   - Realizar commits frecuentes.
   - Ejecutar pruebas automatizadas tras cambios significativos.

---

### 2.4. Testing
1. **Escribir y ejecutar pruebas unitarias**:
   - Validar movimientos válidos e inválidos.
   - Verificar que las torres se actualicen correctamente.
2. **Pruebas manuales**:
   - Simular partidas con diferentes números de discos.
   - Probar flujos completos.
3. **Retroalimentación del cliente**:
   - Mostrar el avance del juego.
   - Incorporar cambios según los comentarios.

---

## 3. Cierre del Proyecto
1. **Entrega del producto final:**
   - Demostrar el juego completo al cliente, incluyendo funcionalidades avanzadas.
   - Documentar el código y las instrucciones de uso.
2. **Revisión del proceso:**
   - Reflexionar sobre qué funcionó bien y qué puede mejorar.
   - Identificar aprendizajes clave.

---

## Diagrama del Workflow

```plaintext
Inicio del proyecto
      ↓
Planning (Historias de Usuario, Priorización)
      ↓
Designing (Estructura de datos, Diagramas, Planificación de pruebas)
      ↓
Coding (Programación en pares, Refactorización, Integración continua)
      ↓
Testing (Pruebas unitarias, Pruebas manuales, Retroalimentación)
      ↓
¿Producto Completo?
    ↙       ↘
  No          Sí
  (Iterar)    (Entrega Final)
