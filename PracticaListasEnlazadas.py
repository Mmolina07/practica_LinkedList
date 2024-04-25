class Node:
  __slots__ = 'value', 'next'
  def __init__(self, value):
    self.value = value
    self.next = None

  def __str__(self):
    return str(self.value)

class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def __iter__(self):
      NodoActual = self.head 
      while NodoActual is not None:
         yield NodoActual
         NodoActual = NodoActual.next

  def __str__(self):
    result = [str(x.value) for x in self]
    return ' '.join(result)

  def append(self, value):
    new_node = Node(value)
    if self.head == None:
      self.head = new_node
      self.tail = new_node

    else:
      new_node.next = None
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1

  def pop_first(self):
    if self.length == 0:
        return None

    popped_node = self.head
    if self.length == 1:
        self.head = self.tail = None

    else:
        self.head = self.head.next
        popped_node.next = None
    self.length -= 1
    return popped_node

  def pop(self):
    if self.length == 0:
        return None

    popped_node = self.tail 
    if self.length == 1:
        self.head = self.tail = None

    else:
        prevtail_node = self.get(self.length - 2)
        self.tail = prevtail_node

    self.length -= 1
    return popped_node

  def remove(self, index):
    if index < -1 and index >= self.length:
        return None

    if index == 0:
        return self.pop_first()

    if index == -1 or index == self.length - 1:
        return self.pop()

    prev_node = self.get(index - 1)
    popped_node = prev_node.next
    prev_node.next = popped_node.next
    popped_node.next = None
    self.length -= 1
    return popped_node

class Libro:
    def __init__(self, numero_libro: int , genero: str, autor: str, titulo: str, year_publicacion: int, tarifa_diaria_alquiler: float, disponible: bool = True):
        self.numero_libro = numero_libro
        self.genero = genero
        self.autor = autor
        self.titulo = titulo
        self.year_publicacion = year_publicacion
        self.tarifa_diaria_alquiler = tarifa_diaria_alquiler
        self.disponible = disponible
        self.alquilado_por = None

    def __repr__(self) -> str:
        return f"[{self.numero_libro}] Genero {self.genero} {self.titulo} por {self.autor} publicado en {self.year_publicacion}, precio: {self.tarifa_diaria_alquiler}, disponible: {'Si' if self.disponible else 'No'} "

