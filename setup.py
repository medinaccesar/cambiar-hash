from setuptools import setup
from utils.constantes import Configuracion as conf

setup(
    name = conf.NOMBRE_AP,
    version = conf.VERSION,
    #packages = [],
    install_requires=[
        'python-dotenv',
        'python-gettext'     
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: GNU GENERAL PUBLIC LICENSE V3',
        'Operating System :: OS Independent',
    ],
    description=conf.DESCRIPCION_APP,
    url='https://github.com/medinaccesar/cambiar-hash'
)
