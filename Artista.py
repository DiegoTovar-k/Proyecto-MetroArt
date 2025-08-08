class Artista:
    def __init__(self,nombre,nacionalidad,fecha_nacimiento,fecha_muerte):
        self.nombre = nombre
        self.nacionalidad = nacionalidad 
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_muerte = fecha_muerte

    def show(self):
        print(f'''
El nombre completo del artista es: {self.nombre}
La nacionalidad del artista es: {self.nacionalidad}
La fecha de nacimiento es: {self.fecha_nacimiento}
La fecha de muerte es: {self.fecha_muerte}
''')