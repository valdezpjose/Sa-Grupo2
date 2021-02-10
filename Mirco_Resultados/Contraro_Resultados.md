![Help Builder Web Site](../Logo.png)
# Proyecto_SA_Grupo2
### Modulo Resultados

**ID: MS-3**
<br>
**Nombre: Resultados**


<table>
<thead>
	<tr>
		<th>Historia de usuario</th>
	</tr>
</thead>
<tbody>
	<tr>
		<td>COMO usuario registrado QUIERO poder entrar al módulo de resultados y visualizar información general de la elección, la opción ganadora, cantidad de votos, cantidad de votantes registrados y graficas con información relevante</td>
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
		<td>Resultados</td>
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
		<td>Elección</td> 
		<td>string</td>
		<td>Recibe el nombre de la elección que se desea visulizar</td>
</tbody>
</table>
<br>



<table>
<tbody>
	<tr>
	<td>Formato de Salida</td>
	<td>Interfaz</td>
	</tr>
	<tr>
	<td>Información correspondiente a los resultados de la elección</td>
	<td>Gráficas y descripción</td>
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
		<td>Si la respuesta es correcta se mostrará la información de la elección</td> 
		<td>boolean</td>
		<td>Se podrán visualizar las gráficas y descripción de los votantes y la elección</td>
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
		<td>Fallo en la carga de la elección</td>
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
		<td>El usuario debe estar registrado y autenticado previamente</td> 
    </tr>
    <tr>
        <td>Los resultados se mostrarán solmente en gráfica de pie y barras</td>
    </tr> 
    <tr>
        <td>Por medio de un mapa se mostrarán los votos realizados en los diferentes depertamentos y municiopios</td>
    </tr> 
</tbody>
</table>

<br>

