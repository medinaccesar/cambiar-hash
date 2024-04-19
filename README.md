# cambiarhash
Permite cambiar el «hash» de un archivo sin corromperlo.

# Requisitos
 Python 3.
 
# Instalación de dependencias
Se instalan las dependencias:
```
 pip install -r requirements.txt
 ```
Se compilan los archivos de idiomas:
```
python utils/compile_lang.py 
```
# Uso
```
Uso: cambiarhash.py [-h] [-c ARCHIVO | -d ARCHIVO | -o ARCHIVO | -g] [--version]

cambiarhash 1.0.0

argumentos opcionales:
  -h, --help                          muestra este mensaje de ayuda y sale
  -c ARCHIVO, --cambiar ARCHIVO       Cambia al vuelo el «hash» del archivo
  -d ARCHIVO, --duplicar ARCHIVO      Crea un nuevo archivo pero con distinto «hash»
  -m ARCHIVO, --mostrar ARCHIVO      Calcula el «hash» del archivo
  -g, --gui                           Se ejecuta el entorno gráfico
  --version                           Muestra la versión del programa
```
Por ejemplo:

* **Cambiar el «hash» de un archivo:**
```
$ python cambiarhash.py -c prueba.pdf
«Hash» del archivo: a56274c33feed7d80606ceadf3e33b37bdc199eed519e26c0d6506404a56b18f
Progreso |████████████████████████████████████████| 100% Completo
El «hash» del archivo se ha cambiado correctamente.
Nuevo «hash» del archivo: eab62c3db3e25b3229c39d2059449d51b93fda9962811b20ee727abe64a4d1e2 
```
* **Calcular el «hash» de un archivo:**
```
$ python cambiarhash.py -m prueba.pdf
Progreso |████████████████████████████████████████| 100% Completo
«Hash» del archivo: eab62c3db3e25b3229c39d2059449d51b93fda9962811b20ee727abe64a4d1e2 
```
* **Crea un nuevo archivo pero con distinto «hash»:**
```
$ python cambiarhash.py -d prueba.pdf
«Hash» del archivo original: eab62c3db3e25b3229c39d2059449d51b93fda9962811b20ee727abe64a4d1e2
Progreso |████████████████████████████████████████| 100% Completo
Nombre del archivo duplicado: prueba_240416_223022.pdf
«Hash» del archivo duplicado: 3d22b297602fb4ec694d65773aa1c3872384249f2a8c2b06f5b9013ba32c2f53 
```
# Traducciones / Translations
Se puede usar como base ./locale/programa.po y con «poedit» u otro editor rellenar las traducciones.  El archivo se coloca dentro de la carpeta correspondiente, por ejemplo para portugués en ./locale/pt/LL_MESSAGES/:

```
cifra-descifra/
├─ README.md
├─ cambiarhash.py
├─ ...
├─ locale/
│  ├─ pt/    
│  │   └─ LL_MESSAGES/
│  │        └─programa.po
│  ├─ ...
|
├─ ...  
```
Posteriormente se compila el archivo de traducción ejecutando:
```
python utils/compile_lang.py 
```
El idioma de la aplicación, (distinto de español), se fija en el archivo .env, (renombrar .env.template):
```
IDIOMA = 'pt'
```

[EN] You can use as a base ./locale/programa.po and with "poedit" or another editor fill in the translations.  The file is placed inside the corresponding folder, for example for Portuguese in ./locale/pt/LL_MESSAGES/:
```
cifra-descifra/
├─ README.md
├─ cambiarhash.py
├─ ...
├─ locale/
│  ├─ pt/    
│  │   └─ LL_MESSAGES/
│  │        └─programa.po
│  ├─ ...
|
├─ ...  
```
Subsequently, the translation file is compiled by executing:
```
python utils/compile_lang.py 
```
The application language is set in the .env file, (remane .env.template):
```
IDIOMA = 'pt'
```

# Ejecutables para linux ubuntu y windows
Se puede crear el ejecutable con «pyinstaller».

En la carpeta «dist» próximanente....

# ejemplos de uso del ejecutable

* **Cambiar el «hash» de un archivo (linux):**
```
cambiarhash -c prueba.pdf
«Hash» del archivo: a56274c33feed7d80606ceadf3e33b37bdc199eed519e26c0d6506404a56b18f
Progreso |████████████████████████████████████████| 100% Completo
El «hash» del archivo se ha cambiado correctamente.
Nuevo «hash» del archivo: eab62c3db3e25b3229c39d2059449d51b93fda9962811b20ee727abe64a4d1e2 
```

* **Cambiar el «hash» de un archivo (win):**
```
cambiarhash.exe -c prueba.pdf
«Hash» del archivo: a56274c33feed7d80606ceadf3e33b37bdc199eed519e26c0d6506404a56b18f
Progreso |████████████████████████████████████████| 100% Completo
El «hash» del archivo se ha cambiado correctamente.
Nuevo «hash» del archivo: eab62c3db3e25b3229c39d2059449d51b93fda9962811b20ee727abe64a4d1e2 
```
* **Calcular el «hash» de un archivo (linux):**
```
cambiarhash -m prueba.pdf
Progreso |████████████████████████████████████████| 100% Completo
«Hash» del archivo: eab62c3db3e25b3229c39d2059449d51b93fda9962811b20ee727abe64a4d1e2 
```
* **Calcular el «hash» de un archivo (win):**
```
cambiarhash.exe -m prueba.pdf
Progreso |████████████████████████████████████████| 100% Completo
«Hash» del archivo: eab62c3db3e25b3229c39d2059449d51b93fda9962811b20ee727abe64a4d1e2 
```

* **Crea un nuevo archivo pero con distinto «hash» (linux):**
```
cambiarhash -d prueba.pdf
«Hash» del archivo original: eab62c3db3e25b3229c39d2059449d51b93fda9962811b20ee727abe64a4d1e2
Progreso |████████████████████████████████████████| 100% Completo
Nombre del archivo duplicado: prueba_240416_223022.pdf
«Hash» del archivo duplicado: 3d22b297602fb4ec694d65773aa1c3872384249f2a8c2b06f5b9013ba32c2f53 
```
* **Crea un nuevo archivo pero con distinto «hash» (win):**
```
cambiarhash.exe -d prueba.pdf
«Hash» del archivo original: eab62c3db3e25b3229c39d2059449d51b93fda9962811b20ee727abe64a4d1e2
Progreso |████████████████████████████████████████| 100% Completo
Nombre del archivo duplicado: prueba_240416_223022.pdf
«Hash» del archivo duplicado: 3d22b297602fb4ec694d65773aa1c3872384249f2a8c2b06f5b9013ba32c2f53 
```

# Líneas futuras

1) Interfaz gráfica
2) Aplicación móvil

