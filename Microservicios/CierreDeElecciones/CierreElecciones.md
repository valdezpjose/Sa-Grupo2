![Logo](../../Img/Logo.png)

# Proyecto_SA_Grupo2

## Cierre de elecciones

En el sistema ***iVoting*** no es necesario ingresar nuevamente para cerrar las vataciones para una elección sino que cierra la elección automaticamente.

### Diagrama de actividades cierre de elección

Cuando los usuarios eligen una elección para votar, se debe de realizar una validación antes de seguir con el proceso. La validación es la siguiente:

*   Elección activa. El sistema desplegara la pantalla del proceso de votación

*   Elección inactiva. El sistema notificara al usuario si las elecciones fueron cerradas o si aun no ha iniciado.

![Cierre](../../Img/DiagramaActividadCierre.png)

<table>
<thead>
	<tr>
	    <th>Tipo</th>
		<th>Evento</th>
	</tr>
</thead>
<tbody>
	<tr>
		<td>Exito</td>
		<td>Desplegar pantalla proceso de votación</td>
	</tr>
	<tr>
	    <td>Error</td>
	    <td>Mostrar mensaje "Eleccion inactiva. Puede contactarse con el administrador para volver activar la eleccion"</td>
	</tr>
</tbody>
</table>

### Diagrama de secuencia para carga de votos

Esta opción de carga de reporte solamente lo puede realizar el usuario administrador. Se envia el reporte al servicio de cierre en donde procede a contar los votos encriptando la información para seguir con la seguridad de voto anonimo, este servicio genera un nuevo reporte y para guardar este reporte es enviado al servicio de auditoria.

El usuario adminsitrador puede revisar el informe guardado en auditoria por lo que el sistema se comunicara con el servicio de auditoria para que pueda proveer el informe que el usuario necesita.

![Carga](../../Img/DiagramaCargaVotos.png)

<table>
<thead>
	<tr>
		<th>Tipo</th>
		<th>Evento</th>
	</tr>
</thead>
<tbody>
	<tr>
	    <td>Exito</td>
		<td>Mostrar mensaje "Registro de votos cargado exitosamente" </td>
	</tr>
	<tr>
	    <td>Exito</td>
		<td>Desplegar informe</td>
	</tr>
	<tr>
	    <td>Error</td>
		<td>Mostrar mensaje "Error interno del servidor"</td>
	</tr>
</tbody>
</table>