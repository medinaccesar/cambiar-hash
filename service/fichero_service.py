import shutil
import os
from datetime import datetime

class Fichero():
       
    def marca_temporal(self):
        ahora = datetime.now()
        return ahora.strftime('%y%m%d_%H%M%S')
   
    def annadir_marca_temporal(self, nombre_archivo):
        marca_temporal = self.marca_temporal()
        # Se extrae la extensión del archivo
        extension = os.path.splitext(nombre_archivo)[1]
        # Se concatena la extensión con la marca temporal
        nombre_archivo = nombre_archivo[:-
                                        len(extension)] +'_'+ marca_temporal + extension
        return nombre_archivo
  
    def crear_copia(self, nombre_archivo): 
        nombre_copia = self.annadir_marca_temporal(nombre_archivo)
        shutil.copy2(nombre_archivo,nombre_copia)  
        return nombre_copia
    
    def existe(self,ruta):       
        if not os.path.isfile(ruta):
            return False       
        return True
    
   