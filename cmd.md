Simbolo del sistema windows no distingue entre masyusculas 
Directorio: Carpeta
para utilizar espacios en el cmd se utiliza las ""
se puede autocmpletar con tab los nombres de archivos y directorios

# directorios

cd nombreDeDirectorio = Mover al directorio "nombreDeDirectorio"  (Se puede mover por mas directorios "cd nombreDeDirectorio\\nombreDeDirectorio2\\" )
cd .. = Retrocceder un directorio (Se puede agregar mas directorios para retroceder "cd ..\\..\\")
dir = Listar archivos y directorios en la ruta presente
cls = limpiar consola

mkdir MyDirectorio = crear Directorio "MyDirectorio" (Se puede agregar mas carpetas una dentro de otra "mkdir MyDirectorio\\MyDirectorio2")

md MyDirectorio = crear Directorio "MyDirectorio" (Se puede agregar mas carpetas para crear, tambien Se puede agregar mas carpetas una dentro de otra) 

ren MyDiretorio nuevoNombreDirectorio = cambiar nombre de la carpeta de "MyDiretorio" a "nuevoNombreDirectorio"

rd nuevoNombreDirectorio = eliminar Directorio "nuevoNombreDirectorio"

# archivos
copy nul index.html = Crear archivo "index.html" vacio "nul"

copy con index2.html = Crear archivo , "con" nos permite agregar contenido al archivo para finalizar escribimos ctrl + z y enter

del index2.html = eliminar archivo "index2.html"

del directorio = eliminar directorio "directorio"

copy index.html directorio = copiar archivo "index.html" a el directorio "directorio"

rmdir /s carpetaConArchivos = eliminar carpeta con su contenido (tambien se puede eliminar multiples carpetas)

xcopy /s RutaDeArchivos CopiarEn = Copia los archivos de "RutaDeArchivos" y los envia a "CopiarEn"

dir *.exe = mostrar todos los archivos .exe

Se puede abrir archivos solo utilizando la ruta del archivo .exe y copiandolo en el cmd

dir /? = muestra toda la informacion de ayuda del comando "dir" (se puede utilizar para otros comandos)

tasklist = muestra la lista de procesos abiertos

taskkill /f /im opera.exe = cierra la aplicacion de opera

shutdown /s /t 60 = apaga el pc en 30 segundos
shutdown /a = cancelar el apagado del pc.