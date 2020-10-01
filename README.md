This is a Bioinformatics final project made by Daniel Alexander Basto (daniel.basto@udea.edu.co) and me (david.mcewen@udea.edu.co). Using Python and PHP. 



Lenguage Spanish: 

DESCRIPCIÓN:

TRABAJO FINAL - INFORMÁTICA I
                                                          I. DESCRIPCIÓN DEL TRABAJO A REALIZAR

Desarrollar una aplicación CRUD (Create, Read, Update and Delete) en PYTHON, un script que permita almacenar y gestionar la infraestructura de una IPS. Dicha aplicación contará con una entrada y salida de información en el Shell de Python y almacenamiento de la información en una base de datos MySQL.

i. La base de datos contará con 3 tablas, una para almacenar la información de los equipos de infraestructura, los responsables y las posibles ubicaciones en la IPS.

ii. La tabla de los equipos debe contar con:

o Serial
o Número de activo (numérico)
o Nombre del equipo
o Marca
o Código de ubicación (código de la tabla de ubicaciones)
o Código responsable (código de la tabla de responsables)
iii. La tabla de responsables deberá tener:

o Código responsable (tipo numérico)
o Nombre
o Apellido
o Número del documento de identidad (numérico)
o Cargo
iv. La tabla de ubicaciones tendrá:

o Código de ubicación (tipo numérico)
o Nombre de la ubicación
o Piso (numérico)
o Teléfono (numérico)

v. El algoritmo debe contar con un menú que permita ingresar a la información los equipos, los responsables y las ubicaciones o salir, la única forma de salir será si el usuario escoge esta opción. Si se selecciona una opción diferente a las anteriores, el algoritmo deberá sacar una alerta de error y volver al menú para que el usuario haga la selección nuevamente.

vi. Una vez se ingrese a una de las tres opciones anteriores, allí se debe tener la opción de hacer la aplicación CRUD para cada opción, decir, si se ingresa a la opción de equipos, allí el usuario verá otro menú que tenga las opciones de:

o Ingresar un nuevo equipo
o Actualizar la información de un equipo. Usando el número de activo como parámetro de búsqueda.
o Ver la información de un equipo. Usando el número de activo como parámetro de búsqueda.
o Ver la información de todos los equipos almacenados.
o Eliminar un equipo. Usando el número de activo como parámetro de búsqueda.
o Volver al menú principal
Si se selecciona una opción diferente a las anteriores, el algoritmo deberá sacar una alerta de error y volver al menú para que el usuario haga la selección nuevamente.

vii. Para las opciones de responsables y ubicaciones, se debe contar con menús similares al descrito en el numeral anterior, pero adaptado a cada caso.

viii. SOLO para la información de los equipos, cuando se muestre la información de estos, se deberá hacer en consulta múltiple, es decir, se debe mostrar la información que hay también en las otras tablas y que está relacionada con cada equipo. En la opción de responsable, no deberá aparecer el código del responsable si no el nombre, así que tendrán que consultar la tabla para traer el nombre, se debe hacer lo mismo con la ubicación.

ix. La aplicación debe validar la información numérica que se ingrese usando la sentencia try/except, es decir, los que en los numerales anteriores (2,3 y4) dice numérico, si el usuario ingresa letras, se activen las excepciones para permitir corregir esta opción.

x. La base de datos MySQL deberá estar configurada con los siguientes parámetros:
Nombre de la base de datos: informatica1
usuario: informatica1
contraseña: bio123

tablas: estarán nombradas y configurada según lo considerado por cada equipo

xi. Las tres tablas deberán tener información previamente cargada para poder hacer la consulta desde un principio, por favor, aunque la información que ingresen va a ser ficticia, esta debe tener coherencia, no se aceptan letras puestas sin sentido para llenar los campos.

xii. Importante: las tablas de la base de datos deben estar relacionadas, es decir, cuando se vaya a ingresar la información de nuevo equipo, en el campo del responsable se debe mostrar la información disponible para cada caso. Por ejemplo:
o Se pide ingresar el responsable y en la tabla responsables de la base de datos hay 5 registros, es decir, 5 opciones, cuando se le pida al usuario escoger esta opción será algo como:

1- Responsable 1 (Nombre y apellido del responsable en la tabla)
2- Responsable 2
3- Responsable 3
4- Responsable 4
5- Responsable 5

o Para el caso de la ubicación del equipo, deberá ser igual, pero se debe listar las ubicaciones disponibles en la tabla.








                                                      II. OBSERVACIONES DE ENTREGA:
                                                      
                                                      
• El trabajo se realizará en grupos de 2, los cuales se inscribirán en un archivo que está compartido en Drive, es decir, ustedes mismos irán seleccionando los grupos y se irán inscribiendo.
• Se deben entregar todos los archivos (.py) diseñados en PYTHON y el archivo de la base de datos en MySQL, incluirá las 3 tablas y la información previamente cargada para probar. Deben asegurarse de enviar correctamente los archivos ya que la revisión se realizará única y exclusivamente con los archivos enviados carados en la tarea del classroom que de abrirá para tal efecto.
• En la cabecera del script se deben colocar los nombres de los autores como un comentario (integrantes del grupo) y el código debe estar debidamente documentado. Descripción de las variables, descripción de los procesos y resultados a mostrar.
• El trabajo debe ser cargado en el classroom, solo una vez, es decir, uno de los dos integrantes hará la carga a más tardar el día DOMINGO 09 DE DICIEMBRE DE 2018 A LAS 11:59PM. IMPORTANTE: EL TRABAJO NO SE RECIBIRÁ DESPUÉS DE ESTA HORA, ES DECIR A LAS 12:00AM ESTE 20% SERÁ CERO (0.0).
• Cualquier intento de fraude o copia de código entre los diferentes equipos implicará una calificación de 0.0 para todos los involucrados sin posibilidad de recuperación.
• Si al ejecutar el script hay algún error, sin importar cual sea, el trabajo se calificará sobre 3.0.
