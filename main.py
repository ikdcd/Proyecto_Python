from model.Libro import Libro
from model.Socio import Socio

# Metodo main
def main():
    # Obtenemos los libros y socios
    libros = getLibros()
    socios = getSocios()



# Metodos
def getLibros():
    libros = []
    with open("data/libros.txt", "r", encoding="utf-8") as f:
        for linea in f:
            # aplicamos un strip por cada elemento del .split()
            id, titulo, autor, anio, categoria, id_socio = [s.strip() for s in linea.split(",")]

            libro = Libro(id, titulo, autor, anio, categoria, id_socio)
            libros.append(libro)
    return libros

def getSocios():
    socios = []
    with open("data/socios.txt", "r", encoding="utf-8") as f:
        for linea in f:
            # aplicamos un strip por cada elemento del .split()
            id, nombre, email, id_libro = [s.strip() for s in linea.split(",")]

            socio = Socio(id, nombre, email, id_libro)
            socios.append(socio)
    return socios



# Ejecuta el metodo main
main()