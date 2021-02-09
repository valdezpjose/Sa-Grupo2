##Descripción de la seguridad de la aplicación

Para ***iVoting*** lo más importante es garantizar a los votantes que su voto es secreto y seguro, para que puedan tener confianza en la aplicación y se redusca la cantidad de personas que votan de forma presencial.
Para esto existirá un micoservicio encargado de encriptar la información al momento de realizar un voto, es decir la información de la persona que realizó el voto. En el momento de mostrar los resultados, solamente se mostrará el todal de personas que votaron por las diferentes opciones.

De igual forma, la información de las personas registradas será encriptada para evitar el mal uso de ésta. 

Para garantizar seguridad en la autenticación de los usuarios, al momento que un usuario ingrese a la plataforma se le enviará un tocken para confirmar la autenticidad del ingreso. Esto se realizará utilizando JWT (Json Web Token).

Con estas medidas se espera una aplicación segura y confiable para realizar distintas elecciones.