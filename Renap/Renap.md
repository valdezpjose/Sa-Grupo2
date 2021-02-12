![Logo](../Img/Logo.png)

# Proyecto_SA_Grupo2

## Base de datos Renap

El sistema ***iVoting*** tiene un servicio que simula el funcionamiento del RENAP. En este servicio consiste en consultas para tener la información de una persona en este caso de un usuario. El sistema utilizara este servicio para validar si un usuario ya existe para que no se tenga registros duplicados.

Tambien se puede realizar la consulta si un usuario tiene permisos para emitir su voto, esta consulta muestra el estado de la persona, por ejemplo si una persona esta condenado o si esta en un proceso judicial.

A continuación se presenta los datos que este servicio puede recuperar.

<table>
<thead>
	<tr>
		<th>Atributo</th>
		<th>Tipo de dato</th>
	</tr>
</thead>
<tbody>
	<tr>
		<td>Nombres</td>
		<td>String</td>
	</tr>
	<tr>
		<td>Apellidos</td>
		<td>String</td>
	</tr>
	<tr>
		<td>Fecha de nacimiento</td>
		<td>Date</td>
	</tr>
	<tr>
		<td>Lugar de nacimiento</td>
		<td>String</td>
	</tr>
	<tr>
		<td>Nombre de la Madre</td>
		<td>String</td>
	</tr>
	<tr>
		<td>Nombre del Padre</td>
		<td>String</td>
	</tr>
	<tr>
		<td>Dpi</td>
		<td>Number</td>
	</tr>
	<tr>
	    <td>Apto</td>
	    <td>Boolean</td>
	</tr>
</tbody>
</table>
