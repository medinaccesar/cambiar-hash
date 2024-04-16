import os


class Configuracion:

    __slots__ = ()

    NOMBRE_AP = 'cambia-hash'
    DESCRIPCION_APP = 'Cambia el «hash» de un archivo'
    VERSION = '1.0.0'
    CREDITOS = 'César Medina'

  
    # Directorios
    DIR_DOCUMENTOS = os.path.expanduser("~")
    DIR_ABS = os.path.dirname(os.path.abspath(__file__))+os.path.sep   

    # En función del tamaño del archivo se elige el método para calcular el hash, o bien se lee en memoria entero o se divide en partes
    TAMANNO_MAX_ARCHIVO_CALC_HASH = 524280000  # 500M
