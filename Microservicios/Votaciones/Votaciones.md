![Logo](../../Img/Logo.png)
# Votaciones

El módulo de votaciones puede ser accedido solamente por personas previamente registradas. El cual es un microservicio independiente encargado de recibir los votos de las personas en las distintas elecciones que pueden estar creadas así como la información general del voto, es decir, fecha, hora y localidad donde se realizó.

Para asegurar la seguridad del voto y garantizar que el voto es secreto, este microservicio se comunica con el microservicio de encriptación el cual se encarga de esto.

Así mismo se comunica con el microservicio encargado de realizar la auditoría de los votos, para garantizar que todos los votos sean válidos y autenticados correctamente.	

Una parte importante de este servicio es que debe consultar al servicio de cierre de elecciones, para saber si la elección seleccionada por el usuario sigue en estado "Activo".

El servicio ofrece:

	●	Selección entre las opciones disponibles para votar.
	●	Garantizar que se realice solamente un voto por persona.
	●	Guardar los votos en la base de datos
	●	Almacenar los resultados en la base de datos