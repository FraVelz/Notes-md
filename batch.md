@echo off = Desactivar la visualización de los caracteres de entrada en la pantalla

echo. = salto de linea
echo asa = escribe "asa" en el cmd
pause = pausa los comandos hasta dar un enter
pause > nul = pausa los comandos hasta dar enter pero sin un aviso

:: = comentario no oficial
REM = comentario oficial

:inicio = crea una etiqueta llamada "inicio"

goto inicio = Llama al lector de codigo hasta la etiqueta inicio

title Hola Mundo = A la consola le quita el titulo, y le coloca "Hola Mundo"

color 0a = Cambia el color de consola por 0 (negro) de fondo, a (verde) para la letra

color 1 = texto azul oscuro

set nombre=dato de la variable 
= crea una variable con nombre "nombre" y almacena "dacto de la variable"

set /p num1="Ingresa el primer número: " = Pide un dato en consola

set ca1=5
set ca2=8
set /a res = %ca1% + %ca2%

echo %nombre% = imprime el dato de la variable
echo %ca1% + %ca2% = %res%