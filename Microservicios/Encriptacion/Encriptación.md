![Help Builder Web Site](../../Img/Logo.png)
# Proyecto_SA_Grupo2
### Encriptación
Este documento tiene el objetivo de:
<br>
* Dar una descripción breve del microservicio de Encriptación.

Este microservicio tiene la función de tomar los datos de un usuario que este registrado en la base de datos de iVoting y para tener una seguridad de los datos sensibles que se manejan utilizar la estructura de datos conocida como Blockchain, "el uso de esta tecnología se explica de mejor forma en la carpeta Blockchain"

Lo que se hace para encriptar es crear una lista enlazada donde el apuntador es un Hashing que esta en un formato como "HS256" donde el bloque siguiente siempre es apuntado por el Hashing del bloque anterior.

Los datos que guarda cada bloque son:
<table>
<thead>
	<tr>
		<th>Dato</th>
		
	</tr>
</thead>
<tbody>
	<tr>
		<td>DPI</td>
		
	</tr>
	<tr>
		<td>Nombre</td>
		
	</tr>
	<tr>
		<td>Apellidos</td>
		
	</tr>
	<tr>
		<td>Fecha de nacimiento</td>
		
	</tr>
	<tr>
		<td>Lugar de nacimiento</td>
		
	</tr>
	<tr>
		<td>Nombre de la Madre del usuario</td>
		
	</tr>
	<tr>
		<td>Nombre del Padre del usuario</td>
		
	</tr>
</tbody>
</table>










