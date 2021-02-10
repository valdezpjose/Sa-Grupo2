![Help Builder Web Site](../Logo.png)
# Proyecto_SA_Grupo2
### Modulo Autenticación

**ID: MS-2**
<br>
**Nombre: Autenticación**


<table>
<thead>
	<tr>
		<th>Historia de usuario</th>
	</tr>
</thead>
<tbody>
	<tr>
		<td>COMO usuario QUIERO poder entrar a mi cuenta sin el peligro que alguien mas se haga pasar por mi, por lo que esperaría que el sistema de registro e ingreso si hagan las validaciones necesarias para autenticarme.</td>
	</tr>
</tbody>
</table>




<table>
<thead>
	<tr>
		<th>Prioridad</th>
		<th>Estimado</th>
		<th>Modulo</th>
	</tr>
</thead>
<tbody>
	<tr>
		<td>Alta</td>
		<td>10 puntos</td>
		<td>Autenticación</td>
	</tr>
</tbody>
</table>



**Criterios de Aceptación**
<br>
El servicio debe tener la siguiente configuración:
<br>
<table>
<tbody>
	<tr>
	<td>Ruta</td>
	<td>a definir</td>
	</tr>
	<tr>
	<td>Método</td>
	<td>GET</td>
	</tr>
	<tr>
	<td>Formato de entrada</td>
	<td>JSON</td>
	</tr>
</tbody>
</table>


**Parametros de Entrada**
<table>
<thead>
	<tr>
		<th>Atributo</th>
		<th>Tipo</th>
		<th>Descripción</th>
	</tr>
</thead>
<tbody>
	<tr>
		<td>Correo</td> 
		<td>string</td>
		<td>Recibe el correo del usuario y se manda a corroborar con el microservicio de Base de datos de iVoting.</td>
	</tr>
		<tr>
		<td>Contraseña</td> 
		<td>string</td>
		<td>Recibe la contraseña del usuario y se manda a corroborar con el microservicio de Base de datos de iVoting.</td>
	</tr>
	<tr>
		<td>DPI</td> 
		<td>string</td>
		<td>Recibe el DPI del usuario y se envía al microservicio de RENAP para comprobar información.</td>
	</tr>
		<tr>
		<td>Fecha de nacimiento</td> 
		<td>string</td>
		<td>Recibe la fecha de nacimiento del usuario y se envía al microservicio de RENAP para comprobar información. </td>
	</tr>
		<tr>
		<td>Nombre de padre y madre</td> 
		<td>string</td>
		<td>Recibe el nombre del padre y madre del usuario y se envía al microservicio de RENAP para comprobar información.</td>
	</tr>
</tbody>
</table>
<br>



<table>
<tbody>
	<tr>
	<td>Formato de Salida</td>
	<td>JSON</td>
	</tr>
	<tr>
	<td>Código de respuesta exitosa</td>
	<td>HTTP 200</td>
	</tr>
</tbody>
</table>

**Parametros de Salida Exitosa**
<table>
<thead>
	<tr>
		<th>Atributo</th>
		<th>Tipo</th>
		<th>Descripción</th>
	</tr>
</thead>
<tbody>
	<tr>
		<td>Si la respuesta es correcta se dejará seguir a la cuenta del usuario.</td> 
		<td>boolean</td>
		<td>Recibe una respuesta "True" en un formato JSON.</td>
	</tr>
		<tr>
		<td>Si despúes de 3 intentos la información no es valida no se podrá ingresar a la cuenta y se tendrá que volver a tratar de ingresar en un periodo de X horas.</td> 
		<td>boolean</td>
		<td>Recibe una respuesta "False" en un formato JSON.</td>
	</tr>

</tbody>
</table>
<br>

**Código de respuesta fallida**
<table>
<thead>
	<tr>
		<th>Código</th>
		<th>Descripción</th>
	</tr>
</thead>
<tbody>
	<tr>
		<td>403</td> 
		<td>Fallo en la autenticación, prohibido entrar</td>
	</tr>

</tbody>
</table>
<br>

**Validaciones requeridas**
<table>
<thead>
	<tr>
		<th>Validación</th>
	</tr>
</thead>
<tbody>
	<tr>
		<td>El formato de las fechas debe ser DD-MM-AAAA</td> 
		
	</tr>	
	<tr>
		<td>El formato del correo debe de ser xxxx@xxxx.xxxx</td> 
		
	</tr>
	<tr>
		<td>Cuando se escriba la contraseña, puede verse solo si se da a un botón de mostrar contraseña</td> 
		
	</tr>
	<tr>
		<td>El nombre del padre y la madre debe de tener el formato Xxxx Xxxx</td> 
		
	</tr>

</tbody>
</table>
<br>







