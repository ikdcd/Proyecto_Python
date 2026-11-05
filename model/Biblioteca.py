from model.Libro import Libro
from model.Socio import Socio

class Biblioteca:
    # Constructor
    def __init__(self):
        self.libros = []
        self.socios = []

        # Carga los datos guardados
        with open("data/libros.txt", "r", encoding="utf-8") as f:
            for linea in f:
                # aplicamos un strip por cada elemento del .split()
                id, titulo, autor, anio, categoria, id_socio = [s.strip() for s in linea.split(",")]

                libro = Libro(id, titulo, autor, anio, categoria, id_socio)
                self.libros.append(libro)
        
        with open("data/socios.txt", "r", encoding="utf-8") as f:
            for linea in f:
                # aplicamos un strip por cada elemento del .split()
                id, nombre, email, id_libro = [s.strip() for s in linea.split(",")]

                socio = Socio(id, nombre, email, id_libro)
                self.socios.append(socio)
        
    # Metodos
    def getLibroById(self, idLibro):
        for libro in self.libros:
            if libro.id == idLibro:
                return libro
        return False
    
    def updateLibro(self, newLibro):
        for libro in self.libros:
            if libro.id == newLibro.id:
                libro = newLibro

    def getSocioById(self, idSocio):
            for socio in self.socios:
                if socio.id == idSocio:
                    return socio
            return False
    
    def updateSocio(self, newSocio):
        for socio in self.socios:
            if socio.id == newSocio.id:
                socio = newSocio
    
    def getPrestas(self):
        prestas = []
        for socio in self.socios:
            if socio.id_libro != "":
                for libro in self.libros:
                    if libro.id == socio.id_libro:
                        prestas.append([socio, libro])
        return prestas
    
    def guardarBiblioteca(self):
        with open("data/libros.txt", "w", encoding="utf-8") as f:
            for libro in self.libros:
                # escribimos los datos del libro
                print(f"{libro.id}, {libro.titulo}, {libro.autor}, {libro.anio}, {libro.categoria}, {libro.id_socio}", file=f)

        with open("data/socios.txt", "w", encoding="utf-8") as f:
            for socio in self.socios:
                # escribimos los datos del socio
                print(f"{socio.id}, {socio.nombre}, {socio.email}, {socio.id_libro}", file=f)
    