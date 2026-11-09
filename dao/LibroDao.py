from model.Libro import Libro

class LibroDao:
    # Metodos
    def read():
        libros = []
        with open("data/libros.txt", "r", encoding="utf-8") as f:
            for linea in f:
                # aplicamos un strip por cada elemento del .split()
                id, titulo, autor, anio, categoria, id_socio = [s.strip() for s in linea.split(",")]

                libro = Libro(id, titulo, autor, anio, categoria, id_socio)
                libros.append(libro)
        return libros

    def write(libros):
        with open("data/libros.txt", "w", encoding="utf-8") as f:
            for libro in libros:
                # escribimos los datos del libro
                print(f"{libro.id}, {libro.titulo}, {libro.autor}, {libro.anio}, {libro.categoria}, {libro.id_socio}", file=f)