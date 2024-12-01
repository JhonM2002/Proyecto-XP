## **Iteración 2: Funcionalidades Avanzadas**

### Clase: Juego
| **NOMBRE DE LA CLASE** | Juego                                  |
|-------------------------|----------------------------------------|
| **SUPERCLASES**        | Ninguna                               |
| **SUBCLASES**          | Ninguna                               |
| **RESPONSABILIDADES**  | - Incrementar el contador de movimientos. <br> - Detectar si el jugador ha ganado. <br> - Mostrar mensajes de retroalimentación al usuario. |
| **COLABORADORES**      | Torre                        |
| **PENSAMIENTO EN OBJETOS** | Extiende la lógica del juego básico con funcionalidad avanzada de monitoreo y retroalimentación. |
| **PROPIEDAD**          | - Torres. <br> - Número de movimientos. <br> - Mensajes para el usuario. |

---

### Clase: Torre
| **NOMBRE DE LA CLASE** | Torre                                  |
|-------------------------|----------------------------------------|
| **SUPERCLASES**        | Ninguna                               |
| **SUBCLASES**          | Ninguna                               |
| **RESPONSABILIDADES**  | - Gestionar discos de forma avanzada. <br> - Detectar intentos de movimientos inválidos. |
| **COLABORADORES**      | Juego                                 |
| **PENSAMIENTO EN OBJETOS** | Actúa como intermediario en la validación de reglas avanzadas. |
| **PROPIEDAD**          | - Lista de discos. |

---
