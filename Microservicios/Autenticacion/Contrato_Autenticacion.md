![Help Builder Web Site](../../Img/Logo.png)
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
	<td>POST</td>
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
		<td>Content-Type</td> 
		<td>Header</td>
		<td>Cabecera que identifica el tipo de contenido que a mandar y recibir por la aplicación.</td>
	</tr>
		<tr>
		<td>Data</td> 
		<td>Body</td>
		<td>Contiene los valores de las credenciales del usuario en formato JSON.</td>
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
		<td>401</td> 
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
		<td>Se espera que venga en Data el nombre de usuario y la contraseña</td> 
	</tr>
		<tr>
		<td>La contraseña tenga un minímo de 8  caracteres</td> 
	</tr>

</tbody>
</table>
<br>







