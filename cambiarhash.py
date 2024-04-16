
from service.fichero_service import Fichero
from utils.espannol_string_argparse import *
import argparse
from utils.locale_manager import _,p
from dotenv import load_dotenv  # type: ignore

from utils.constantes import Configuracion as conf
from service.hash_service import HashService
from utils.barra_progreso import BarraProgresoConsola

class CambiarHash():

    def __init__(self):               
   
        self._hash_service = HashService()       
        self._fichero_service = Fichero()       
           
        parser = self._get_parser()       
        self._procesar_argumentos(parser)
   

    # Se ejecuta en modo consola
    def _ejecutar_modo_consola(self, args):

        print(_('Se ejecuta en modo consola.'),'\n')

        if args.cambiar is not None:
            barra_progreso = BarraProgresoConsola(100)
            nombre_archivo = args.cambiar
            barra_progreso.dibujar(10)
            hash = self._hash_service.calcular_hash_archivo(nombre_archivo)
            print(_('«Hash» del archivo:'),hash)
            self._hash_service.cambiar_hash_archivo(nombre_archivo)
            hash_nuevo = self._hash_service.calcular_hash_archivo(nombre_archivo)
            barra_progreso.dibujar(80)
            print(_('El «hash» del archivo se ha cambiado correctamente.'))
            print(_('Nuevo «hash» del archivo:'),hash_nuevo,'\n')
      
        elif args.duplicar is not None:
            barra_progreso = BarraProgresoConsola(100)
            nombre_archivo = args.duplicar
            barra_progreso.dibujar(10)
            hash = self._hash_service.calcular_hash_archivo(nombre_archivo)
            print(_('«Hash» del archivo original:'),hash)
            nombre_archivo_nuevo = self._fichero_service.crear_copia(nombre_archivo)
            self._hash_service.cambiar_hash_archivo(nombre_archivo_nuevo)
            barra_progreso.dibujar(10)
            hash_nuevo = self._hash_service.calcular_hash_archivo(nombre_archivo_nuevo)         
            barra_progreso.dibujar(70)
            print(_('Nombre del archivo duplicado:'),nombre_archivo_nuevo)
            print(_('«Hash» del archivo duplicado:'),hash_nuevo,'\n')
        elif args.obtener is not None:
            barra_progreso = BarraProgresoConsola(100)
            barra_progreso.dibujar(10)
            nombre_archivo = args.obtener
            hash = self._hash_service.calcular_hash_archivo(nombre_archivo)                     
            barra_progreso.dibujar(80)
            print(_('«Hash» del archivo:'),hash,'\n')
        else:
            print(_('No se especificó ninguna opción'))
           
   
    def _get_parser(self):
        
        parser = argparse.ArgumentParser(
            description=conf.NOMBRE_AP+" "+str(conf.VERSION))  # formatter_class=CustomHelpFormatter
        group = parser.add_mutually_exclusive_group()
        group.add_argument('-c', '--cambiar', type=str,
                           metavar=(_('ARCHIVO')), help=_('Cambia al vuelo el «hash» del archivo'))       
        group.add_argument('-d', '--duplicar', type=str,
                           metavar=(_('ARCHIVO')), help=_('Crea un nuevo archivo pero con distinto «hash»'))    
        group.add_argument('-o', '--obtener', type=str,
                           metavar=(_('ARCHIVO')), help=_('Calcula el «hash» del archivo'))        
        group.add_argument('-g', '--gui', action='store_true',
                           help=_('Se ejecuta el entorno gráfico'))
        parser.add_argument('--version', action='version', version='%(prog)s ' +
                            conf.VERSION, help=_('Muestra la versión del programa'))

        return parser

    def _procesar_argumentos(self, parser):
        
        args = parser.parse_args()
        if args.gui:
            # TODO
            print('Próximamente...')
        else:
            self._ejecutar_modo_consola(args)



if __name__ == "__main__":
     
    CambiarHash()
