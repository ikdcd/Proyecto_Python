from model.Socio import Socio

class SocioDao:
    # Metodos
    def read():
        socios = []
        with open("data/socios.txt", "r", encoding="utf-8") as f:
            for linea in f:
                # aplicamos un strip por cada elemento del .split()
                id, nombre, email, id_libro = [s.strip() for s in linea.split(",")]

                socio = Socio(id, nombre, email, id_libro)
                socios.append(socio)
        return socios

    def write(socios):
        with open("data/socios.txt", "w", encoding="utf-8") as f:
            for socio in socios:
                # escribimos los datos del socio
                print(f"{socio.id}, {socio.nombre}, {socio.email}, {socio.id_libro}", file=f)