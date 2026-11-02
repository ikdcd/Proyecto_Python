class Libro:
    # Constructor
    def __init__(self, id, titulo, autor, anio, categoria, id_socio):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.categoria = categoria
        self.id_socio = id_socio

    # Metodos
    def isDisponible (self):
        return not self.id_socio
