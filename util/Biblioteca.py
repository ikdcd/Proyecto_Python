from errors.LibroYaPrestado import LibroYaPrestado
from errors.EmailYaEnUso import EmailYaEnUso
from errors.SocioNoTieneLibroPrestado import SocioNoTieneLibroPrestado
from errors.SocioTieneLibroPrestado import SocioTieneLibroPrestado
from model.Libro import Libro
from model.Socio import Socio
from dao.LibroDao import LibroDao
from dao.SocioDao import SocioDao
from util.Logger import Logger

class Biblioteca:
    # Constructor
    def __init__(self):
        # Carga los datos guardados
        self.libros = LibroDao.read()
        self.socios = SocioDao.read()

        Logger.newLogHeader("BIBLIOTECA CARGADA")

    # Metodos
    def getLibroById(self, idLibro):
        for libro in self.libros:
            if libro.id == idLibro:
                return libro
    
    def prestarLibro(self, libro: Libro, socio: Socio):
        if socio.prestaLibro() == False:
            if libro.isDisponible() == True:
                libro.id_socio = socio.id
                socio.id_libro = libro.id
                self.updateLibro(libro)
                self.updateSocio(socio)
                Logger.newLog("LIBRO PRESTADO", f"{socio.nombre} ({socio.id}) <-- {libro.titulo} ({libro.id})")
            else:
                raise LibroYaPrestado()
        else: 
            raise SocioTieneLibroPrestado()
        
    def devolverLibro(self, socio: Socio):
        if socio.prestaLibro() == True:
            libro = self.getLibroById(socio.id_libro)

            libro.id_socio = ""
            socio.id_libro = ""
            self.updateLibro(libro)
            self.updateSocio(socio)

            Logger.newLog("LIBRO DEVUELTO", f"{socio.nombre} ({socio.id}) --> {libro.titulo} ({libro.id})")
            return libro
        else:
            raise SocioNoTieneLibroPrestado()
            
    def updateLibro(self, newLibro):
        for libro in self.libros:
            if libro.id == newLibro.id:
                libro = newLibro
        return True

    def getSocioById(self, idSocio):
        for socio in self.socios:
            if socio.id == idSocio:
                return socio
    
    def updateSocio(self, newSocio):
        for socio in self.socios:
            if socio.id == newSocio.id:
                socio = newSocio
        return True
    
    def getPrestas(self):
        prestas = []
        for socio in self.socios:
            if socio.id_libro != "":
                for libro in self.libros:
                    if libro.id == socio.id_libro:
                        prestas.append([socio, libro])
        return prestas
    
    def addLibro(self, titulo, autor, anio, categoria):
        libros = self.libros

        # Obtenemos el ultimo libro y le asignamos al nuevo libro su id mas 1
        nuevoId = int(libros[-1].id) + 1
        libro = Libro(nuevoId, titulo, autor, anio, categoria, "")

        self.libros.append(libro)
        Logger.newLog("LIBRO AÑADIDO", f"Libro({libro.id}, {libro.titulo}, {libro.autor}, {libro.anio}, {libro.categoria}, null).")

    def addSocio(self, nombre, email):
        socios = self.socios

        # Comprobamos que no exista un socio con el mismo email
        i = 0
        while i < len(socios):
            if socios[i].email.lower() == str(email).lower():
                raise EmailYaEnUso
            i += 1

        # Obtenemos el ultimo socio y le asignamos al nuevo libro su id mas 1
        nuevoId = str(int(socios[-1].id) + 1)
        socio = Socio(nuevoId, nombre, email, "")

        self.socios.append(socio)
        Logger.newLog("SOCIO AÑADIDO", f"Socio({socio.id}, {socio.nombre}, {socio.email}, null).")

    def guardarBiblioteca(self):
        LibroDao.write(self.libros)
        SocioDao.write(self.socios)
        Logger.newLog("CAMBIOS GUARDADOS", f"Se ha guardado los cambios realizados.")