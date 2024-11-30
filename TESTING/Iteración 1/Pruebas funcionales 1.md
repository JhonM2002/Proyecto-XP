# Pruebas Funcionales de la Iteración 1

## **HU1: Representación básica del juego**

**Nombre de la prueba:** Representación básica del juego  
**Descripción:** Validar que las tres torres y los discos se muestren correctamente al inicio del juego.  
**Precondiciones:** El juego ha sido iniciado con 3 discos en la Torre 1 y no se ha realizado ningún movimiento.  
**Datos de entrada:** Número de discos configurado en 3  

**Pasos:**
1. Iniciar el juego con 3 discos en la primera torre.
2. Verificar que se muestren tres torres.
3. Verificar que los discos estén apilados correctamente en la primera torre.
4. Asegurarse de que no haya discos en las otras dos torres.

**Resultado esperado:**  
- Tres torres visibles.  
- Discos apilados correctamente en la primera torre (más grande abajo).  
- Las otras dos torres deben estar vacías.

**Resultado real:**

![HU1](Anexos\HU1.JPG)

**Estado de la prueba:** Pasó  
**Comentarios:** La prueba fue completada con éxito

---

## **HU2: Movimiento de discos**

**Nombre de la prueba:** Movimiento de discos  
**Descripción:** Verificar que el jugador pueda mover un disco de una torre a otra.  
**Precondiciones:** El juego ha sido iniciado con 3 discos en la Torre 1 y no se ha realizado ningún movimiento.  
**Datos de entrada:** Mover un disco de la Torre 1 a la Torre 2.  

**Pasos:**
1. Iniciar el juego con 3 discos en la primera torre.
2. El jugador selecciona un disco en la Torre 1.
3. El jugador selecciona la Torre 2 como destino.
4. Verificar la actualización de las torres después del movimiento.

**Resultado esperado:**  
- Disco más pequeño (1) movido a la Torre 2.  
- Estado actualizado: Torre 1: [3, 2], Torre 2: [1], Torre 3: [].

**Resultado real:**

![HU2](Anexos\HU2.JPG)

**Estado de la prueba:** Pasó  
**Comentarios:** La prueba fue completada con éxito

---

## **HU3: Validación de movimientos**

**Nombre de la prueba:** Validación de movimientos  
**Descripción:** Verificar que el sistema valide que un disco más grande no se coloque sobre un disco más pequeño.  
**Precondiciones:** El juego ha sido iniciado con 3 discos en la Torre 1 y no se ha realizado ningún movimiento.  

**Pasos:**
1. Iniciar el juego con tres discos apilados en la Torre 1.
2. Mover el disco pequeño (1) a la Torre 2.
3. Intentar mover el disco más grande (2) de la Torre 1 a la Torre 2.

**Resultado esperado:**  
- Mensaje de error indicando que el movimiento no es válido.  
- El estado de las torres debe mantenerse igual.

**Resultado real:**

![HU3](Anexos\HU3.JPG)

**Estado de la prueba:** Pasó  
**Comentarios:** La prueba fue completada con éxito