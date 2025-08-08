from Artista import Artista
from Obra import Obra
import requests
import json

class Museo:
    def start(self):
        
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
                        seleccion_id = int(input("\n Introduce el ID del departamento que deseas explorar:"))
                        self.buscar_obras_departamento(seleccion_id)
                    except ValueError:
                        print("Entrada no valida. Por favor, introduce un numero:")
                        
            elif menu == "2":
                nacionalidades = self.leer_nacionalidades()
                if nacionalidades:
                    try:
                        seleccion_nacionalidad = input("\nIntroduce la nacionalidad del autor que deseas explorar: ")
                        self.buscar_obras_nacionalidades(seleccion_nacionalidad)
                    except ValueError:
                        print("Nacionalidad invalida")
                        
    def buscar_obras_nacionalidades(self,nacionalidad):
        
        link = f"https://collectionapi.metmuseum.org/public/collection/v1/search?q={nacionalidad}"
        
        try:
            response = requests.get(link)
            data = response.json()
            object_ids = data.get("objectIDs", [])
            
            if not object_ids:
                print("No se encontraron departamentos.")
                return None
            
            print("Departamentos del Museo Metropolitano de Arte:")
            for obj_id in object_ids [:40]:
                    print(f" - ID de Obra: {obj_id}")
            return object_ids
        
        except:
            print("Se ha encontrado un error: ")
    
                        
    def leer_nacionalidades(self):
        nacionalidades = []
        with open("nacionalidades.txt") as archivo:
            print("Nacionalidades disponibles")
            for linea in archivo:
                nacionalidad = linea
                print(f"- {nacionalidad}")
                nacionalidades.append(nacionalidad)
        return nacionalidades
    
    def listar_departamentos(self):
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
        link = f"https://collectionapi.metmuseum.org/public/collection/v1/departments={departamento_id}"

        try :
            response = requests.get(link)

            data = response.json()
            object_ids = data.get("objectIDs", [])

            if not object_ids:
                print("No se encontraron departamentos.")
                return None
            
            print("Departamentos del Museo Metropolitano de Arte:")
            for obj_id in object_ids[:40]:
                print(f" - Id de Obra: {obj_id}")
            return object_ids
        
        except:
            print("Se ha encontrado un error: ")
            
    def buscar_obras_autor(self, nombre_autor):
        link = f"https://collectionapi.metmuseum.org/public/collection/v1/search?q={nombre_autor}"
        
        try :
            response = requests.get(link)
            
            data = response.json()
            objects_ids = data.get("objectIDs, []")
            return objects_ids
        
        except:
            print("Se ha encontrado un error")
            return None