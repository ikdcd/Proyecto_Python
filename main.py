from errors.LibroYaPrestado import LibroYaPrestado
from errors.EmailYaEnUso import EmailYaEnUso
from errors.SocioNoTieneLibroPrestado import SocioNoTieneLibroPrestado
from errors.SocioTieneLibroPrestado import SocioTieneLibroPrestado
from model.Libro import Libro
from model.Socio import Socio
from util.Biblioteca import Biblioteca

# Inicializa la biblioteca
biblioteca = Biblioteca()

# Metodo main
def main():
    opcion = -1
    while opcion != 0:
        print(f"\n---------------[ MENU ]---------------\n\n"
              +"1. Mostrar todos los libros\n"
              +"2. Mostrar los libros disponibles\n"
              +"3. Buscar un libro\n"
              +"4. Prestar un libro\n"
              +"5. Devolver un libro\n"
              +"6. Mostrar prestas\n"
              +"7. Añadir socio\n"
              +"8. Añadir libro\n"
              +"0. Acabar\n")

        opcion = int(input(">> "))

        match opcion:
            case 1:
                mostrarLibros()
            case 2:
                mostrarLibrosDisponibles()
            case 3:
                busqueda = input("Busqueda: ").lower().strip()
                buscarLibro(busqueda)
            case 4:
                idLibro = input("Codigo de libro: ").strip()
                idSocio = input("Codigo de socio: ").strip()
                prestarLibro(idLibro, idSocio)
            case 5:
                idSocio = input("Codigo de socio: ").strip()
                devolverLibro(idSocio)
            case 6:
                mostrarPrestas()
            case 7:
                print("Introduzca los datos del nuevo socio:")
                nombre = input("Nombre: ").strip()
                email = input("Email: ").strip().lower()
                addSocio(nombre, email)
            case 8:
                print("Introduzca los datos del nuevo libro:")
                titulo = input("Titulo: ").strip()
                autor = input("Autor: ").strip()
                anio = input("Año: ").strip()
                categoria = input("Categoria: ").strip()
                addLibro(titulo, autor, anio, categoria)
            case 0:
                print(f"Saliendo del programa...")
                biblioteca.guardarBiblioteca()
            case _:
                print(f"ERROR: La opcion \"{opcion}\" no existe.")



# Metodos
def printLibros(listaLibros, fila1, fila2, fila3, fila4, fila5, fila6):
    anchoFila1 = 6
    anchoFila2 = 40
    anchoFila3 = 30
    anchoFila4 = 6
    anchoFila5 = 20
    anchoFila6 = 16

    # Imprimimos los encabezados
    if fila1 == True:
        print(f" {"ID":^{anchoFila1}} ", end="")
        if any([fila2, fila3, fila4, fila5, fila6]):
            print("|", end="")
    if fila2 == True:
        print(f" {"TITULO":^{anchoFila2}} ", end="")
        if any([fila3, fila4, fila5, fila6]):
            print("|", end="")
    if fila3 == True:
        print(f" {"AUTOR":^{anchoFila3}} ", end="")
        if any([fila4, fila5, fila6]):
            print("|", end="")
    if fila4 == True:
        print(f" {"AÑO":^{anchoFila4}} ", end="")
        if any([fila5, fila6]):
            print("|", end="")
    if fila5 == True:
        print(f" {"CATEGORIA":^{anchoFila5}} ", end="")
        if fila6 == True:
            print("|", end="")
    if fila6 == True:
        print(f" {"DISPONIBILIDAD":^{anchoFila6}} ", end="")
    print("")

    # Imprimimos el separador del encabezado y las filas
    if fila1 == True:
        print(f"-{"-" * anchoFila1}-", end="")
        if any([fila2, fila3, fila4, fila5, fila6]):
            print("+", end="")
    if fila2 == True:
        print(f"-{"-" * anchoFila2}-", end="")
        if any([fila3, fila4, fila5, fila6]):
            print("+", end="")
    if fila3 == True:
        print(f"-{"-" * anchoFila3}-", end="")
        if any([fila4, fila5, fila6]):
            print("+", end="")
    if fila4 == True:
        print(f"-{"-" * anchoFila4}-", end="")
        if any([fila5, fila6]):
            print("+", end="")
    if fila5 == True:
        print(f"-{"-" * anchoFila5}-", end="")
        if fila6 == True:
            print("+", end="")
    if fila6 == True:
        print(f"-{"-" * anchoFila6}-", end="")
    print("")
    
    # Imprimimos los libros
    for libro in listaLibros:
        if fila1 == True:
            print(f" {libro.id:>{anchoFila1}} ", end="")
            if any([fila2, fila3, fila4, fila5, fila6]):
                print("|", end="")
        if fila2 == True:
            print(f" {libro.titulo:<{anchoFila2}} ", end="")
            if any([fila3, fila4, fila5, fila6]):
                print("|", end="")
        if fila3 == True:
            print(f" {libro.autor:<{anchoFila3}} ", end="")
            if any([fila4, fila5, fila6]):
                print("|", end="")
        if fila4 == True:
            print(f" {libro.anio:^{anchoFila4}} ", end="")
            if any([fila5, fila6]):
                print("|", end="")
        if fila5 == True:
            print(f" {libro.categoria:<{anchoFila5}} ", end="")
            if fila6 == True:
                print("|", end="")
        if fila6 == True:
            if libro.id_socio != "":
                print(f" {"No disponible":^{anchoFila6}} ", end="")
            else:
                print(f" {"Disponible":^{anchoFila6}} ", end="")
        print("")

