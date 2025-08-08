from Artista import Artista
from Obra import Obra
import requests

class Museo:
    """
    Aquí se encuentra el catálogo principal con las diferentes opciones de encontrar las obras que el 
    usuario tiene a su disposición.
    """
    def start(self):
        """
        Aquí se encuentra el menú con las diferentes opciones que podrá escoger el usuario.    
        """
        while True:
            menu = input (""" Bienvenido a Metro Art. Seleccione la opción de su preferencia:
1- Ver lista de obras por departamento
2- Ver lista de obras por nacionalidad del autor
3- Ver lista de obras por nombre del autor
4- Mostrar detalles de la obra
5- Salir
""")
            if menu == "1":
                departamentos = self.listar_departamentos()
                if departamentos:
                    try:
                        seleccion_id = int(input("\n Introduce el ID del departamento que desea conocer:"))
                        object_ids = self.buscar_obras_departamento(seleccion_id)
                        if object_ids:
                            self.mostrar_detalles(object_ids)
            
                    except ValueError:
                        print("Entrada no valida. Por favor, introduce un numero:")
                        
            elif menu == "2":
                nacionalidades = self.leer_nacionalidades()
                if nacionalidades:
                    try:
                        seleccion_nacionalidad = input("\nIntroduce la nacionalidad del autor que deseas explorar: ")
                        object_ids = self.buscar_obras_nacionalidades(seleccion_nacionalidad)
                        if object_ids:
                            self.mostrar_detalles(object_ids)
                    except ValueError:
                        print("Nacionalidad invalida")
                        
            elif menu == "3":
                nombre_autor = input("\nIntroduce el nombre del autor que deseas buscar: ")
                object_ids = self.buscar_obras_autor(nombre_autor)
                if object_ids:
                    self.mostrar_detalles(object_ids)
                    
            elif menu == "4":
                None
                
            elif menu == "5":
                break
            
            else: 
                print("El valor ingresado no está dentro de las opciones")
                
    def buscar_obras_nacionalidades(self,nacionalidad):
        """
        Busca los ID's de las obras por la nacionalidad escogida por el usuario.    
        """
        link = f"https://collectionapi.metmuseum.org/public/collection/v1/search?q={nacionalidad}"
        
        try:
            response = requests.get(link)
            data = response.json()
            object_ids = data.get("objectIDs", [])
            return object_ids
        
        except:
            print("Se ha encontrado un error: ")
            return None
    
                        
    def leer_nacionalidades(self):
        """
        Lee la lista de las nacionalidades desde el archivo "nacionalidades.txt"
        """
        nacionalidades = []
        with open("nacionalidades.txt") as archivo:
            print("Nacionalidades disponibles")
            for linea in archivo:
                nacionalidad = linea.strip()
                print(f"- {nacionalidad}")
                nacionalidades.append(nacionalidad)
        return nacionalidades
    
    def listar_departamentos(self):
        """
        Obtiene y muestra la lista de todos los departamento disponibles desde la API.
        """
        link = "https://collectionapi.metmuseum.org/public/collection/v1/departments"

        try:
            response = requests.get(link)

            data = response.json()
            departamentos = data.get("departments", [])

            if not departamentos:
                print("No se encontraron departamentos.")
                return None
            
            print("Departamentos del Museo Metropolitano de Arte:")
            for departamento in departamentos:
                print(f"ID: {departamento["departamentId"]} - Nombre: {departamento["displayName"]}")
            return departamentos
        
        except:
            print("Se ha encontrado un error: ")

    def buscar_obras_departamento(self,departamento_id):
        """
        Busca los ID's de las obras por el departamento escogido por el usuario.
        """
        link = f"https://collectionapi.metmuseum.org/public/collection/v1/departments={departamento_id}"

        try :
            response = requests.get(link)
            data = response.json()
            object_ids = data.get("objectIDs", [])
            return object_ids

        except:
            print("Se ha encontrado un error: ")
            return None
            
    def buscar_obras_autor(self, nombre_autor):
        """
        Busca los ID's de las obras por el autor escogido por el usuario.
        """
        link = f"https://collectionapi.metmuseum.org/public/collection/v1/search?q={nombre_autor}"
        
        try :
            response = requests.get(link)
            data = response.json()
            objects_ids = data.get("objectIDs, []")
            return objects_ids
        
        except:
            print("Se ha encontrado un error")
            return None
        
    def mostrar_detalles(self, object_ids):
        """
        Obtiene los detalles de las obras a partir de sus ID's y crea los objetos Obra y Artista.
        Adicionalmente, imprime los resultados de la forma requerida.
        """
        if not object_ids:
            print("No se encontraron obras")
            return
        obras_encontradas = []
        print("\n Listado de Obras ")
        
        for obj_id in object_ids[:20]:
            link = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obj_id}"
            
            try :
                response = requests.get(link)
                detalles_obra = response.json()
            
                artista = Artista (
nombre = detalles_obra.get("artistDisplayName"),
nacionalidad = detalles_obra.get("artistNationality"),
fecha_nacimiento = detalles_obra.get("artistEndDate"),
fecha_muerte = detalles_obra.get("artistEndDate"))
            
                obra = Obra(
id = detalles_obra.get("objectID"),
titulo = detalles_obra.get("title"),
artista = artista,
departamento = detalles_obra.get("department"),
tipo = detalles_obra.get("classification"),
fecha_creacion = detalles_obra.get("objectDate"),
imagen_url = detalles_obra.get("primaryImage"))
            
                obras_encontradas.append(obra)   
                print(f" Id de la obra: {obra.id}, Título: {obra.titulo}, Nombre del autor: {obra.artista.nombre}")
            
            except:
                print(f"No se pudieron obtener los detalles para la obra con ID: {obj_id}")