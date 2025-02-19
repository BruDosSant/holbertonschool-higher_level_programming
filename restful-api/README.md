Resumen de la Estructura de HTTP

Estructura de la Petición:Línea de Petición: Método, URL, Versión HTTPEncabezados: Información sobre la solicitud (por ejemplo, agente de usuario, cookies)Cuerpo: Datos opcionales (generalmente en peticiones POST o PUT)Estructura de la Respuesta:Línea de Estado: Versión HTTP, Código de Estado, Mensaje de Estado

Encabezados: Información sobre la respuesta (por ejemplo, tipo de contenido, longitud)

Cuerpo: Los datos que se envían de vuelta (por ejemplo, HTML, JSON)HTTP methods:GET

Description: Retrieves data

Use case: Fetching a web page or data from an API.POST

Description: Sends data to the server to create or update a resource

Use case: Submitting form data, creating new records (e.g., user registration or a comment).PUT

Description: Updates an existing resource on the server

Use case: Replacing an entire resource or record, such as updating a user’s profile.DELETE

Description: Removes a resource from the server

Use case: Deleting a resource, such as removing an item from a shopping cart or deleting an account.HTTP Status Codes:200 OKDescription: The request was successful and the server returned the requested data.

Use case: The requested page or data has been successfully retrieved.302 FoundDescription: The requested resource is temporarily located at a different URL.

Use case: The resource has been temporarily moved, and the original URL will still be valid in the future.404 Not FoundDescription: The server cannot find the requested resource.

Use case: The page or resource doesn’t exist on the server.500 Internal Server ErrorDescription: The server encountered an error while processing the request.

Use case: There’s an issue on the server that prevents it from completing the request.

