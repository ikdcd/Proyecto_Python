class Socio:
    # Constructor
    def __init__(self, id, nombre, email, id_libro):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.id_libro = id_libro

    # Metodos
    def prestaLibro (self):
        return not self.id_libro
