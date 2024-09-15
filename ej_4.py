# i. ¿Los identificadores mozo1 y mozo2 hacen referencia al mismo objeto?
# No, aunque los identificadores mozo1 y mozo2 son instancias de la clase Mozo con el mismo nombre ("Alfredo"), apuntan a dos objetos diferentes en memoria. En Python, cada vez que se crea un objeto con Mozo("Alfredo"), se crea una nueva instancia, lo que significa que mozo1 y mozo2 no son el mismo objeto.

# ii. ¿Son objetos equivalentes?
# No necesariamente. Aunque ambos objetos tienen el mismo valor para su atributo nombre, siguen siendo dos instancias diferentes de la clase Mozo. La equivalencia entre objetos podría definirse si se sobrecarga el método especial __eq__() para comparar objetos por sus atributos. Dos objetos son equivalentes cuando sus atributos tienen los mismos valores, pero esto no significa que sean el mismo objeto en memoria.

# iii. ¿Los objetos ligados a mozo1 y mozo2 comparten la misma posición de memoria?
# No, cada instancia de la clase Mozo tiene su propia posición de memoria. Incluso si sus atributos tienen los mismos valores, los objetos son distintos y se almacenan en diferentes posiciones de memoria.