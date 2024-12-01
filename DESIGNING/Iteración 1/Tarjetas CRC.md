 Tarjetas CRC: Sistema Torre de Hanoi

---

## **Iteración 1: Funcionalidades Básicas**

### Clase: Juego
| **NOMBRE DE LA CLASE** | Juego                                  |
|-------------------------|----------------------------------------|
| **SUPERCLASES**        | Ninguna                               |
| **SUBCLASES**          | Ninguna                               |
| **RESPONSABILIDADES**  | - Inicializar las torres del juego. <br> - Representar visualmente el estado del juego. <br> - Gestionar el flujo principal del juego. |
| **COLABORADORES**      | Torre                        |
| **PENSAMIENTO EN OBJETOS** | Controla la lógica principal del juego y valida las reglas. |
| **PROPIEDAD**          | - Torres (lista de objetos Torre). <br> - Número de discos. <br> - Contador de movimientos. |

---

### Clase: Torre
| **NOMBRE DE LA CLASE** | Torre                                  |
|-------------------------|----------------------------------------|
| **SUPERCLASES**        | Ninguna                               |
| **SUBCLASES**          | Ninguna                               |
| **RESPONSABILIDADES**  | - Almacenar discos en forma de pila. <br> - Validar si un disco puede ser colocado en la torre. <br> - Retirar discos de la torre. |
| **COLABORADORES**      | Juego                               |
| **PENSAMIENTO EN OBJETOS** | Actúa como una estructura de pila para los discos y controla la lógica de apilamiento. |
| **PROPIEDAD**          | - Lista de discos. |

---