class Biblioteca:

    def __init__(self) -> None:
        self.head = None
        self.libros = LinkedList()

    """Agregar un libro, debe ser posible agregar nuevos libros, se debe permitir 
    registrar un nuevo libro con todos sus atributos."""

    def agregar_libro(self, libro: Libro):
        if self.libros.head is None:
            self.libros.append(libro)
        else:
            current = self.libros.head
            prev = None
            while current is not None:
                if current.value.genero == libro.genero:
                    if prev is None:
                        new_node = Node(libro)
                        new_node.next = current
                        self.libros.head = new_node
                    else:
                        new_node = Node(libro)
                        new_node.next = current
                        prev.next = new_node
                    return
                prev = current
                current = current.next
            self.libros.append(libro)

    """Eliminar un libro, debe permitir la opción de eliminar libros."""

    def eliminar_libro(self, numero_libro: int):
        self.libros.remove(numero_libro-1)

    """Buscar todos los libros por género, debe retornar cuantos libros se tienen, la 
    información de cada uno y adicionalmente si está o no disponible para el alquiler"""

    def buscar_por_genero(self, genero: str):
        contador = 0
        for libro in self.libros:
            if libro.value.genero == genero:
                print(libro)
                contador += 1
        print(f"Se encontraron {contador} libros del género '{genero}' ")

    """Buscar un libro por título, debe retornar si se tiene el libro en la 
    biblioteca y adicionalmente si está o no disponible para el alquiler"""

    def buscar_por_titulo(self, titulo: str):
        contador = 0
        for libro in self.libros:
            if libro.value.titulo.lower() == titulo.lower():
                print(f"El libro '{titulo}' esta en la biblioteca y su estado es {'disponible' if libro.value.disponible else 'No disponible'} para alquiler. ")
                contador += 1
                return
        print(f"El libro '{titulo}' no se encuentra en la biblioteca")

    """Buscar un libro por autor, debe retornar si se tiene el libro en la 
    biblioteca y adicionalmente si está o no disponible para el alquiler"""

    def buscar_por_autor(self, autor: str):
        contador = 0
        for libro in self.libros:
            if libro.value.autor.lower() == autor.lower():
                print(libro)
                contador += 1
        print(f"Se encontraron {contador} libros del autor '{autor}'")

    """Buscar un libro por año de publicación, debe retornar si se tiene el libro 
    en la biblioteca y adicionalmente si está o no disponible para el alquiler"""

    def buscar_por_year(self, year_publicacion: int):
        contador = 0
        for libro in self.libros:
            if libro.value.year_publicacion == year_publicacion:
                print(libro)
                contador += 1
        print(f"Se encontraron {contador} libros publicados en el año '{year_publicacion}' ")

    """Listar todos los libros disponibles para alquilar, los usuarios deben poder ver la lista 
    de libros disponibles para alquilar, mostrando todos los atributos de cada libro."""

    def listar_libros_disponibles(self):
        print("Libros disponibles para alquilar:")
        for nodo in self.libros:
            if nodo.value.disponible:
                print(f"Título: {nodo.value.titulo}")
                print(f"Autor: {nodo.value.autor}")
                print(f"Género: {nodo.value.genero}")
                print(f"Año de publicación: {nodo.value.year_publicacion}")
                print(f"Estado: {'Disponible' if nodo.value.disponible else 'No disponible'}")
                print("-" * 30)

    """Listar todos los libros que se encuentran alquilados, los usuarios deben poder ver la 
    lista de libros NO disponibles para alquilar, mostrando todos los atributos de cada libro."""

    def listar_libros_alquilados(self):
        print("Libros alquilados:")
        for nodo in self.libros:
            if not nodo.value.disponible:
                print(f"Título: {nodo.value.titulo}")
                print(f"Autor: {nodo.value.autor}")
                print(f"Género: {nodo.value.genero}")
                print(f"Año de publicación: {nodo.value.year_publicacion}")
                print(f"Estado: {'Disponible' if nodo.value.disponible else 'No disponible'}")
                print("-" * 30)

    """Listar todos los libros disponibles para alquilar x Género, los usuarios deben poder 
    ver la lista de libros disponibles para alquilar, mostrando todos los atributos de cada libro."""

    def listar_libros_disponibles_por_genero(self, genero: str):
        print(f"Libros disponibles para alquilar del género '{genero}':")
        contador = 0
        for nodo in self.libros:
            if nodo.value.disponible and nodo.value.genero.lower() == genero.lower():
                print(f"Título: {nodo.value.titulo}")
                print(f"Autor: {nodo.value.autor}")
                print(f"Año de publicación: {nodo.value.year_publicacion}")
                print(f"Estado: {'Disponible' if nodo.value.disponible else 'No disponible'}")
                print("-" * 30)
                contador += 1
        if contador == 0:
            print(f"No se encontraron libros del género '{genero}' en la biblioteca.")

    """Listar todos los libros que se encuentran alquilados x Género, los usuarios deben poder ver la 
    lista de libros NO disponibles para alquilar, mostrando todos los atributos de cada libro."""

    def listar_libros_alquilados_por_genero(self, genero: str):
        print(f"Libros alquilados del género '{genero}':")
        contador = 0
        for nodo in self.libros:
            if not nodo.value.disponible and nodo.value.genero.lower() == genero.lower():
                print(f"Título: {nodo.value.titulo}")
                print(f"Autor: {nodo.value.autor}")
                print(f"Año de publicación: {nodo.value.year_publicacion}")
                print(f"Estado: {'No disponible'}")
                print("-" * 30)
                contador += 1
        if contador == 0:
            print(f"No se encontraron libros alquilados del género '{genero}' en la biblioteca.")

    """Alquilar un libro x Género, los usuarios deben poder alquilar un libro específico de la lista enlazada."""

    def alquilar_por_genero(self, usuario: str,  genero: str):
        for libro in self.libros:
            if libro.value.genero.lower() == genero.lower() and libro.value.disponible:
                libro.value.disponible = False
                libro.value.alquilado_por = usuario
                print(f"El libro '{libro.value.titulo}' del género '{genero}' ha sido alquilado.")
                return
        print(f"No hay libros disponibles del género '{genero}' para alquilar.")

    """Alquilar un libro, los usuarios deben poder alquilar un libro específico de la lista enlazada."""

    def alquilar_libro(self, usuario: str, titulo: str):
        for libro in self.libros:
            if libro.value.titulo.lower() == titulo.lower() and libro.value.disponible:
                libro.value.disponible = False
                libro.value.alquilado_por = usuario
                print(f"El libro '{titulo}' ha sido alquilado.")
                return
        print(f"No hay libros disponibles con el título '{titulo}' para alquilar.")

    """Devolver un libro, Los usuarios también deben poder registrar la devolución de un libro alquilado."""

    def devolver_libro(self, titulo: str):
        for nodo in self.libros:
            if nodo.value.titulo.lower() == titulo.lower():
                if nodo.value.disponible:
                    print(f"El libro '{titulo}' no está alquilado actualmente.")
                else:
                    nodo.value.disponible = True
                    print(f"El libro '{titulo}' ha sido devuelto correctamente.")
                return
        print(f"El libro '{titulo}' no se encuentra en la biblioteca")

    def intercambiar_libros_deteriorados(self, nodo_nuevo:Libro):
        print(self.mostrar_libros())
        nodo_deteriorado = int(input("Ingrese el numero del libro que esta deteriorado: "))
        current = self.libros.head
        prev = None

        while current:
            if current.value.numero_libro == nodo_deteriorado:
                nodo_nuevo = Node(nodo_nuevo)
                if prev:
                    prev.next = nodo_nuevo
                else:
                    self.libros.head = nodo_nuevo

                nodo_nuevo.next = current.next
                print("Intercambio realizado con éxito.")
                return True

            prev = current
            current = current.next

        print("No se encontró el nodo deteriorado en la lista.")
        return False

    """Se debe otorgar un dcto del 10% x libro, si el mismo usuario alquila 2 o más libros. """
    def calcular_tarifa(self, usuario: str):
        libros_usuario = [libro for libro in self.libros if libro.value.alquilado_por == usuario]
        total = sum([libro.value.tarifa_diaria_alquiler for libro in libros_usuario])
        print(f"Total sin descuento para {usuario} es: {total}")
        if len(libros_usuario) >= 2:
            total *= 0.9
            print(f"Total con descuento para {usuario} es: {total}")
        return total
    
    def ingreso_total(self):
        usuarios = set([libro.value.alquilado_por for libro in self.libros if not libro.value.disponible])
        return f"El dinero total obtenido por los alquileres es: {sum([self.calcular_tarifa(usuario) for usuario in usuarios])}"

    """Se debe retornar el ingreso total obtenido por alquileres de libros hasta el momento."""

    def mostrar_libros(self):
       for libro in biblioteca.libros:
          print(libro)

