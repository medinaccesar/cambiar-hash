
from service.fichero_service import Fichero
from utils.espannol_string_argparse import *
import argparse
from utils.locale_manager import _
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

        if args.cambiar is not None:
           
            self._cambiar_hash_archivo(args.cambiar)   
      
        elif args.duplicar is not None:
                       
            self._duplicar_archivo(args.duplicar)             
            
        elif args.mostrar is not None:          
           
            self._mostrar_hash_archivo(args.mostrar) 
            
        elif args.acerca is not False:          
           
            self._acerca_de() 
                           
        else:
            print(_('No se especificó ninguna opción'))
    
    
    def _cambiar_hash_archivo(self, nombre_archivo): 
               
        barra_progreso = BarraProgresoConsola(100)        
        self._comprobar_fichero_existe(nombre_archivo)
        barra_progreso.dibujar(10)
        hash = self._hash_service.calcular_hash_archivo(nombre_archivo)
        print(_('«Hash» del archivo:'),hash)
        self._hash_service.cambiar_hash_archivo(nombre_archivo)
        hash_nuevo = self._hash_service.calcular_hash_archivo(nombre_archivo)
        barra_progreso.dibujar(80)
        print(_('El «hash» del archivo se ha cambiado correctamente.'))
        print(_('Nuevo «hash» del archivo:'),hash_nuevo,'\n')
        
    def _duplicar_archivo(self, nombre_archivo):
        
        barra_progreso = BarraProgresoConsola(100)            
        self._comprobar_fichero_existe(nombre_archivo)
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
        
    def _mostrar_hash_archivo(self, nombre_archivo):
        
        barra_progreso = BarraProgresoConsola(100)
        self._comprobar_fichero_existe(nombre_archivo)
        barra_progreso.dibujar(10)
        hash = self._hash_service.calcular_hash_archivo(nombre_archivo)                     
        barra_progreso.dibujar(80)
        print(_('«Hash» del archivo:'),hash,'\n')
        
    def _comprobar_fichero_existe(self, nombre_archivo):
        
        if not self._fichero_service.existe(nombre_archivo):
            print(_('El archivo no existe.'), '\n')
            sys.exit(1)
            
    def _acerca_de(self):      
        print(conf.NOMBRE_AP,'v'+conf.VERSION)        
        print(_(conf.DESCRIPCION_APP), '\n')
        print(conf.CREDITOS, '\n')        
             
   
    def _get_parser(self):
        
        parser = argparse.ArgumentParser(
            description=conf.NOMBRE_AP+" "+str(conf.VERSION) ) 
        group = parser.add_mutually_exclusive_group()
        group.add_argument('-c', '--cambiar', type=str,
                           metavar=(_('ARCHIVO')), help=_('Cambia al vuelo el «hash» del archivo'))       
        group.add_argument('-d', '--duplicar', type=str,
                           metavar=(_('ARCHIVO')), help=_('Crea un nuevo archivo pero con distinto «hash»'))  
        group.add_argument('-m', '--mostrar', type=str,
                           metavar=(_('ARCHIVO')), help=_('Muestra el «hash» del archivo'))        
        group.add_argument('-g', '--gui', action='store_true',
                           help=_('Se ejecuta el entorno gráfico'))
        parser.add_argument('--version', action='version', version='%(prog)s ' +
                            conf.VERSION, help=_('Muestra la versión del programa'))
        parser.add_argument("--acerca", action='store_true', help=argparse.SUPPRESS)
        
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
