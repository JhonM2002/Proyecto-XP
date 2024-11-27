### Pruebas Funcionales para La Torre de Hanoi


### **HU4: Contador de Movimientos**

| **Nombre de la Prueba** | Incremento del Contador con Movimiento Válido |
|-------------------------|-----------------------------------------------|
| **Descripción**         | Verifica que el contador de movimientos se incremente en 1 después de cada movimiento válido y se refleje en pantalla. |
| **Precondiciones**      | - El juego está configurado con 3 discos. <br> - El estado inicial de las torres está cargado: <br> `Torre 1: [3, 2, 1]` <br> `Torre 2: vacía` <br> `Torre 3: vacía` |
| **Datos de Entrada**    | - Torre de origen: `1` <br> - Torre de destino: `3` |
| **Pasos para Ejecutar la Prueba** | 1. Seleccionar la torre `1` como origen y la torre `3` como destino. <br> 2. Ejecutar el movimiento. <br> 3. Observar el contador de movimientos y el estado de las torres. |
| **Resultado Esperado**  | - El estado de las torres se actualiza: <br> `Torre 1: [3, 2]` <br> `Torre 2: vacía` <br> `Torre 3: [1]` <br> - El contador de movimientos muestra `1`. |

---

| **Nombre de la Prueba** | Contador No Incrementa con Movimiento Inválido |
|-------------------------|-----------------------------------------------|
| **Descripción**         | Verifica que el contador de movimientos no se incremente con movimientos no válidos. |
| **Precondiciones**      | - El juego está configurado con 3 discos. <br> - El estado inicial de las torres está cargado. |
| **Datos de Entrada**    | - Torre de origen: `2` (vacía) <br> - Torre de destino: `3` |
| **Pasos para Ejecutar la Prueba** | 1. Seleccionar la torre `2` como origen y la torre `3` como destino. <br> 2. Intentar realizar el movimiento inválido. <br> 3. Observar el contador de movimientos y el estado de las torres. |
| **Resultado Esperado**  | - Mensaje de error: `Movimiento inválido: la torre de origen está vacía.` <br> - El contador de movimientos permanece sin cambios (ej.: `0`). <br> - El estado de las torres no se altera. |

---

| **Nombre de la Prueba** | Contador Acumula Movimientos Válidos |
|-------------------------|-------------------------------------|
| **Descripción**         | Verifica que el contador acumule correctamente los movimientos válidos realizados durante el juego. |
| **Precondiciones**      | - El juego está configurado con 3 discos. |
| **Datos de Entrada**    | - Secuencia de movimientos válidos: <br> 1. De `Torre 1` a `Torre 3`. <br> 2. De `Torre 1` a `Torre 2`. <br> 3. De `Torre 3` a `Torre 2`. |
| **Pasos para Ejecutar la Prueba** | 1. Realizar tres movimientos válidos consecutivos. <br> 2. Observar el contador de movimientos y el estado de las torres después de cada movimiento. |
| **Resultado Esperado**  | - El contador de movimientos muestra `3` después del tercer movimiento válido. <br> - El estado de las torres refleja correctamente los cambios realizados. |

---

### **HU5: Condición de Victoria**

| **Nombre de la Prueba** | Detectar Condición de Victoria |
|-------------------------|--------------------------------|
| **Descripción**         | Verifica que el sistema detecte la condición de victoria cuando todos los discos están apilados en la última torre en el orden correcto. |
| **Precondiciones**      | - El juego está configurado con 3 discos. <br> - El estado actual muestra los discos distribuidos, y el jugador está a un movimiento de resolver el juego. |
| **Datos de Entrada**    | - Torre de origen: `2` <br> - Torre de destino: `3` |
| **Pasos para Ejecutar la Prueba** | 1. Realizar el último movimiento válido para resolver el juego: mover el disco de la torre `2` a la torre `3`. <br> 2. Observar el mensaje mostrado por el sistema y el estado de las torres. |
| **Resultado Esperado**  | - Mensaje de victoria: `¡Felicidades! Has resuelto la Torre de Hanói en 11 movimientos.` <br> - El estado final de las torres es: <br> `Torre 1: vacía` <br> `Torre 2: vacía` <br> `Torre 3: [3, 2, 1]`. <br> - El sistema no permite más movimientos. |

---

| **Nombre de la Prueba** | No Detectar Condición de Victoria Prematuramente |
|-------------------------|-------------------------------------------------|
| **Descripción**         | Verifica que el sistema no detecte victoria hasta que los discos estén correctamente apilados en la última torre. |
| **Precondiciones**      | - El juego está configurado con 3 discos. <br> - Los discos están distribuidos en diferentes torres. |
| **Datos de Entrada**    | - Intentar cualquier movimiento que no complete el juego. |
| **Pasos para Ejecutar la Prueba** | 1. Realizar movimientos válidos, pero sin resolver el rompecabezas. <br> 2. Observar el mensaje mostrado por el sistema y el estado de las torres. |
| **Resultado Esperado**  | - El sistema no muestra un mensaje de victoria. <br> - El juego continúa permitiendo más movimientos. |

---

| **Nombre de la Prueba** | Juego Termina Después de la Victoria |
|-------------------------|-------------------------------------|
| **Descripción**         | Verifica que el juego termine correctamente después de mostrar el mensaje de victoria. |
| **Precondiciones**      | - El juego está configurado con 3 discos. <br> - El jugador resuelve el juego. |
| **Datos de Entrada**    | - Torre de origen: `2` <br> - Torre de destino: `3` |
| **Pasos para Ejecutar la Prueba** | 1. Realizar el movimiento que resuelve el juego. <br> 2. Intentar realizar un nuevo movimiento después de la victoria. |
| **Resultado Esperado**  | - Mensaje de victoria: `¡Felicidades! Has resuelto la Torre de Hanói en 11 movimientos.` <br> - El sistema no permite más movimientos. |

---
