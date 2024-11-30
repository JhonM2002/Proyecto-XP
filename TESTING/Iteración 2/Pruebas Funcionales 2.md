### Pruebas Funcionales para La Torre de Hanoi

### **HU4: Contador de Movimientos**

| **Nombre de la Prueba** | Contador con Movimientos |
|-------------------------|------------------------------------------------------------------|
| **Descripción**         | Verifica que el contador de movimientos se incremente correctamente solo con movimientos válidos y no cambie con movimientos inválidos.|
| **Precondiciones**      | - El juego está configurado con 3 discos. <br> - El estado inicial de las torres está cargado: <br> `Torre 1: [3, 2, 1]` <br> `Torre 2: vacía` <br> `Torre 3: vacía` |
| **Datos de Entrada**    | - Movimiento 1: Torre de origen `1` a Torre de destino `3`. <br> - Movimiento 2: Torre de origen `1` a Torre de destino `2`. <br> - Movimiento 3: Torre de origen `3` a Torre de destino `2`. <br> - Movimiento Inválido: Torre de origen `2` (vacía) a Torre de destino `3`. |
| **Pasos para Ejecutar la Prueba** | 1. Realizar un movimiento válido de `Torre 1` a `Torre 3`. <br> 2. Realizar un movimiento válido de `Torre 1` a `Torre 2`. <br> 3. Realizar un movimiento válido de `Torre 3` a `Torre 2`. <br> 4. Intentar realizar un movimiento inválido de `Torre 2` a `Torre 3` (ya que la Torre 2 está vacía). <br> 5. Intentar realizar un movimiento inválido de `Torre 1` a `Torre 2` (ya que la Torre 1 tiene un dsico mas grande que la Torre 2). |
| **Resultado Esperado**  | - El contador de movimientos debe reflejar un total de `3` después de realizar los tres movimientos válidos. <br> - El estado de las torres debe actualizarse correctamente después de cada movimiento válido: <br> `Torre 1: [3, 2]`, `Torre 2: [1]`, `Torre 3: vacía` después del primer movimiento. <br> `Torre 1: [3]`, `Torre 2: [2, 1]`, `Torre 3: vacía` después del segundo movimiento. <br> `Torre 1: [3]`, `Torre 2: [2, 1]`, `Torre 3: [1]` después del tercer movimiento. <br> - El contador y el estado de las torres no debe cambiar con el movimiento inválido, y el mensaje de error debe ser `Movimiento inválido:`, y el motivo. |
| **Resultado Real**  | ![HU4](Anexos\HU4.JPG)
|**Estado de la prueba:** |Pasó  
|**Comentarios:** |La prueba fue completada con éxito

---

### **HU5: Condición de Victoria**

| **Nombre de la Prueba** | Condición de Victoria |
|-------------------------|--------------------------------------------------------------------|
| **Descripción**         | Verifica que el sistema detecte correctamente la condición de victoria y termine el juego después de que el jugador haya resuelto la Torre de Hanói. |
| **Precondiciones**      | - El juego está configurado con 3 discos. <br> - El estado actual muestra los discos distribuidos en las torres, y el jugador está a un movimiento de resolver el rompecabezas. |
| **Datos de Entrada**    | - Movimiento de Torre de origen `2` a Torre de destino `3` (movimiento final que resuelve el juego).|
| **Pasos para Ejecutar la Prueba** | 1. Realizar el último movimiento válido para resolver el juego: mover el disco de la torre `2` a la torre `3`. <br> 2. Intentar realizar un nuevo movimiento después de la victoria. |
| **Resultado Esperado**  | - El sistema indica que la victoria ha sido alcanzada correctamente. <br> - El estado final de las torres es: <br> `Torre 1: vacía`, `Torre 2: vacía`, `Torre 3: [3, 2, 1]`. <br> - El sistema no permite más movimientos después de la victoria. <br> -  Si el jugador realiza movimientos sin completar el objetivo, el sistema continúa permitiendo más movimientos y no muestra el mensaje de victoria prematuramente. |
| **Resultado Real**  | ![HU5](Anexos\HU5.JPG)
|**Estado de la prueba:** |Pasó  
|**Comentarios:** |La prueba fue completada con éxito

---