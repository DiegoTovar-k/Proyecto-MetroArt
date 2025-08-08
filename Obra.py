class Obra:
    """
    Representa una obra de arte con sus detalles y un objeto Artista asociado.
    """
    def __init__(self,id,titulo,artista,departamento,tipo,fecha_creacion,imagen_url):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.departamento = departamento
        self.tipo = tipo
        self.fecha_creacion = fecha_creacion
        self.imagen_url = imagen_url
        
    def show(self):
        """
        Muestra los detalles completos de la obra y el nombre del artista.
        """
        print(f"""
El id es: {self.id}
El titulo es: {self.titulo}
El artista es: {self.artista.nombre}
El departamento es: {self.departamento}
El tipo es: {self.tipo}
La fecha de creacion es: {self.fecha_creacion}
El url de la imagen es: {self.imagen_url}
""")     