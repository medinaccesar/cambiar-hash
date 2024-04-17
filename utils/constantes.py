import os


class Configuracion:

    __slots__ = ()

    NOMBRE_AP = 'cambiarhash'
    DESCRIPCION_APP = 'Permite cambiar el «hash» de un archivo sin corromperlo'
    VERSION = '1.0.0'
    CREDITOS = 'César Medina'

  
    # Directorios
    DIR_DOCUMENTOS = os.path.expanduser("~")
    DIR_ABS = os.path.dirname(os.path.abspath(__file__))+os.path.sep   

    # En función del tamaño del archivo se elige el método para calcular el hash, o bien se lee en memoria entero o se divide en partes
    TAMANNO_MAX_ARCHIVO_CALC_HASH = 524280000  # 500M
