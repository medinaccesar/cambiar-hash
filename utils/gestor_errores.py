import errno
from utils.locale_manager import _


class GestorErrores():

    def __init__(self):
        # Reglas ordenadas
        self._reglas = [
            (self._es_error_permisos, 'No tiene permisos suficientes para acceder al archivo.'),
            (self._es_error_disco_lleno, 'No hay espacio suficiente en el disco.'),
        ]

    def obtener_mensaje(self, error):
        for coincide, mensaje in self._reglas:
            if coincide(error):
                return _(mensaje)
        return _('No se ha podido procesar el archivo:') + ' ' + str(error)

    def _es_error_permisos(self, error):
        return isinstance(error, PermissionError)

    def _es_error_disco_lleno(self, error):
        return isinstance(error, OSError) and error.errno == errno.ENOSPC