def mostrarLibros():
    # Obtenemos los libros
    libros = biblioteca.libros

    print(f"\n{"-" * 60}[ LIBROS ]{"-" * 60}\n")

    printLibros(libros, True, True, True, True, True, True)

def mostrarLibrosDisponibles():
    # Obtenemos los libros
    libros = biblioteca.libros

    # Filtramos los libros disponibles
    librosDisponibles = []
    for libro in libros:
        if libro.id_socio == "":
            librosDisponibles.append(libro)

    print(f"\n{"-" * 41}[ LIBROS DISPONIBLES ]{"-" * 41}\n")

    printLibros(librosDisponibles, True, True, True, True, True, False)
    
def buscarLibro(busqueda):
    # Obtenemos los libros
    libros = biblioteca.libros

    # Filtramos el resultado de la busqyeda
    librosEncontrados = []
    for libro in libros:
        if busqueda in libro.titulo.lower():
            librosEncontrados.append(libro)

    if len(librosEncontrados) > 0:
        print(f"\n{"-" * 52}[ RESULTADOS DE BUSQUEDA ]{"-" * 52}\n")

        printLibros(librosEncontrados, True, True, True, True, True, True)
    else:
        print(f"\nNo se ha encontrado ningun libro con el termino \"{busqueda}\".")

def prestarLibro(idLibro, idSocio):
    libro = biblioteca.getLibroById(idLibro)
    socio = biblioteca.getSocioById(idSocio)
    try:
        biblioteca.prestarLibro(libro, socio)
        print(f"ADMITIDO: Socio \"{socio.nombre}\" ha prestado el libro \"{libro.titulo}\".")
    except SocioTieneLibroPrestado as e:
        print("DENEGADO: Este socio ya tiene un libro prestado.")
    except LibroYaPrestado as e:
        print("DENEGADO: Este libro ya esta prestado.")

def devolverLibro(idSocio):
    socio = biblioteca.getSocioById(idSocio)
    try:
        libroDevuelto = biblioteca.devolverLibro(socio)
        print(f"Socio \"{socio.nombre}\" ha devuelto el libro \"{libroDevuelto.titulo}\".")
    except SocioNoTieneLibroPrestado as e:
        print(f"ERROR: Socio \"{socio.nombre}\" no ha prestado ningun libro.")

def mostrarPrestas():
    socios = biblioteca.socios
    libros = biblioteca.libros

    # Obtenemos las prestas
    prestas = []
    for socio in socios:
        if socio.id_libro != "":
            for libro in libros:
                if libro.id == socio.id_libro:
                    prestas.append([socio, libro])

    print(f" {"ID":^{4}} | {"SOCIO":^{20}} | {"ID":^{4}} | {"LIBRO":^{40}} ")
    print(f"-{"-" * 4}-+-{"-" * 20}-+-{"-" * 4}-+-{"-" * 40}-")
    for presta in prestas:
        print(f" {presta[0].id:>{4}} | {presta[0].nombre:<{20}} | {presta[1].id:>{4}} | {presta[1].titulo:<{40}} ")

def addLibro(titulo, autor, anio, categoria):
    biblioteca.addLibro(titulo, autor, anio, categoria)
    print(f"Nuevo libro \"{titulo}\" ha sido añadido.")
    

def addSocio(nombre, email):
    try:
        biblioteca.addSocio(nombre, email)
        print(f"Nuevo socio \"{nombre}\" ha sido añadido.")
    except EmailYaEnUso as e:
        print(f"ERROR: Ya hay un socio creado con el email \"{email}\"")

# Ejecuta el metodo main
main()