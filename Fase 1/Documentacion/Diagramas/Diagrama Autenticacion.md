![Diagrama](../Img/Logo.png)

# Diagrama de actividades del microservicio de autenticación
***

## Descripción General


Este microservicio utilizará un modelo Cliente-Token en el cual el token es utilizado para indicar la identidad del usuario, el contenido del token se encontrará encriptado por cuestiones de seguridad. 

Se utilizará [JWT (Json Web Token) ][JWT] para definir el formato del token, asi mismo como su contenido y estructura de encriptación.
***

## Estructura del token JWT
La estructura consiste unicamente de 3 partes: Header, Payload y Signature.

#### Header
Header contiene el tipo, valor fijado como JWT y el algoritmo hash utilizado en JWT.

    {
        "typ": "JWT",
        "alg": "HS256"
    }`

#### Payload
Incluye informacion estandar la cual consiste en: user id, expiration date, y user name

    { 
        "id": 123, 
        "name": "Mena Meseha",
        "is_admin": true,
        "expire": 1558213420 
    }
#### Signature
Este campo es utilizado para el cliente para verificar la identidad del token.

    HMACSHA256(
      base64UrlEncode(header) + "." +
      base64UrlEncode(payload),
      secret
    )


Al utilizar esta estructura el resultado final obtenido sera parecido a esto:

    eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTIzLCJuYW1lIjoiTWVuYSBNZXNlaGEiLCJpc19hZG1pbiI6dHJ1ZSwiZXhwaXJlIjoxNTU4MjEzNDIwfQ.Kmy_2WCPbpg-aKQmiLaKFLxb5d3rOC71DHexncH_AcQ

***
## Flujo basico que el microservicio utiliza
![Flujo Basico][img1]

[img1]: https://miro.medium.com/max/875/0*4e6oPp1HYrmDm2CH.png "Error"

***

Para mayor informacion visitar el sitio web [JWT (Json Web Token)]: http:https://jwt.io/