if __name__ == "__main__":
    
    biblioteca = Biblioteca()

    nuevo_libro1 = Libro(1,"Ficción", "J.K. Rowling","Harry Potter y la piedra filosofal", 1997, 15000)
    nuevo_libro2 = Libro(2,"Ficción", "Isaac Asimov", "Fundación", 1951, 5000)
    nuevo_libro3 = Libro(3,"Ficción", "Angie", "Titanic", 2024, 12000)
    nuevo_libro4 = Libro(4,"Misterio", "Dan Brown", "El Código da Vinci", 2003, 15000)
    nuevo_libro5 = Libro(5,"Fantasía", "J.R.R. Tolkien", "El señor de los anillos", 1954, 12000)
    nuevo_libro6 = Libro(6,"Realismo mágico", "Gabriel Garcia Marquez", "Cien años de soledad", 1967, 15000)

    biblioteca.agregar_libro(nuevo_libro1)
    biblioteca.agregar_libro(nuevo_libro2)
    biblioteca.agregar_libro(nuevo_libro3)
    biblioteca.agregar_libro(nuevo_libro4)
    biblioteca.agregar_libro(nuevo_libro5)
    biblioteca.mostrar_libros()
    biblioteca.eliminar_libro(1)
    biblioteca.mostrar_libros()

    biblioteca.buscar_por_genero("Ficción")

    biblioteca.mostrar_libros()

    biblioteca.buscar_por_titulo("El señor de los anillos")

    biblioteca.buscar_por_autor("J.R.R. Tolkien")

    biblioteca.buscar_por_year(2003)

    biblioteca.listar_libros_disponibles()

    biblioteca.listar_libros_alquilados()

    biblioteca.listar_libros_disponibles_por_genero("Ficción")

    biblioteca.listar_libros_alquilados_por_genero("Ficción")

    biblioteca.alquilar_por_genero ("Angie", "Fantasía")

    biblioteca.devolver_libro("El señor de los anillos")

    biblioteca.intercambiar_libros_deteriorados(nuevo_libro6)

    biblioteca.calcular_tarifa("Mateo")

    biblioteca.ingreso_total()

    nuevo_libro7 = Libro(7,"Misterio", "Dan Brown", "El Código da Vinci", 2003, 15000)

    biblioteca.listar_libros_disponibles()