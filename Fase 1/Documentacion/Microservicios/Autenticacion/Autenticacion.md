![Help Builder Web Site](../../Img/Logo.png)
# Proyecto_SA_Grupo2
### Autenticación
Este documento tiene el objetivo de:
<br>
* Dar una descripción breve del microservicio de Autenticación.

Este microservicio se utilizara siempre al utilizar los microservicios de "registrar un nuevo usuario" o de "ingresar a la cuenta de un usuario". Por esto se piden los siguientes datos para verificarlos con 2 microservicios:

<table>
<thead>
	<tr>
		<th>Dato</th>
		<th>Microservicio</th>
	</tr>
</thead>
<tbody>
	<tr>
		<td>Correo</td>
		<td>BD iVoting</td>
	</tr>
	<tr>
		<td>Contraseña</td>
		<td>BD iVoting</td>
	</tr>
	<tr>
		<td>DPI</td>
		<td>BD RENAP</td>
	</tr>
	<tr>
		<td>Fecha de nacimiento</td>
		<td>BD RENAP</td>
	</tr>
	<tr>
		<td>Nombre del Padre del usuario</td>
		<td>BD RENAP</td>
	</tr>
	<tr>
		<td>Nombre del Madre del usuario</td>
		<td>BD RENAP</td>
	</tr>
</tbody>
</table>

El usuario tiene unicamente 3 intentos para ingresar estos datos, si al tercer intento los datos NO devuelven un valor "True" entonces se le presenta un mensaje de error al usuario.

Si se esta registrando un nuevo usuario y el valor es "False" después de mostrarle el mensaje de error se le vuelve al inicio para que inicie de nuevo todo el proceso de registro.

Si se esta ingresando a la cuenta y el valor es "False" después de mostrar el mensaje de error se bloquea la cuenta durante 12 horas.

Si el valor en efecto es "True" entonces si se estaba registrando se crear el nuevo usuario y si se estaba ingresando se deja entrar a la cuenta del usuario.









