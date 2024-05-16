# Obligatorio
Trabajo obligatorio de programación 1

Se desea desarrollar un sistema robusto que facilite la gestión de los pacientes en una policlínica,
desde la expedición de tickets hasta la finalización de las consultas médicas.
Este sistema debe permitir la gestión completa de la atención médica a pacientes, incluyendo el
registro de socios, gestión de consultas, y el seguimiento hasta la conclusión de cada consulta.
Este sistema busca no solo mejorar la eficiencia de los procesos internos sino también elevar la
calidad del servicio ofrecido a los pacientes.
Las funcionalidades que debe tener el sistema son:
Alta de especialidad:
  • Registro de información de la especialidad: Nombre de la especialidad y precio fijo
  asociado.
  • Cada especialidad médica tendrá un precio fijo asociado, que se aplicará a todos los
  tickets de consulta.
  • Ejemplo:
o Traumatología: $350 por consulta.
o Cardiología: $400 por consulta.
Alta de socio:
• Registro de información personal: nombre, apellido, cédula de identidad, fecha de
nacimiento, fecha de ingreso a la institución y número de celular.
• Hay dos tipos de socios, los bonificados y no bonificados. En caso de que sean
bonificados, se aplicará un descuento de un 20% en cada consulta.
• También se debe llevar la deuda que tiene cada socio asociado.
Alta de médico:
• Registro de información personal: nombre, apellido, cédula de identidad, fecha de
nacimiento, fecha de ingreso a la institución y número de celular.
• Los médicos tendrán una especialidad también.
Alta de consulta médica:
• Registro de consultas médicas, estas consultas deben tener una especialidad asociada,
un médico de dicha especialidad, la fecha de la consulta y una lista de pacientes que se
atenderán en dicha consulta. También se debe registrar la cantidad máxima de
pacientes que se pueden emitir por consulta.
• Los pacientes tendrán número de consulta, por ende, si el paciente A se quiere atender
con el número 3, deberá estar en la tercera posición del array.
Emitir ticket de consulta:
• Se debe permitir que los socios se registren en las consultas disponibles, permitiendo
que elijan el número en que se desean atender.
Por otra parte, también se deben poder realizar consultas al sistema:
1. Obtener todos los médicos asociados a una especialidad específica.
Programación 1
2. Obtener el precio de una consulta de una especialidad en específico.
3. Listar todos los socios con sus deudas asociadas en orden ascendente.
4. Realizar consultas respecto a cantidad de consultas entre dos fechas
5. Realizar consultas respecto a las ganancias obtenidas entre dos fechas.
A continuación, se declara el flujo del programa, lo que aparece en texto azul es lo que el
programa debe mostrar en pantalla: Todo el flujo debe ser continuo y en cada paso el usuario
debe tener la opción de regresar a la opción anterior o al menú principal dependiendo de donde
esté.
Menú principal:
El menú principal deberá continuar en loop hasta que el usuario ingrese una opción válida o la
opción salir del programa.
Seleccione una opción del menú:
1. Dar de alta una especialidad
2. Dar de alta un socio
3. Dar de alta un médico
4. Dar de alta una consulta médica
5. Emitir un ticket de consulta
6. Registrar una consulta
7. Realizar consultas
8. Salir del programa
En caso de no ser una opción válida mostrar en pantalla: La opción seleccionada no es correcta,
vuelva a intentar con otra opción.
Dar de alta una especialidad:
- Ingrese el nombre de la especialidad:
- Ingrese el precio asociado:
En caso de que la especialidad no sea un string válido o el precio no sea un int mostrar en
pantalla: El nombre de la especialidad es incorrecto, ingréselo nuevamente o El precio de la
especialidad es incorrecto, ingréselo nuevamente.
Esto debe estar en loop hasta que ambos datos sean correctos.
Si se pudo crear la especialidad mostrar en pantalla: La especialidad se ha creado con éxito
Dar de alta un socio
- Ingrese el nombre:
- Ingrese el apellido:
- Ingrese la cédula de identidad:
- Ingrese la fecha de nacimiento en formato aaaa-mm-dd:
- Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd:
- Ingrese el número de celular:
- Ingrese el tipo de socio: 1- Bonificado 2- No bonificado
Esta operación deberá estar en loop hasta que todos los parámetros sean correctos.
Programación 1
En caso de que el nombre no sea un string mostrar en pantalla: No es un nombre válido,
ingréselo de nuevo
En caso de que el apellido no sea un string mostrar en pantalla: No es un apellido válido,
ingréselo de nuevo
En caso de que la cédula no sea de 8 dígitos mostrar en pantalla: No es una cédula válida, ingrese
nuevamente una cédula de 8 dígitos.
En caso de que la fecha no sea en el formato aaaa-mm-dd mostrar en pantalla: No es una fecha
válida, vuelva a ingresarla en el formato aaaa-mm-dd. Se recomienda usar la libreria datetime
para el manejo de fechas.
En caso de que el número de celular no sea un int de 9 dígitos mostrar en pantalla: No es un
número de celular válido, ingrese un número con el formato 09XXXXXXX
Si el valor ingresado no es 1 o 2 mostrar en pantalla: El valor ingresado no es correcto, elige la
opción 1 o 2.
Dar de alta un médico
- Ingrese el nombre:
- Ingrese el apellido:
- Ingrese la cédula de identidad:
- Ingrese la fecha de nacimiento en formato aaaa-mm-dd:
- Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd:
- Ingrese el número de celular:
- Ingrese la especialidad
Esta operación deberá estar en loop hasta que todos los parámetros sean correctos.
En caso de que el nombre no sea un string mostrar en pantalla: No es un nombre válido,
ingréselo de nuevo
En caso de que el apellido no sea un string mostrar en pantalla: No es un apellido válido,
ingréselo de nuevo
En caso de que la cédula no sea de 8 dígitos mostrar en pantalla: No es una cédula válida, ingrese
nuevamente una cédula de 8 dígitos.
En caso de que la fecha no sea en el formato aaaa-mm-dd mostrar en pantalla: No es una fecha
válida, vuelva a ingresarla en el formato aaaa-mm-dd. Se recomienda usar la libreria datetime
para el manejo de fechas.
En caso de que el número de celular no sea un int de 9 dígitos mostrar en pantalla: No es un
número de celular válido, ingrese un número con el formato 09XXXXXXX
En caso de que la especialidad no sea un string válido mostrar en pantalla: La especialidad debe
ser un string. Y en caso de que la especialidad no coincida con alguna de las especialidades dadas
de alta mostrar esta especialidad no fue dada de alta mostrar en pantalla: Esta especialidad no
está dada de alta elija una opción:
1 - Volver a ingresar la especialidad
2 - Dar de alta esta especialidad
Si se selecciona la opción 2, se debe ir a la parte del flujo dar de alta una especialidad.
Programación 1
Dar de alta una consulta
- Ingrese la especialidad
- Ingrese el nombre del médico
- Ingrese la fecha de consulta
- Ingrese la cantidad de pacientes que se atenderán
En caso de que la especialidad no sea un string válido mostrar en pantalla: La especialidad debe
ser un string. Y en caso de que la especialidad no coincida con alguna de las especialidades dadas
de alta mostrar esta especialidad no fue dada de alta mostrar en pantalla: Esta especialidad no
está dada de alta elija una opción:
1 - Volver a ingresar la especialidad
2 - Dar de alta esta especialidad
Si se selecciona la opción 2, se debe ir a la parte del flujo dar de alta una especialidad.
En caso de que el nombre del médico no sea uno de los médicos dados de alta, mostrar en
pantalla: Este médico no está dado de alta, elija una opción:
1 - Volver a ingresar el médico
2 - Dar de alta el médico
Si se selecciona la opción 2, se debe ir a la parte del flujo dar de alta un médico.
Emitir ticket de consulta
- Ingrese la especialidad
Se debe mostrar en la pantalla una lista con las consultas de esa especialidad. Ejemplo:
1 - Doctor: Juan Pérez Día de la consulta: 2024-07-01
2 - Doctor: Ana Rodríguez Día de la consulta: 2024-08-15
- Seleccione la opción deseada
Listar los números que quedan disponibles para esta consulta
- Seleccionar el número de atención deseado
En caso de que la especialidad no sea un string válido mostrar en pantalla: La especialidad debe
ser un string. Y en caso de que la especialidad no coincida con alguna de las especialidades dadas
de alta mostrar esta especialidad no fue dada de alta mostrar en pantalla: Esta especialidad no
está dada de alta elija una opción:
1 - Volver a ingresar la especialidad
2 - Dar de alta esta especialidad
Si se selecciona la opción 2, se debe ir a la parte del flujo dar de alta una especialidad.
En caso de que la opción seleccionada no esté dentro del rango de la lista mostrar en pantalla:
La opción ingresada no es una opción válida debe ser un número ente x e y, vuelva a ingresarla.
En caso de que el número de atención ingresado no sea válido mostrar en pantalla: No es un
número de consulta válido, los números válidos son: 1, 4, 5 y 7
Realizar consulta
Seleccione una opción:
Programación 1
1. Obtener todos los médicos asociados a una especialidad específica.
2. Obtener el precio de una consulta de una especialidad en específico.
3. Listar todos los socios con sus deudas asociadas en orden ascendente.
4. Realizar consultas respecto a cantidad de consultas entre dos fechas
5. Realizar consultas respecto a las ganancias obtenidas entre dos fechas.
Si se seleccionan las opciones 4 o 5 se debe solicitar fecha inicio y fecha final.
En caso de que la fecha no sea en el formato aaaa-mm-dd mostrar en pantalla: No es una fecha
válida, vuelva a ingresarla en el formato aaaa-mm-dd.
