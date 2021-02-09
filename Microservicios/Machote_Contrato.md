![Help Builder Web Site](./Logo.png)
# Proyecto_SA_Grupo2
### Modulo X

**ID: MS-X**
<br>
**Nombre: Base de datos**


<table>
<thead>
	<tr>
		<th>Historia de usuario</th>
	</tr>
</thead>
<tbody>
	<tr>
		<td>Trata acerca de</td>
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
		<td>Media</td>
		<td>10 puntos</td>
		<td>Sesión</td>
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
	<td>/api/bd</td>
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
		<td>par1</td> 
		<td>int</td>
		<td>recibe un int</td>
	</tr>
		<tr>
		<td>par2</td> 
		<td>string</td>
		<td>recibe un string</td>
	</tr>
		<tr>
		<td>par3</td> 
		<td>boolean</td>
		<td>recibe un boolean</td>
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
		<td>par1</td> 
		<td>int</td>
		<td>recibe un int</td>
	</tr>
		<tr>
		<td>par2</td> 
		<td>string</td>
		<td>recibe un string</td>
	</tr>
		<tr>
		<td>par3</td> 
		<td>boolean</td>
		<td>recibe un boolean</td>
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
		<td>Fallo en la autenticación</td>
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
		<td>El sistema debe ser Windows 10</td> 
	</tr>

</tbody>
</table>
<br>







